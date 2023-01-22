#!/bin/bash
# script to

path=$(realpath $1)

if test -f "$path"; then
    python main.py $path
else
    echo "Provided path to file does not exists or points to a directory!"
fi