#!/usr/bin/python3

from fabric.api import local, put, env
import os

# Define the hosts
env.hosts = ['localhost']

def do_deploy(archive_path):
    """Distribute an archive to the web server"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory
        put(archive_path, '/tmp/')
        
        # Extract the archive to the current directory
        filename = os.path.basename(archive_path)
        local('mkdir -p temp_folder')
        local('tar -xzf /tmp/{} -C temp_folder'.format(filename))

        # Delete the archive from the local machine
        local('rm /tmp/{}'.format(filename))

        # Delete the existing index.html file, if it exists
        local('rm -f index.html')

        # Move the contents of temp_folder to the current directory
        local('mv temp_folder/web_static/* .')
        local('rm -rf temp_folder')

        return True
    except:
        return False

