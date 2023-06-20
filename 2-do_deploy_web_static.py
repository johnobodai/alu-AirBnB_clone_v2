#!/usr/bin/python3


from fabric.api import local, put, run, env
from datetime import datetime
import os

# Define the hosts
env.hosts = ['localhost']

def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the .tgz archive
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path

def do_deploy(archive_path):
    """Distribute an archive to the web servers"""
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

        # Delete the existing symbolic link
        local('rm -f hbnb_static')

        # Move the contents of temp_folder to the current directory
        local('mv temp_folder/* .')
        local('rm -rf temp_folder')

        # Create a symbolic link to the new version
        local('ln -s {} hbnb_static'.format(os.path.splitext(filename)[0]))

        return True
    except:
        return False

def deploy():
    """Pack and deploy the web_static folder"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

def clean():
    """Clean up the local directory"""
    local('rm -rf versions/*')
    local('rm -rf hbnb_static')

def do_deploy_web():
    """Deploy web_static to web servers"""
    if not deploy():
        return False

    # Upload the index file to the web servers
    put('web_static/0-index.html', '/tmp/')
    run('mkdir -p /data/web_static/releases/test/')
    run('mv /tmp/0-index.html /data/web_static/releases/test/')

    # Update the symbolic link to the new version
    run('rm -f /data/web_static/current')
    run('ln -s /data/web_static/releases/test/ /data/web_static/current')

    # Validate the deployment
    output_web01 = run('ls /data/web_static/releases/test/')
    output_web02 = run('ls /data/web_static/releases/test/')
    if '0-index.html' in output_web01 and '0-index.html' in output_web02:
        return True
    else:
        return False

def pep8():
    """Run PEP8 validation"""
    local('pep8 --first --exclude=tests/* fabfile.py')
