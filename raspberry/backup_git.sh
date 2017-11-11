#!/bin/bash
source ~/check_remote_dir.sh

#-------------------------------------------------------------------------------

GIT_REPO="${REMOTE_DIR}/git"
if [ ! -d ${GIT_REPO} ]
then
    mkdir ${GIT_REPO}
	cd ${GIT_REPO}
	git init
	git config --global user.email "pi@pi"
    git config --global user.name "pi"
fi

#-------------------------------------------------------------------------------

# Generate crontab
crontab -l >  ${GIT_REPO}/crontab

# Generate dpkg
dpkg -l > ${GIT_REPO}/dpkg.txt

# Copy home (-a = -rlptgoD, remove -g and -o)
rsync -rlptDvz --exclude "*.log" --delete ~/ ${GIT_REPO}/home

# Copy etc
rsync -rlptDvz \
	/etc/fstab \
	/etc/apt/sources.list \
	/etc/apt/sources.list.d/raspi.list \
	${GIT_REPO}/etc

#-------------------------------------------------------------------------------

case ${MODE} in

DEFAULT)
    ;;

MEDIAWIKI)
    rsync -rlptDvz \
        /etc/mediawiki/mediawiki.conf \
        /etc/mediawiki/LocalSettings.php \
        /etc/apache2/apache2.conf \
        ${GIT_REPO}/mediawiki
    ;;

*)
    date +"%Y%m%d %H%M%S $0 : Error with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} : Unknown MODE" >> ${REMOTE_DIR}/backup.log
    exit 1
    ;;

esac

#-------------------------------------------------------------------------------

# Commit to Git
git -C ${GIT_REPO} add -A
git -C ${GIT_REPO} commit -m "$(date)"

#-------------------------------------------------------------------------------

date +"%Y%m%d %H%M%S $0 : End with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} and GIT_REPO=${GIT_REPO}" >> ${REMOTE_DIR}/backup.log

#-------------------------------------------------------------------------------
