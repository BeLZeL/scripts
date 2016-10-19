#----------------------------------------------------------
# Git and PS1
# curl -L https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh
source ~/.bash_git

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]$(__git_ps1):\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi

#----------------------------------------------------------
# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

#----------------------------------------------------------
# SSH-ADD called when terminal start for the first time
if [ $(ssh-add -l | grep -c "$HOME/.ssh") -eq 0 ]
then
    ssh-add
fi

#----------------------------------------------------------
# Shortcuts
json () { echo "$*" | perl -p -e "s/\n//g" | python -mjson.tool; }
xml  () { echo "$*" | perl -p -e "s/\n//g" | xmlstarlet fo -s 4; }
xml_root  () { echo "<xml_root>$*</xml_root>" | perl -p -e "s/\n//g" | xmlstarlet fo -s 4; }
echo_clean() { echo "$*" | perl -p -e "s/\s*\n/\n/g"; }
cat_clean () { cat "$*" | perl -p -e "s/\s*\n/\n/g"; }
cdl() { cd "$*" ; ll; }

#----------------------------------------------------------
# autocomplete ssh commands
complete -W "$(echo `cat ~/.bash_history | egrep '^ssh ' | sort | uniq | sed 's/^ssh //'`;)" ssh

#----------------------------------------------------------
# Alias
alias w='ssh -l www'
alias r='ssh -l root'
alias jessie64='schroot -c jessie-64 -p'
alias ll='ls -l'

#----------------------------------------------------------
# Functions

# Find an executable file in subdirectory
findbin () { find . -type f -executable -name "*$**"; }

# Show JSON
json () { echo "$*" | perl -p -e "s/\n//g" | python -mjson.tool; }

# Show XML
xml  () { echo "$*" | perl -p -e "s/\n//g" | xmlstarlet fo -s 4; }

# Show XML nodes
xml_root  () { echo "<xml_root>$*</xml_root>" | perl -p -e "s/\n//g" | xmlstarlet fo -s 4; }

# Remove trailing spaces
echo_clean() { echo "$*" | perl -p -e "s/\s*\n/\n/g"; }
cat_clean () { cat "$*" | perl -p -e "s/\s*\n/\n/g"; }

# Go and list directory
cdl() { cd "$*" ; ls -l; }

