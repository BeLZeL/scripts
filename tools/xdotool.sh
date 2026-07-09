#!/bin/bash

# Ouvrir un nouveau terminal
xdotool key ctrl+alt+t

# Attendre 1 seconde pour s'assurer que le terminal est ouvert
sleep 1
xdotool type "date"
xdotool key Return

# Attendre 1 seconde pour s'assurer que le terminal est ouvert
sleep 1
xdotool type "$(printf 'date\r')"
sleep 1; xdotool type $'date\n'
sleep 1; xdotool type $'date\r'
