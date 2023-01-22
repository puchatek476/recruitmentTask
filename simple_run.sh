#!/bin/bash
# script to run application with pure python, without docker

if [ "$#" -lt 1 ]; then
    echo "Please provide path to a file with map, e.g. '/../islands.txt'"
elif [ "$#" -ne 1 ]; then
    echo "Please provide only one parameter - path to a file with map, e.g. '/../islands.txt'"
else
    path=$(realpath $1) &> /dev/null

    if test -f "$path"; then
        python main.py $path
    else
        echo "Provided path to file does not exists or points to a directory!"
    fi
fi
