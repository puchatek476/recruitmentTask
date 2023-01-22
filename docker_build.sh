#!/bin/bash
# script which builds islands-counter image

echo Building image, please wait...
docker build --no-cache -t islands-counter . &> /dev/null
echo Image islands-counter successfully created!
