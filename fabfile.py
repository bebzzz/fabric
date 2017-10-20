from fabric.api import sudo, env, roles, execute, put, run, local, lcd, prompt, cd, parallel
import os
from creds import *

user_to_create = 'ansible'
sshport = ssh_port

env.user = ssh_user
env.password = ssh_pass
env.hosts = ssh_hosts



def createUser():
    sudo("useradd -m -d /home/"+user_to_create+" -s /bin/bash ansible", pty=True)
    sudo("echo "+user_to_create+":"+securepass+" | chpasswd")
    sudo("""su - """+user_to_create+""" -c "ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -q -N ''" """)

