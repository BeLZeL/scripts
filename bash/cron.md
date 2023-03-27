#------------------------------------------------------------------------------
# Cron using date

* * * * * date +"\%H:\%M:\%S" >> /tmp/debug.log
* * * * * touch /tmp/file_$(date +"\%H-\%M-\%S")

#------------------------------------------------------------------------------
# Cron every two weeks (thursday 10:00)
00 10   * * 4 ~/run.sh

$ head ~/run.sh
[ `date "+scale=0; (%s/86400)%14" | bc -l` -lt 7 ] && exit 0

#------------------------------------------------------------------------------
# Cron first friday for each month (20:00)
# OK : %w day of week (0..6); 0 is Sunday
00 20 1-7 * * [ "$(date '+\%w')" -eq 5 ] && /path/script.sh
# NOK : because every 1-7 OR friday
00 20 1-7 * 5 /path/script.sh

#------------------------------------------------------------------------------
# Restart every day, but write a specific file on Sunday (DO NOT use "echo")
# OK :
00 20 * * * something stop ; [ "$(date '+\%w')" -eq 0 ] && printf "Hello\nWorld" >> /tmp/reset.log ; something start ; 
# NOK : https://serverfault.com/questions/169706/strange-problem-with-crontab-and-echo
00 20 * * * something stop ; [ "$(date '+\%w')" -eq 0 ] && echo -e "Hello\nWorld" >> /tmp/reset.log ; something start ;

#------------------------------------------------------------------------------
# Generate a backup
crontab -l > ~/crontab_save/crontab_save_$(date +"%Y%m%d_%H%M%S")

#------------------------------------------------------------------------------
# Modify with sed
crontab -l | sed 's/a/b/g' | crontab -
