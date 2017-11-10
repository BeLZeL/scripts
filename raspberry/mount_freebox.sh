#!/bin/bash
# sudo ./mount_freebox.sh
FREEBOX_DIR=/media/Freebox

#-------------------------------------------------------------------------------

if [ ! -d ${FREEBOX_DIR} ]
then
    sudo mkdir ${FREEBOX_DIR}
fi

#-------------------------------------------------------------------------------
# fstab
# //mafreebox.freebox.fr/Disque\040dur /media/Freebox cifs _netdev,rw,users,iocharset=utf8,uid=1000,sec=none,file_mode=0777,dir_mode=0777 0 0
# sudo mount -a

if [ -e /etc/fstab ]
then
    res=$(grep freebox /etc/fstab)
    if [ -z "${res}" ]
    then
        sudo echo "# Mount Freebox" >> /etc/fstab
        sudo echo "//mafreebox.freebox.fr/Disque\040dur ${FREEBOX_DIR} cifs _netdev,rw,users,iocharset=utf8,uid=1000,sec=none,file_mode=0777,dir_mode=0777 0 0" >> /etc/fstab
        res=$(grep freebox /etc/fstab)
        if [ -z "${res}" ]
        then
            echo "FSTAB : installation FAILED"
        else
            echo "FSTAB : installation OK"
        fi
    else
        echo "FSTAB : already installed"
    fi
else
    echo "FSTAB : can't install, file /etc/fstab doesn't exist"
fi

#-------------------------------------------------------------------------------
# crontab
# @reboot <cmd>

#if [ -e /etc/crontab ]
#then
#    res=$(grep freebox /etc/crontab)
#    if [ -z "${res}" ]
#    then
#        sudo echo "# Automount Freebox during boot" >> /etc/crontab
#        sudo echo "@reboot sudo mount -t cifs //mafreebox.freebox.fr/Disque\ dur ${FREEBOX_DIR} -o user=freebox,password=password,uid=1000,gid=1000,rw,sec=ntlm" >> /etc/crontab
#        res=$(grep freebox /etc/crontab)
#        if [ -z "${res}" ]
#        then
#            echo "CRONTAB : installation FAILED"
#        else
#            echo "CRONTAB : installation OK"
#        fi
#    else
#        echo "CRONTAB : already installed"
#    fi
#else
#    echo "CRONTAB : can't install, file /etc/crontab doesn't exist"
#fi

#-------------------------------------------------------------------------------

sudo mount -t cifs //mafreebox.freebox.fr/Disque\ dur ${FREEBOX_DIR} -o user=freebox,password=password,uid=1000,gid=1000,rw,sec=ntlm

ls ${FREEBOX_DIR}

#-------------------------------------------------------------------------------
