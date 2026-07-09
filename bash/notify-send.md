# Show a popup, during unlimited time
```
notify-send -u critical -i dialog-information "Système" "Backup done."
```

# Show a popup, during limited time
```
notify-send -i dialog-information "Système" "Backup done."
```

# watch pattern on remote server
# n user@server:/path/log.log "pattern"
```
function n() {
    local user_server="${1%%:*}"
    local filepath="${1#*:}"
    local pattern="$2"
    
    local line=$(ssh "${user_server}" "tail -n0 -f \"${filepath}\" | grep --line-buffered -m1 \"${pattern}\"")
    
    if [ -n "$line" ]; then
        notify-send -u critical -i dialog-information "Pattern found : $(date +%T)" "server : ${user_server}\nfilepath : ${filepath}\npattern : ${pattern}\n\n${line}"
    fi
}
```
