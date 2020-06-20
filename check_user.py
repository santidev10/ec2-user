#!/usr/bin/env python3
import sys, os, subprocess, pwd, grp, getpass, time, shutil, re
from time import strftime
def die(msg):
    print(msg)
    os._exit(1)

def checkuser(name):
   try:
       return pwd.getpwnam(name)
   except KeyError: 
       return None

def getfirst():
    fn = ""
    try:
        while len(fn) == 0: 
            fn = input("First Name: ")
            print(fn)
    except KeyboardInterrupt: 
        die("Interrupt detected, exiting.")
    return fn

def getlast():
    ln = ""
    try:
        while len(ln) == 0: 
            ln = input("Last Name: ")
    except KeyboardInterrupt: 
            die("Interrupt detected, exiting.")
    return ln

def getusername(fn, ln):
    user = ""
    # Build username from first letter in 'fn' and up to 7 letters in 'ln'
    # Is this the best way to do it?
    fn1 = fn[0:1].lower()		# get first character
    ln = ln.replace(" ", "")		# remove empty spaces, if any
    ln7 = ln[0:7].lower()		# get first 7 characters
    user_rec = fn1 + ln7
    if checkuser(user_rec):
        print("user existe")
    return user_rec

def main():
    print(os.system("python3 --version")) 
    print("Enter user information:")
    fn = getfirst()
    print(fn)
    ln = getlast()
    print(fn,ln)
    username=getusername(fn,ln)
    print(username)

if __name__ == "__main__":
    main()


