#!/usr/local/bin/python3

import subprocess
import time
import shlex
import os
from yaspin import yaspin
from yaspin.spinners import Spinners

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_cmd(cmd, loading_msg, complete_msg, suppress_output=False):
	"""
	Runs terminal command.
	Goes straight to stdout, no need to return or print.
	"""
	with yaspin(Spinners.arc, text=loading_msg) as spinner:
		spinner.color = 'red'
		output = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE)
		spinner.text = ''
		spinner.color = None
		spinner.ok(complete_msg)
		if not suppress_output:
			print()
			print(output.stdout.decode('utf-8'))
		return output.stdout.decode('utf-8')

def update():
	"""
	Update homebrew package index, then upgrade all packages and gui apps (cask)
	"""
	run_cmd('brew update', 
			'Updating Homebrew package index',
			'✅ Homebrew package index updated', suppress_output=True)
	upgraded_pkgs = run_cmd('brew outdated',
						'Querying upgradable packages',
						'✅ Queried upgradable packages')
	upgraded_casks = run_cmd('brew outdated --cask',
			'Querying upgradable Casks',
			'✅ Queried upgradable Casks')
	run_cmd('brew upgrade',
			'Upgrading packages',
			'✅ Upgraded packages')
	run_cmd('brew upgrade --cask',
			'Upgrading Casks',
			'✅ Upgraded Casks')
	print(colors.OKGREEN+colors.UNDERLINE+'Upgraded packages:'+colors.ENDC) # this is actually packages ATTEMPTED to upgrade (need to add error checking)
	print(upgraded_pkgs)
	print(colors.OKGREEN+colors.UNDERLINE+'Upgraded Casks:'+colors.ENDC)
	print(upgraded_casks)
	# check to see if errors occured during upgrade (i.e. 'Error: The `brew link` step did not complete successfully')
	# print(colors.FAIL+colors.BOLD+'Exiting without upgrading'+colors.ENDC)

if __name__ == '__main__':
	update()
