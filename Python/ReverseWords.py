#!/usr/bin/python

import argparse
import os

# Grab our argument values with ArgParse
parser = argparse.ArgumentParser(description='Reverse the words in a sentence')
parser.add_argument('-f', '--file', help='The file to reverse words on', action='store')

args = parser.parse_args()
inputFile = args.file

reversedText = []

# Open our file and read it to "originalText"
with open(inputFile) as file:
    originalText = file.read()
    originalText = originalText.split()
    for word in originalText:
        word = word[::-1] # Flip the order of the letters in each 'word'
        reversedText.append(word) # Add the reversed word to "reversedText"

print ' '.join(reversedText)
