#!/usr/bin/env python3

"""copying and moving files into different directory"""
import shutil   #utility to move files
import os       #low level os operations access

def main():
    os.chdir('/home/student/mycode/')               #changing the working directory
    shutil.move('raynor.obj', 'ceph_storage/')      #moving the file into new directory
xname = input('What is the new name for kerrigan.obj? ') #getting user's input for file name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)   #moving and changing name as input

main()
    
