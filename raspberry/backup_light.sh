#!/bin/bash
# ./backup_light.sh [ DEFAULT | MEDIAWIKI ]
source $(dirname $0)/check_remote_dir.sh

#-------------------------------------------------------------------------------

LIGHT_DIR="${REMOTE_DIR}/light"
if [ ! -d ${LIGHT_DIR} ]
then
    mkdir ${LIGHT_DIR}
fi

#-------------------------------------------------------------------------------

# Generate crontab
crontab -l >  ${LIGHT_DIR}/crontab

# Generate dpkg
dpkg -l > ${LIGHT_DIR}/dpkg.txt

# Copy home (-a = -rlptgoD, remove -g and -o)
rsync -rlptDvz --exclude "*.log" --delete ~/ ${LIGHT_DIR}/home

# Copy etc
rsync -rlptDvz \
	/etc/fstab \
	/etc/apt/sources.list \
	/etc/apt/sources.list.d/raspi.list \
	${LIGHT_DIR}/etc

#-------------------------------------------------------------------------------

case ${MODE} in

DEFAULT)
    sudo tar -hcvJf ${REMOTE_DIR}/backup_light_${MODE}_$(date +"%Y%m%d").txz \
        ${LIGHT_DIR}/*
    ;;

MEDIAWIKI)
    mysqldump --user=root --password="${MYSQL_PASSWD}" wikidb > ${LIGHT_DIR}/wikidb.sql
    sudo tar -hcvJf ${REMOTE_DIR}/backup_light_${MODE}_$(date +"%Y%m%d").tar.xz \
        ${LIGHT_DIR}/* \
        /etc/mediawiki/mediawiki.conf \
        /etc/mediawiki/LocalSettings.php \
        /etc/apache2/apache2.conf \
		/var/lib/mediawiki/images \
		/var/lib/mediawiki/extensions
    ;;



*)
    date +"%Y%m%d %H%M%S $0 : Error with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} and LIGHT_DIR=${LIGHT_DIR}: Unknown MODE" >> ${REMOTE_DIR}/backup.log
    exit 1
    ;;

esac

#-------------------------------------------------------------------------------

date +"%Y%m%d %H%M%S $0 : End with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR}" >> ${REMOTE_DIR}/backup.log

#-------------------------------------------------------------------------------
