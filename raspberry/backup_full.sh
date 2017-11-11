#!/bin/bash
# ./backup_full.sh [ DEFAULT | MEDIAWIKI ]
source ~/check_remote_dir.sh

#-------------------------------------------------------------------------------

case ${MODE} in

DEFAULT)
    DD="FULL"
    ;;

MEDIAWIKI)
    recently_modified=$(sudo find /var/lib/mysql/wikidb -cmin -1440 -name "*")
    if [ ! -z "${recently_modified}" ]  
    then
		date +"%Y%m%d %H%M%S $0 : OK with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} : ${recently_modified}" >> ${REMOTE_DIR}/backup.log
        DD="FULL"
    fi
    ;;

*)
    date +"%Y%m%d %H%M%S $0 : Error with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} : Unknown MODE" >> ${REMOTE_DIR}/backup.log
    exit 1
    ;;

esac

#-------------------------------------------------------------------------------

case ${DD} in

FULL)
    sudo dd bs=1M conv=noerror,sparse if=/dev/mmcblk0 | xz --fast > ${REMOTE_DIR}/raspberry-$(date +"%A").img.xz
    ;;

ISO)
    sudo dd bs=2048 conv=noerror if=/dev/mmcblk0 of=${REMOTE_DIR}/raspberry-$(date +"%A").iso
    ;;
  
*)
    date +"%Y%m%d %H%M%S $0 : ERROR with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} and DD=${DD} : Unknown DD" >> ${REMOTE_DIR}/backup.log
    exit 1
    ;;
  
esac

#-------------------------------------------------------------------------------

date +"%Y%m%d %H%M%S $0 : End with MODE=${MODE} and REMOTE_DIR=${REMOTE_DIR} and DD=${DD}" >> ${REMOTE_DIR}/backup.log

#-------------------------------------------------------------------------------
