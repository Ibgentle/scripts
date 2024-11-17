#!/usr/bin/env python3

__author__ = 'Ibor E. Offor'
__designation__ = 'Technical Manager'
__email__ = 'iboroffor@gmail.com'

"""

A script to download voice call recordings from the
server matching a given phone number and date...

"""

from paramiko import SSHClient, AutoAddPolicy
import re


if __name__ == "__main__":
    # Get date, and phone number as input from the user
    date_input = input('Enter the year, month, and date in the format YYYY/MM/DD: ')
    phone_num = input('Enter the phone without the leading zero: ')

def recordings(phone_num, date_input):
    call_recordings = 'cd $RECORDINGS/' + date_input + ' ; ' + 'ls -t | grep -Z ' + phone_num + ' | ' + 'xargs cp -t /root/call_recordings/'
    client = SSHClient()
    # LOAD HOST KEYS: keys that have been added to the host .ssh file
    client.load_host_keys('C:/Users/ECC/.ssh/known_hosts')
    client.load_system_host_keys()
    # Known_host policy: add new host to list of trusted devices
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect('172.16.30.65', username='root',
        password='icdadmin')
    stdin, stdout, stderr = client.exec_command(call_recordings)
    # open an SFTP session, change to directory in the path, and list files
    ftp_client = client.open_sftp()
    ftp_client.chdir('/root/call_recordings')
    stdout = ftp_client.listdir('.')
    # For each file in the listing, download the file
    for i in stdout:
        ftp_client.get('./%s'%(i), 'C:/Users/Public/Downloads/%s'%(i))
    ftp_client.close()
    # Remove the files temporarily copied to the created directory on the server
    stdin, stdout, stderr = client.exec_command('rm -f /root/call_recordings/*')
    # Clean-up: don't leave these guys open...they don't like that!
    stdin.close()
    stdout.close()
    stderr.close()
    client.close()

recordings(phone_num, date_input)
print("Done! Go to 'C:/Users/Public/Downloads' to see the files")
