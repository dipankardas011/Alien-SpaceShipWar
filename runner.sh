#!/bin/bash

python3 -m pip install -r requirements.txt

echo $(tput setaf 3)$(tput bold)Starting$(tput init) "Starting"

python3 alien_invasion.py

if [ $? == 'False' ]; then
  echo $(tput setaf 1)$(tput bold)ERROR$(tput init) "Internal Error"
else
  echo $(tput setaf 2)$(tput bold)Done$(tput init) "Exited Successfully"
fi