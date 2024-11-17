#!/usr/bin/env python3

__author__ = 'Offor'
__designation__ = 'Technical Manager'
__email__ = 'iboroffor@gmail.com'

"""
    A simple script to check the status of fop2 service,
    and start it up, if it isn't running. My pleasure...
"""

from paramiko import SSHClient, AutoAddPolicy
import webbrowser
import time
import re

client = SSHClient()

# LOAD HOST KEYS: keys that have been added to the host .ssh file
client.load_host_keys('C:/Users/ECC/.ssh/known_hosts')
client.load_system_host_keys()
# Known_host policy: add new host to list of trusted devices
client.set_missing_host_key_policy(AutoAddPolicy())

if __name__ == "__main__":
    # connect to the server to check status of fop2 service,
    client.connect('172.16.30.65', username='root',
        password='icdadmin')
    stdin, stdout, stderr = client.exec_command('service fop2 status')
    
    # Read the output of the command which will be returned as a list
    # Slice the list and select the section showing fop2 current status
    # Use regular expression to find the word 'running' in the text
    fop2_status = stdout.readlines()[2]
    fop2_running = re.search('running', fop2_status)

    # If the service isn't running, then start it up baby...
    if bool(fop2_running) == False:
        client.exec_command('service fop2 start')
    else:
        client.exec_command('service fop2 stop')
        time.sleep(3)
        client.exec_command('service fop2 start')
        
    stdin, stdout, stderr = client.exec_command('service fop2 start')

    # Clean-up: don't leave these guys open...they don't like that!
    stdin.close()
    stdout.close()
    stderr.close()
    client.close()

    # wait for 2 seconds, and open browser...before everywhere go bust
    time.sleep(2)
    # Finally, open the web browser to show fop2 login page. Una wedon o!
    webbrowser.open('172.16.30.65/fop2/')
    




