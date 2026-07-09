#!/usr/bin/env python3
# $ pylint --extension-pkg-whitelist=wx cliptray.py
# pylint: disable = missing-docstring, invalid-name, unused-argument, broad-exception-caught, line-too-long

"""
Cliptray - Smart clipboard monitoring application with system tray icon
"""

import logging
import os
import re
import subprocess
import sys
import threading
import webbrowser
from enum import IntEnum, auto
from typing import Optional, Callable

try:
    import pyperclip
except ModuleNotFoundError:
    print("Please install pyperclip (apt install python3-pyperclip)", file=sys.stderr)
    sys.exit(-1)

try:
    import wx
    import wx.adv
except ModuleNotFoundError:
    print("Please install wxpython (apt install python3-wxgtk4.0)", file=sys.stderr)
    sys.exit(-1)

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths
NOTES_DIR = os.path.expanduser('~/Documents/Cliptray/notes/')
TODO_DIR = os.path.expanduser('~/Documents/Cliptray/todo.txt')

# Icon background colors
COLOR_BLACK = wx.Colour(0, 0, 0, 255)
COLOR_BLUE = wx.Colour(0, 155, 255, 255)
COLOR_YELLOW = wx.Colour(255, 255, 0, 255)
COLOR_GREEN = wx.Colour(0, 255, 0, 255)

class ProbeState(IntEnum):
    UNMATCHED = auto()
    HTTPS = auto()
    TASK = auto()
    FILE = auto()
    REFRESH_START = auto()
    REFRESH_STOP = auto()


class ProbeRule:
    def __init__(self, *, # https://stackoverflow.com/questions/816391/avoiding-pylint-warnings-about-too-many-arguments
                 state: ProbeState,
                 pattern: str,
                 letter: str,
                 description: Callable = lambda content: f"{content}",
                 color: wx.Colour = COLOR_GREEN,
                 action: Optional[Callable] = None):
        self.state = state
        self.pattern = pattern
        self.color = color
        self.letter = letter
        self.description = description
        self.action = action
        self.regex = re.compile(pattern) if pattern is not None else None

    def matches(self, content: str) -> bool:
        if self.regex is not None:
            return bool(self.regex.match(content))
        return False

    def print_description(self, content: str):
        if self.state != ProbeState.UNMATCHED:
            logger.info("Match type '%s' using '%s'", self.state.name, self.description(content))

    def execute_action(self, content: str):
        try:
            logger.info("Action type '%s' using '%s'", self.state.name, self.description(content))
            if self.action:
                self.action(content)
        except Exception as e:
            logger.error("Error executing action for %s: %s", self.state.name, e)

# Default unmatched rule
RULE_UNMATCHED = ProbeRule(
        state=ProbeState.UNMATCHED,
        pattern=None,
        letter='',
        color=COLOR_BLACK,
    )

# Define all probe rules
PROBE_RULES = [
    ProbeRule(
        state=ProbeState.HTTPS,
        pattern=r'^https://[^\s\n]+$',
        letter='H',
        action=webbrowser.open,
    ),
    ProbeRule(
        state=ProbeState.TASK,
        pattern=r'^T#\d+$',
        letter='T',
    ),
    ProbeRule(
        state=ProbeState.FILE,
        pattern=r'^note:[^\s\n]+\.txt$',
        letter='F',
        description=lambda content: f"{NOTES_DIR}{re.sub(r'^note:', '', content)}",
        action=lambda content: subprocess.run(['kate', f"{NOTES_DIR}{re.sub(r'^note:', '', content)}"], check=True),
    ),
    ProbeRule(
        state=ProbeState.REFRESH_START,
        pattern=None,
        color=COLOR_YELLOW,
        letter='*',
        description=lambda: "Refresh tasks",
    ),
    ProbeRule(
        state=ProbeState.REFRESH_STOP,
        pattern=None,
        color=COLOR_BLACK,
        letter='',
    ),
]


