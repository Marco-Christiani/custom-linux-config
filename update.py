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


def run_cmd(cmd, loading_msg, complete_msg):
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
		print()
		print(output.stdout.decode('utf-8'))

def notify(title, text):
	cmd = f'osascript -e \'display notification \"{text}\" with title \"{title}\"\''
	os.system(cmd)

def get_available_updates():
	print('AHHHHHHHHHHH')
	cmd = shlex.split('brew outdated')
	output = subprocess.run(cmd, stdout=subprocess.PIPE)
	result = output.stdout.decode('utf-8').strip()

	cmd = shlex.split('brew cask outdated')
	output = subprocess.run(cmd, stdout=subprocess.PIPE)
	result += output.stdout.decode('utf-8').strip()
	# print(repr(result))
	if result == '':
		return None
	outdated_list = result.split('\n')
	# return outdated_list
	notify(f'Brew: {len(outdated_list)} outdated', ', '.join(outdated_list))
	# Send notif for number of updates

def update():
	"""
	Update homebrew package index, then upgrade all packages and gui apps (cask)
	"""
	run_cmd('brew update', 
			'Updating Homebrew package index',
			'✅ Homebrew package index updated')
	run_cmd('brew outdated',
			'Querying upgradable packages',
			'✅ Queried upgradable packages')
	run_cmd('brew cask outdated',
			'Querying upgradable Casks',
			'✅ Queried upgradable Casks')
	valid = False
	while not valid:
		response = input('Continue with upgrades? (Y/n)')
		valid = response in ['Y', 'n']

	if response == 'Y':
		run_cmd('brew upgrade',
			'Upgrading packages',
			'✅ Upgraded packages')
		run_cmd('brew cask upgrade',
			'Upgrading Casks',
			'✅ Upgraded Casks')
	else:
		print(colors.FAIL+colors.BOLD+'Exiting without upgrading'+colors.ENDC)
	# print(subprocess.check_output(['ls','-'], shell=True))

if __name__ == '__main__':
	# update()
	get_available_updates()

# print(get_available_updates())