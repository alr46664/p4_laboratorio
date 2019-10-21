#!/bin/bash
ln -sf "$(pwd)" "$HOME/Desktop/"
sudo chmod -R +rwx "$(pwd)"
sudo pip install -U Flask
echo -e "\nalias firefox='sudo su p4 -c \"firefox &> /dev/null &\"'\n" >> "$HOME/.bashrc"