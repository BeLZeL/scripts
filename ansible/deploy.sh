    #!/usr/bin/env bash

    set -o errexit
    set -o pipefail
    #set -o nounset cannot be used because ANSIBLE_OPTIONS might be empty


    # Default options ##############################################################
    SUBSET_HOSTS=localhost
    INVENTORY=staging
    DRY_RUN=1

    # Usage ########################################################################
    function usage {
        echo "Usage: $0 -i staging -l localhost

    Options:
      -i INVENTORY, --inventory-file=INVENTORY
                            specify inventory host path or comma separated host list.
                            SET TO \"${INVENTORY}\" IF NOT PROVIDED.

      -h, --help            show this help message and exit

      -l SUBSET, --limit=SUBSET
                            further limit selected hosts to an additional pattern
                            SET TO \"${SUBSET_HOSTS}\" IF NOT PROVIDED.

      --no-dry-run          -C (--check) flag of ansible-playbook is enabled by default. Use
                            this option to disable it.

    See 'ansible-playbook --help' for more options."
    }


    # Options management ###########################################################
    ANSIBLE_OPTIONS=()
    while [[ $1 ]]; do
        case $1 in
            -l|--limit)
                SUBSET_HOSTS="$2"
                shift 2
                ;;

            -h|--help)
                usage
                exit 0;
                ;;
            -i|--inventory)
                INVENTORY="$2"
                shift 2
                ;;
            --no-dry-run)
                DRY_RUN=0
                shift
                ;;
            *)
                ANSIBLE_OPTIONS+=("$1")
                shift
                ;;
        esac
    done

    DRY_RUN_OPTION="-C"
    if [ $DRY_RUN -eq 0 ]; then
       echo "##############################################"
       echo "# /!\    Warning: Check mode disabled    /!\ #"
       echo "#     ALWAYS TEST CHANGES BEFORE DEPLOY!     #"
       echo "##############################################"
       DRY_RUN_OPTION=""
    fi


    # Main #########################################################################

    #pushd "$(git rev-parse --show-toplevel)"
    echo "Command executed: ansible-playbook deploy.yml ${DRY_RUN_OPTION} -D -i $INVENTORY -l $SUBSET_HOSTS ${ANSIBLE_OPTIONS[@]}"

    ansible-playbook deploy.yml ${DRY_RUN_OPTION} -D -i "$INVENTORY" -l "$SUBSET_HOSTS" "${ANSIBLE_OPTIONS[@]}"

    RESULT=$?
    #popd
    echo
    if [ $RESULT -eq 0 ]; then
        if [ $DRY_RUN -eq 1 ]; then
            echo "Everything seems to be fine, you can now relaunch the script with --no-dry-run option"
        else
            # We add or move a tag to notify what commit is deployed on the server
            git tag -f "$SUBSET_HOSTS"
            git push origin "$SUBSET_HOSTS" --force
        fi
    else
        echo "Fail: fix your playbook before using --no-dry-run"
        exit $RESULT
    fi

