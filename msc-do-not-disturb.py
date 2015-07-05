#!/usr/bin/python

'''
preflight script that disables munki notifications a certain day and time
adapted from a script by Graham Gilbert: 
https://github.com/grahamgilbert/mactech_2014/blob/master/Date_Preflight/preflight
'''

import datetime, sys, os

msc_dnd_file = "/Users/Shared/.uk.ac.bris.msc-do-not-disturb"
rm_cmd = "/bin/rm "+msc_dnd_file

current_date = int(datetime.datetime.today().strftime('%Y%m%d'))
current_time = int(datetime.datetime.now().strftime('%H'))

# get the timestamp date and hour of the DND file
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).strftime('%Y%m%d')
def modification_hour(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).strftime('%H')

# set the cancel time based on above
cancel_date = int(modification_date(msc_dnd_file))+1
cancel_hour = int(modification_hour(msc_dnd_file))

# only do anything if the bootstrap file exists
if os.path.isfile(msc_dnd_file):
    # if the cancel date is tomorrow set to true
    if current_date < cancel_date:
        os.system(
	        "/usr/bin/sudo /usr/bin/defaults write /Library/Preferences/ManagedInstalls.plist SuppressUserNotification -bool TRUE")
    # if the cancel date is today, check whether we have reached the hour to cancel yet - if so, set to true
    elif current_date == cancel_date:
        if current_time <= cancel_hour:
            os.system(
	            "/usr/bin/sudo /usr/bin/defaults write /Library/Preferences/ManagedInstalls.plist SuppressUserNotification -bool TRUE")
    # set to false and remove the bootstrap file if we've passed the time
    else:
        os.system(
            "/usr/bin/sudo /usr/bin/defaults write /Library/Preferences/ManagedInstalls.plist SuppressUserNotification -bool FALSE")
        os.system(rm_cmd)
else:
    os.system(
        "sudo defaults write /Library/Preferences/ManagedInstalls.plist SuppressUserNotification -bool FALSE")
    os.system(rm_cmd)
