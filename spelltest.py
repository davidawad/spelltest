#!/usr/bin/python

from bs4 import BeautifulSoup
import argparse
import enchant
import urllib
import yaml
import math
import os

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="directory to look through", default=os.getcwd())

args = parser.parse_args()

d = enchant.Dict("en_US")

# iterate over each file to spellcheck in config
# TODO read yaml file for info

def yield_files_with_extensions(folder_path, file_extension):
   for root, dirs, files in os.walk(folder_path):
       for file in files:
           if file.endswith(file_extension):
               fpath = root + '/' + file
               yield fpath

target_files = yield_files_with_extensions(args.target, '.html')

word_count = 0
bad_words  = []

for index, filename in enumerate(target_files):
    print("Looking for spelling errors in {0}".format(filename))
    with open(filename, 'r') as f:
        page = f.read()

        # pass page content to BS4 function
        soup = BeautifulSoup(page, "html.parser")

        # Find all of the text between paragraph tags and strip out the html
        page = soup.findAll('p')

        # assert that all text content is properly spelled english words.
        for tag in page:
            tag_content = tag.get_text()
            # print(tag_content)
            # check each word the string
            for word in tag_content.split():
                word_count += 1
                # TODO use regex for string replacement
                word = word.replace(',','').replace('.','').replace('?','')
                if not d.check(word):
                    bad_words.append(word)
                    # print(word, d.check(word))

stats = "Mispelled Words: {0}, Total Words: {1}, Percentage Incorrect: {2}%"
percentage = len(bad_words) / word_count
percentage = (math.ceil(percentage*100)/100)

stats = stats.format(len(bad_words), word_count, percentage)
print(stats)
print('_'*20)
print(bad_words)
