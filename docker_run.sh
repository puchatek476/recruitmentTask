#!/bin/bash
# script which creates islands-counter-app container and runs it with provided islands grid file as first param
# containers shuts down and removes itselfs automatically

if [ "$#" -lt 1 ]; then
    echo "Please provide path to a file with map, e.g. '/../islands.txt'"
elif [ "$#" -ne 1 ]; then
    echo "Please provide only one parameter - path to a file with map, e.g. '/../islands.txt'"
else
    path=$(realpath $1)
    if test -f "$path"; then
        # delete MSYS_NO_PATHCONV=1 part if met some issues
        MSYS_NO_PATHCONV=1 docker run --rm --name islands-counter-app -v $path:/application/islands.txt islands-counter islands.txt
    else
        echo "Provided path to file does not exists or points to a directory!"
    fi
fi
