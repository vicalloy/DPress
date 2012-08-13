#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

from helper import run

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "../")
tools_folder = os.path.join(root, "tools/")
env = os.path.join(root, "env/")

pip = os.path.join(env, "Scripts/pip.exe")
if os.name == 'posix':
    pip = os.path.join(env, "bin/pip")

python = "python"
try:
    import config
    python = getattr(config, "python", python)
except:
    pass

def do_pip():
    print '== do_pip =='
    requirements = os.path.join(root, 'requirements.txt')
    run("%s install -r %s" % (pip, requirements))

if __name__ == '__main__':
    virtualenv_py = os.path.join(tools_folder, "virtualenv.py")
    print '== create env =='
    if not os.path.exists(env): 
        run('%s %s %s' % (python, virtualenv_py, env))
    do_pip()
