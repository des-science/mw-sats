#!/usr/bin/env python
"""
Download data files from GitHub
"""
baseurl = 'https://github.com/des-science/mw-sats/releases/download/'
version = 'v0.1'
filnames = []

for filename in filenames:
    url = baseurl + '/' + version + '/' + filename
    os.system('curl %s -O %s'%(url,filename))
