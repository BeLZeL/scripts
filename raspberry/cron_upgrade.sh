#!/bin/bash
# ./cron_upgrade.sh
source $(dirname $0)/check_remote_dir.sh                                                                                                                                                                                               

#-------------------------------------------------------------------------------

echo "--------------" >> ${REMOTE_DIR}/cron_upgrade.log
res=$(sudo aptitude update 2> /dev/null)
date +"%Y%m%d %H%M%S $0 : update : 
${res}" >> ${REMOTE_DIR}/cron_upgrade.log

echo "--------------" >> ${REMOTE_DIR}/cron_upgrade.log
res=$(sudo aptitude upgrade --quiet=2 -y --no-new-upgrades --no-new-installs --download-only 2> /dev/null)
date +"%Y%m%d %H%M%S $0 : upgrade :
${res}" >> ${REMOTE_DIR}/cron_upgrade.log

echo "--------------" >> ${REMOTE_DIR}/cron_upgrade.log
res_lines=$(echo "${res}" | grep "The following packages will be upgraded")
date +"%Y%m%d %H%M%S $0 : lines :
${res_lines}" >> ${REMOTE_DIR}/cron_upgrade.log
   
echo "--------------" >> ${REMOTE_DIR}/cron_upgrade.log
if [ ! -z "${res_lines}" ]
then
    date +"%Y%m%d %H%M%S $0 : 
********************************************************
sudo aptitude upgrade
********************************************************

${res}" >> ${REMOTE_DIR}/cron_upgrade.log
fi

#-------------------------------------------------------------------------------

date +"%Y%m%d %H%M%S $0 : End with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR}" >> ${REMOTE_DIR}/backup.log

#-------------------------------------------------------------------------------
