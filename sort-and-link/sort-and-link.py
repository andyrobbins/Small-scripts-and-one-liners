#!/usr/bin/python

import glob 
import argparse
import os
import shutil

# The primary logic for moving files into their corresponding folders
# is from a stackoverflow answer by user "cji", which you can find here:
# http://stackoverflow.com/questions/13446857/how-to-match-and-move-files-into-corresponding-folders-using-python

parser = argparse.ArgumentParser(description='sort-and-link tool by wald0')
parser.add_argument('-s', '--srcpath', help='the directory to pull PNGs from', action='store')
parser.add_argument('-d', '--destpath', help='the destination root directory', action='store')

args = parser.parse_args()

srcpath = sorted(glob.glob(args.srcpath + "*.jpg"))
destpath = args.destpath

def masterIndex(path):
    html_str = "<a href=" + path + "/index.html>" + path + "</a><br>"
    try:
        with open(destpath + "index.html", "a") as html_file:
            html_file.write(html_str)
            print "I wrote a link for " + path
    except:
        pass

#This function takes input (ie: /root/scan/192.168.1.2:443.png) and returns the corresponding /24 (ie: 192.168.1.0)
def first3(input):
    first3 = input.split("/")[-1]
    first3 = (".".join(first3.split(".")[0:3])) + ".0"
    return first3

#This function creates new directories and adds them to the master index file
def create(dirname, destpath):
    full_path = os.path.join(destpath, dirname)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        masterIndex(dirname)
    return full_path

#This function moves files into a specified directory, and either appends the existing index.html or creates one
def move(filename, dirpath):
    if "443" in filename:
        html_str = '<a target="_blank" href=https://' + '.'.join(filename.split('/')[-1].split('.')[:-1]) + ">" + filename.split("/")[-1] + "</a><br><img src=./" + filename.split("/")[-1]  + " width=800><br><br>"
    else:
        html_str = '<a target="_blank" href=http://' + '.'.join(filename.split('/')[-1].split('.')[:-1]) + ">" + filename.split("/")[-1] + "</a><br><img src=./" + filename.split("/")[-1]  + " width=800><br><br>"
    try:
        shutil.move(os.path.join(srcpath, filename),dirpath)
        try:
            with open(dirpath + "/index.html", "a") as html_file:
                html_file.write(html_str)
        except:
            with open(dirpath + "/index.html", "w") as html_file:
                html_file.write(html_str)
    except:
        pass

destdirs = list(first3(filename) for filename in srcpath)

targets = [(folder, create(folder, destpath)) for folder in destdirs]

for dirname, full_path in targets:
    for filename in srcpath:
        if dirname == first3(filename):
            move(filename, full_path)
