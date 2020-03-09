#!/bin/bash
#
# Usage:
# ./deploy.sh <playbook.yml>
#

set -ex

if [[ ! -z "$VIRTUALENV" ]]; then
    echo "activate your virtualenv"
    exit 1
fi

playbook=$1
shift

ansible-playbook $playbook -e "ansible_python_interpreter=$(which python)" "$@"
