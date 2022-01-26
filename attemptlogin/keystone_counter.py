#!/usr/bin/python3

loginfail = 0
file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
file_lines = file.readlines()
for line in file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("total number of failed logins = ", loginfail)
file.close()

