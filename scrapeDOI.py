#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import re
import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='PDF DOI Scraper.')
parser.add_argument('directory',help='PDF file directory',action='store')
args = parser.parse_args()

print(args)
print args.directory


PATTERN = r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'])\S)+)\b'

# Patterns taken from http://crosstech.crossref.org/2015/08/doi-regular-expressions.html, https://doeidoei.wordpress.com/2009/10/22/regular-expression-to-match-a-doi-digital-object-identifier/
OTHER_PATTERNS = [r'/^10.\d{4,9}/[-._;()/:A-Z0-9]+$/i', r'/^10.1002/[^\s]+$/i', r'/^10.\d{4}/\d+-\d+X?(\d+)\d+<[\d\w]+:[\d\w]*>\d+.\d+.\w+;\d$/i', r'/^10.1207/[\w\d]+\&\d+_\d+$/i', r'[doi|DOI][\s\.\:]{0,2}(10\.\d{4}[\d\:\.\-\/a-z]+)[A-Z\s]']


#data = sys.stdin.read()

def doi_search(text):
    DOI_search  = re.search(PATTERN, text)
    if not DOI_search:
        for x in OTHER_PATTERNS:
            DOI_search = re.search(x, text)
            if DOI_search:
                return DOI_search
    return DOI_search

DOIs_found = []
DOIs_not_found = []

for file in os.listdir(args.directory):
    filePath = os.path.join(args.directory, file)
   
    if file.endswith(".pdf"):

        proc =  subprocess.Popen(["pdftotext", "-layout", filePath, "-"], stdout=subprocess.PIPE)
        output = proc.stdout.read()
        find_doi = doi_search(output)
        if find_doi:
           DOIs_found.append( (file, find_doi.group(0))   )
        else:
            DOIs_not_found.append(file)

print "DOIs found:"
print DOIs_found

print "\n\n DOIs not found for:"
print DOIs_not_found

