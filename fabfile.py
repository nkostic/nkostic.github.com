from __future__ import with_statement

import os.path

from fabric.api import *
from fabric.contrib.project import *

env.user = 'root'
env.hosts = ['80.169.183.93']
env.remote_dir = '/mnt/persist/www/helloper.com'

def deploy(where=None):
  rsync_project(
    env.remote_dir,
    '_site/',
    ['.git', '.git*', 'fabfile.py*', 'config.rb', 'README.md', '.DS_Store', 'Users/', '.sass-cache*'],
    False
  )
