# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:46:19 2017

@author: Home
"""


import subprocess

retcode = subprocess.call('sudo docker ps', shell=True)
