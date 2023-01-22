## About
Island counter project to parse '0' '1' grid and count all the islands that it constructs.

## How to run
### With docker
 * run _docker_build.sh_ script which will create application docker image
 * run _docker_run.sh script with a path to proper file as the first argument, it will create 
application docker container and run it with given argument\
e.g.:<br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _./docker_build.sh_\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _./docker_run.sh islands.txt_
### Without docker, clear python usage
   * run _simple_run.sh_ script with a path to proper file as the first argument\
e.g.:<br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_./simple_run.sh islands.txt_\
this app does not require any external python libraries, thus it can be launched directly using python executable 

## Warnings
Docker scripts for launching island counter were tested only in Windows 10 using Git Bash console.
There is a risk that they can fail on Linux at some reason. If they do, please try removing 
the _MSYS_NO_PATHCONV=1_ part from the _docker_run.sh_ script. It was used to ensure proper paths' strings
behaviour in Git Bash but can make some issues in real Linux enviromnemnt.
