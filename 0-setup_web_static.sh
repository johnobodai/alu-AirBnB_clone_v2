#!/usr/bin/env bash
# Bash script  to set up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx >/dev/null 2&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

