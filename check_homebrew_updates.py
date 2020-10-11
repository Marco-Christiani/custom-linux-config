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

def notify(title, text):
	cmd = f'osascript -e \'display notification \"{text}\" with title \"{title}\"\''
	os.system(cmd)

def get_available_updates():
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

if __name__ == '__main__':
	get_available_updates()