class ClipboardMatcher:
    @classmethod
    def get_rule(cls, asking_for_type: ProbeState) -> ProbeRule:
        for rule in PROBE_RULES:
            if rule.state == asking_for_type:
                return rule
        return RULE_UNMATCHED

    @classmethod
    def find_matching_rule(cls, content: str) -> ProbeRule:
        for rule in PROBE_RULES:
            if rule.matches(content):
                return rule
        return RULE_UNMATCHED

    @classmethod
    def get_probe_state(cls, content: str) -> ProbeState:
        rule = cls.find_matching_rule(content)
        return rule.state


class CliptrayIcon(wx.adv.TaskBarIcon):
    def __init__(self, parent_frame):
        super().__init__()
        self.last_clipboard_content = ""
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(250)  # 250 ms
        self.has_activate = False
        self.parent_frame = parent_frame

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_click)

        # Set initial icon
        self.rule = ClipboardMatcher.get_rule(ProbeState.UNMATCHED)
        self.SetIcon(self.generate_icon(), f'Cliptray :\n\n{self.last_clipboard_content[:1024]}')

        # Init todolist
        self.refresh()

    def generate_icon(self):
        """Create a bitmap with color and letter"""
        letter = self.rule.letter
        color = self.rule.color
        square_size = 24
        font_size = 12

        # Create a bitmap of size 24x24
        bitmap = wx.Bitmap(square_size, square_size)
        dc = wx.MemoryDC(bitmap)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()

        # Draw the letter in the center
        dc.SetPen(wx.Pen(wx.Colour(255, 255, 255), 1))  # White
        dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255)))

        # Set font
        font = wx.Font(font_size, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        dc.SetFont(font)

        # Calculate center position
        text_width, text_height = dc.GetTextExtent(letter)
        x = (square_size - text_width) // 2
        y = (square_size - text_height) // 2

        # Draw the text
        dc.DrawText(letter, x, y)
        dc.SelectObject(wx.NullBitmap)
        return wx.BitmapBundle.FromBitmap(bitmap)

    def on_timer(self, event):
        if self.rule.state == ProbeState.REFRESH_START:
            self.SetIcon(self.generate_icon(), f'Cliptray :\n\n{self.last_clipboard_content[:1024]}')
        else:
            self.generate_icon_with_clipboard()
            self.check_keyboard_shortcut()

    def generate_icon_with_clipboard(self):
        try:
            content = pyperclip.paste()
            if content != self.last_clipboard_content or self.rule.state == ProbeState.REFRESH_STOP:
                self.last_clipboard_content = content
                self.rule = ClipboardMatcher.find_matching_rule(content)
                self.rule.print_description(content)
                self.SetIcon(self.generate_icon(), f'Cliptray :\n\n{self.last_clipboard_content[:1024]}')
        except Exception as e:
            logger.error("Error reading clipboard: %s", e)

    def check_keyboard_shortcut(self):
        try:
            # Get keyboard state
            ctrl = wx.GetKeyState(wx.WXK_CONTROL)
            scroll = wx.GetKeyState(wx.WXK_SCROLL)

            if ctrl and scroll and self.has_activate is False:
                self.do_something()
                self.has_activate = True
            elif not ctrl and not scroll and self.has_activate is True:
                self.has_activate = False
        except Exception as e:
            print(f"Error here: {e}")

    def on_left_click(self, event):
        self.do_something()

    def do_something(self):
        if self.rule.state != ProbeState.UNMATCHED:
            if self.rule.state == ProbeState.TASK:
                self.edit_or_delete_task()
            else:
                self.rule.execute_action(self.last_clipboard_content)

    def CreatePopupMenu(self):
        """
        Override wxTaskBarIcon::CreatePopupMenu()
        https://docs.wxpython.org/wx.adv.TaskBarIcon.html#wx.adv.TaskBarIcon.CreatePopupMenu
        """
        menu = wx.Menu()

        # Refresh
        refresh_item = menu.Append(wx.ID_ANY, "Refresh")
        self.Bind(wx.EVT_MENU, self.on_refresh, refresh_item)

        menu.AppendSeparator() # ------------------------------

        # Task submenu
        task_submenu = wx.Menu()

        # Task > New
        new_item = task_submenu.Append(wx.ID_ANY, "New task")
        self.Bind(wx.EVT_MENU, self.on_new, new_item)

        # Task > Edit
        edit_item = task_submenu.Append(wx.ID_ANY, "Edit task")
        self.Bind(wx.EVT_MENU, self.on_edit, edit_item)

        # Task > Delete
        delete_item = task_submenu.Append(wx.ID_ANY, "Delete task")
        self.Bind(wx.EVT_MENU, self.on_delete, delete_item)

        # Add Task submenu to main menu
        menu.AppendSubMenu(task_submenu, "Task")

        menu.AppendSeparator() # ------------------------------

        # Quit
        quit_item = menu.Append(wx.ID_EXIT, "Quit")
        self.Bind(wx.EVT_MENU, self.on_quit, quit_item)

        return menu

    def on_refresh(self, event):
        self.refresh()

    def on_process_finished(self, returncode):
        logger.info("Process finished with return code: %s", returncode)
        wx.CallAfter(self.rule_set_unmatched)

    def rule_set_unmatched(self):
        self.rule = ClipboardMatcher.get_rule(ProbeState.REFRESH_STOP)

    def refresh(self):
        logger.info("refresh")
        self.rule = ClipboardMatcher.get_rule(ProbeState.REFRESH_START)
        #command = "/home/user/Documents/Cliptray/refresh.sh"
        command = "sleep 1"
        run_process_async(command, self.on_process_finished)

    def on_new(self, event):
        logger.info("New task")
        with wx.TextEntryDialog(self.parent_frame, "Enter a new task:", "Input", "") as dialog:
            dialog.SetSize((1200, -1))
            dialog.Centre()
            if dialog.ShowModal() == wx.ID_OK:
                user_input = dialog.GetValue()
                if user_input.strip():
                    result = subprocess.run(['sed', '-i', f'$a\\ {user_input.strip()}', TODO_DIR], capture_output=True, text=True, check=True)
                    logger.info(result)
                    self.refresh()

    def on_edit(self, event):
        logger.info("Edit task")

        if self.rule.state == ProbeState.TASK:
            task_number = self.last_clipboard_content.split('#')[1]
        else:
            with wx.TextEntryDialog(self.parent_frame, "Enter a task #", "T#", "") as dialog:
                if dialog.ShowModal() != wx.ID_OK:
                    return
                user_input = dialog.GetValue()
                task_number = int(user_input.strip())

        with wx.TextEntryDialog(self.parent_frame, "Edit this task:", "Input", "") as dialog:
            result = subprocess.run(['sed', '-n', f"{task_number}p", TODO_DIR], capture_output=True, text=True, check=True)
            line = result.stdout.strip()
            dialog.SetValue(line)
            dialog.SetSize((1200, -1))
            dialog.Centre()
            if dialog.ShowModal() == wx.ID_OK:
                user_input = dialog.GetValue()
                if user_input.strip():
                    line_number = task_number # escape characters for sed
                    escaped_content = user_input.replace('\\', '\\\\').replace('/', '\\/')
                    sed_command = [
                        'sed',
                        '-i',
                        f'{line_number}s/.*/ {escaped_content}/',
                        TODO_DIR
                    ]
                    logger.info(subprocess.run(sed_command, check=True))
                    self.refresh()

    def on_delete(self, event):
        self.delete_task()

    def edit_or_delete_task(self):
        logger.info("Edit task")

        # Récupérer la ligne à éditer
        result = subprocess.run(['sed', '-n', f"{self.last_clipboard_content.split('#')[1]}p", TODO_DIR],
                                capture_output=True, text=True, check=True)
        line = result.stdout.strip()

        # Créer une fenêtre personnalisée
        dialog = wx.Dialog(self.parent_frame, title="Edit or Delete this task", size=(1200, 130))

        # Créer les éléments de l'interface
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Texte d'instruction
        #instruction = wx.StaticText(dialog, label="Edit this task:")
        #main_sizer.Add(instruction, 0, wx.ALL | wx.EXPAND, 5)

        # Champ de saisie texte (une seule ligne)
        text_ctrl = wx.TextCtrl(dialog, style=wx.TE_LEFT | wx.TE_PROCESS_ENTER)
        text_ctrl.SelectNone()
        text_ctrl.SetValue(line)

        # Augmenter la taille de la police
        font = text_ctrl.GetFont()
        font.SetPointSize(11)  # Augmentation de la taille de la police
        text_ctrl.SetFont(font)

        text_ctrl.SetMaxSize((1200, -1))  # Limite la hauteur

        main_sizer.Add(text_ctrl, 0, wx.ALL | wx.EXPAND, 10)

        # Boutons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Bouton OK
        ok_btn = wx.Button(dialog, wx.ID_OK, "OK")
        ok_btn.SetDefault()
        button_sizer.Add(ok_btn, 0, wx.ALL, 2)

        # Bouton Cancel
        cancel_btn = wx.Button(dialog, wx.ID_CANCEL, "Cancel")
        button_sizer.Add(cancel_btn, 0, wx.ALL, 2)

        # Bouton Delete
        delete_btn = wx.Button(dialog, wx.ID_DELETE, "Delete")
        button_sizer.Add(delete_btn, 0, wx.ALL, 2)

        main_sizer.Add(button_sizer, 0, wx.CENTER, 5)

        dialog.SetSizer(main_sizer)
        dialog.Centre()

        # Gérer l'événement de suppression
        def on_delete(event):
            # Vous pouvez ajouter une confirmation ici si nécessaire
            dialog.EndModal(wx.ID_DELETE)

        delete_btn.Bind(wx.EVT_BUTTON, on_delete)

        # Afficher la boîte de dialogue
        result = dialog.ShowModal()

        if result == wx.ID_OK:
            user_input = text_ctrl.GetValue()
            if user_input.strip():
                line_number = self.last_clipboard_content.split("#")[1]
                escaped_content = user_input.replace('\\', '\\\\').replace('/', '\\/')
                sed_command = [
                    'sed',
                    '-i',
                    f'{line_number}s/.*/ {escaped_content}/',
                    TODO_DIR
                ]
                logger.info("Edit OK for %s with %s", line_number, escaped_content)
                logger.info(subprocess.run(sed_command, check=True))
                self.refresh()

        elif result == wx.ID_DELETE:
            # Gérer le cas de suppression
            line_number = self.last_clipboard_content.split("#")[1]
            sed_command = [
                'sed',
                '-i',
                f'{line_number}d',
                TODO_DIR
            ]
            logger.info("Delete OK for %s", line_number)
            logger.info(subprocess.run(sed_command, check=True))
            self.refresh()
        elif result == wx.ID_CANCEL:
            logger.info("Cancel")
            # Ne rien faire en cas d'annulation
            pass

        dialog.Destroy()

    def delete_task(self):

        if self.rule.state == ProbeState.TASK:
            task_number = self.last_clipboard_content.split('#')[1]
        else:
            with wx.TextEntryDialog(self.parent_frame, "Enter a task #", "T#", "") as dialog:
                if dialog.ShowModal() != wx.ID_OK:
                    return
                user_input = dialog.GetValue()
                task_number = int(user_input.strip())

        logger.info("task deleted ?")
        result = subprocess.run(['sed', '-n', f"{task_number}p", TODO_DIR], capture_output=True, text=True, check=True)
        line = result.stdout.strip()
        if wx.MessageBox(line, f"Delete task T#{task_number} ?", wx.OK | wx.CANCEL | wx.ICON_INFORMATION) == wx.OK:
            logger.info("ok")
            subprocess.run(['sed', '-i', f"{task_number}d", TODO_DIR], check=True)
            self.refresh()

    def on_quit(self, event):
        self.timer.Stop()
        wx.GetApp().ExitMainLoop()

class CliptrayApp(wx.App):
    def __init__(self):
        super().__init__()
        self.tray_icon = None

    def OnInit(self):
        frame = wx.Frame(None) # mandatory and don't call frame.Show()
        self.tray_icon = CliptrayIcon(frame)
        return True

def run_process_async(command, callback):
    def target():
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            callback(result.returncode)
        except Exception as e:
            logger.error("Error in run_process_async: %s", e)

    thread = threading.Thread(target=target)
    thread.start()
    return thread

if __name__ == '__main__':
    app = CliptrayApp()
    app.MainLoop()
