#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx >/dev/null 2&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

