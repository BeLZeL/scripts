#!/bin/bash

#-------------------------------------------------------------------------------
# Mount Freebox before : ~/mount_freebox.sh
# sudo mount -t cifs //mafreebox.freebox.fr/Disque\ dur  /media/Freebox/ -o user=freebox,password=password,uid=1000,gid=1000,rw,sec=ntlm
#-------------------------------------------------------------------------------

# Check if Remote Dir is set
source ~/.bash_profile
if [ -z "${REMOTE_DIR}" ]
then
    date +"%Y%m%d %H%M%S $0 : Apply this command first : echo \"export REMOTE_DIR=/media/Freebox/<something>\" >> ~/.bash_profile" >> ~/backup.log
    exit
fi

#-------------------------------------------------------------------------------
# Check if Remote Dir exists
if [ ! -d "${REMOTE_DIR}" ]
then
    date +"%Y%m%d %H%M%S $0 : REMOTE_DIR=${REMOTE_DIR} is not found or valid" >> ~/backup.log
    exit
fi

#-------------------------------------------------------------------------------
# Check params : MODE might be DEFAULT, MEDIAWIKI
if [ $# -eq 0 ]
then
    MODE="DEFAULT"
else
    MODE=$1
fi

#-------------------------------------------------------------------------------

date +"%Y%m%d %H%M%S $0 : Start with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR}" >> ${REMOTE_DIR}/backup.log

#-------------------------------------------------------------------------------
