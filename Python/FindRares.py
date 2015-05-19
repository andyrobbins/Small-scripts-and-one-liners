#!/usr/bin/python

import argparse
import os

# Grab our argument values with ArgParse
parser = argparse.ArgumentParser(description='Find rares characters in a file')
parser.add_argument('-f', '--file', help='The file to find rare characters in', action='store')

args = parser.parse_args()
inputFile = args.file

# Open our file and read each it into "raw"
with open(inputFile) as file:
    raw = file.read()
    characters = list(raw)
    charCount = {}
    for character in characters: # Count each character occurence
        if character in charCount:
            charCount[character] += 1
        else:
            charCount[character] = 1

# Find the characters that occur less than 10 times and report on them    
    for character in charCount:
        if charCount[character] < 10:
            occurence_or_occurences=' occurence!'
            if charCount[character] > 1:
                occurence_or_occurences=' occurences!'
            print character + ' is rare with only ' + str(charCount[character]) + occurence_or_occurences
