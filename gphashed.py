#!/usr/bin/env python3
# =============================================================
# Course/Lab: SecureSet
# Filename: loginhash.py
# Author: Cyrus Field
# Purpose: Continued development of login: add loop with 5 login chances
# =============================================================
# Goals Nested if statements using uList and pList
# List uList and pList for initial login and define them
# uList: root,admin,user pList: password,admin,SpaceJam
# Continued Development on login.py into login2.py
# Added multiple users and passwords still indicating root:password correct
# Def correct username:password combo from [lists]
# Correct login is still root:password even multiple entries in the lists
# Setup loop to count attempts and deny access after 5 failed attempts
# Created loginDict removed lists for user:pass
# New if statement using loginDict to verify user and pass key
# def login earlier but didn't annotate it
# import getpass to hide user password entries
# replaced input for password with getpass.getpass
# Continuing dev, adding logging and hashing for encryption
# Logging pieces from github ED-209-MK7/PythonSnippets
import getpass
import hashlib
from datetime import datetime,date

LOG = "/var/tmp/login.log"
# Logging in Linux based host
# Start the log file
def startLogFile():
    try:
        now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        if not path.isfile(LOG):
            with open(LOG, 'a') as log:
                log.write(now + " - Log Started.\n")
            return('Succeeded')
        else:
            with open(LOG, 'a') as log:
                log.write(now + " - Log Started. Strange, the log file appears to exist already?  Continuing anyways.\n")
            return('Succeeded')
    except:
        return('Failed')
# For now just simply exit here
        exit(1)
def writeToLog(stringToLog):
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG, 'a') as log:
        log.write(now + " - " + stringToLog + '\n')
# Original login
def login():
    print("Thank You! ")
loggedin = False
count = 0
while (count < 6) and loggedin != True:
    loginDict = {'root': 'c4a4e4a0556f39a3057dfc4a13225f38', 'admin': '1a66d97ecac3dccaa9bc3e5bc333b31a', 'user': 'db04a18d3ad5d4df92b0a231cea3e07e'}
    Username = input("Please enter your username:")
    if Username == 'root':
        writeToLog("Attempted Root Login")
    writeToLog("Attempted Login")
# Assigns UTF-8
    salt = "$uperma@n"
    print(salt)
    Password = getpass.getpass("Please enter your password:")
    hash_object = hashlib.md5(Password.encode("utf-8") + salt.encode('utf-8')).hexdigest()
    print(hash_object)
    count = count + 1

    if Username in loginDict.keys() and hash_object == loginDict[Username]:
        loggedin = True
        writeToLog("Login Successful")
        print("Successfully logged in: ")
# loop for 5 login attempts
    elif count >= 5:
        if Username == 'root':
            print("This incident has been reported")
        writeToLog("Max failed attempts reached, this event will reported")
        print("Access denied, to many failed attempts!!! ")
        break
    else:
        print("Access denied. Try again!")
# Added logging for failed attempt root instance and basic user
        if Username == 'root':
            writeToLog("Failed Root Login")
        writeToLog("Failed login Attempt")
login()
