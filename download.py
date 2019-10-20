#!/usr/bin/env python
"""
Download data products from GitHub.
"""
import yaml

import argparse
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('config',nargs='?',default='config.yaml',
                    help='configuration file')
args = parser.parse_args()

print("Downloading data for mw-sats...")

config = yaml.safe_load(open(args.config,'r'))

baseurl = config['download']['url']
release = config['download']['release']
filename = config['download']['filename']
url = '%(url)s/releases/download/%(release)s/%(filename)s'%config['download']

cmd = 'wget %s'%url
print(cmd)
#subprocess.check_call(cmd,shell=True)

cmd = 'tar -xzf %s'%filename
print(cmd)
#subprocess.check_call(cmd,shell=True)
