# munki-do-not-disturb

*A "Do Not Disturb" application for Munki's Managed Software Center*

This is a simple application created using AppleScript. When the application is 
run, a hidden file at `/Users/Shared/.com.grahamrpugh.msc-do-not-disturb` is created.

A preflight script is placed at `/usr/local/munki/preflight` or 
`/usr/local/munki/preflight.d/msc-do-not-disturb.py` 
which checks for the presence of, and the timestamp of the hidden file at the start of a 
Munki run. If the file is present and less than 24 hours old, the 
`SuppressUserNotification` Preference in `ManagedInstalls.plist` is set to `TRUE` so that 
Managed Software Center will not issue pop-up notifications.

## Packaged release version

If you have Sal or MunkiReport-PHP installed, you should be safe to install the 
packaged release on the Releases tab.  Do not use this if you only have 
MunkiWebAdmin installed.  To be on the safe side, check a client for the presence of a 
pre-existing `/usr/local/munki/preflight` file and `/usr/local/munki/preflight.d/` 
directory. If you have both or neither, you are safe.

## Making your own version

* Install [The Luggage](http://grahamgilbert.com/blog/2013/08/09/the-luggage-an-introduction/).
* Clone this project and open `Managed Software Center Do Not Disturb.scpt`
* Make any amendments and Export as an app. You'll want to sign it.
* If you wish to add an alternative image to the app, follow the instructions [here](http://superuser.com/questions/37811/how-can-i-change-an-application-icon-in-mac-os-x)
* If you want the version number to be anything other than 1.0, edit the `CFBundleShortVersionString` key in `/path/to/Managed Software Center Do Not Disturb.app/Contents/Info.plist` 
* Edit `postinstall` with any amendments to the location of the preflight script.
* Run `make pkg` to compile the package which consists of the app and the preflight script.

## Importing to Munki

It's most likely you'll want to distribute this as a self-service app in Munki. Run `munkiimport /path/to/MSC-Do-Not-Disturb.pkg` and edit the resulting pkginfo file: 
the uninstall keys should be something like:

```xml
	<key>uninstall_method</key>
	<string>uninstall_script</string>
	<key>uninstall_script</key>
	<string>#!/bin/sh
/bin/rm -rf "/Applications/Managed Software Center Do Not Disturb.app" \
/usr/local/munki/preflight.d/msc-do-not-disturb.py
/usr/bin/defaults write /Library/Preferences/ManagedInstalls.plist SuppressUserNotification -bool FALSE
/usr/sbin/pkgutil --forget uk.ac.bris.MSC-Do-Not-Disturb</string>
	<key>uninstallable</key>
	<true/>
```
