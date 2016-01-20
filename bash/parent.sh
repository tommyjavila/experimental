#!/bin/bash

# This is a parent script that will launch 7 other scripts

set script1.sh script2.sh script3.sh script4.sh script5.sh script6.sh script7.sh
echo

while [ "$#" -gt 0 ]
do
    bash "$1"
    if [ "$?" -eq 0 ]; then
        shift
    else
        echo "error executing $1"
        echo "The following scripts didn't complete: $@"
        echo
        exit 1
    fi
done
