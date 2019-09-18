#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import os.path
import re
import argparse

__author__="ethan375"





def extract_names(filename):
    """alphabatizes and removes duplicates for baby names"""

    
# main function should pass one file and extract function should sort one file
# Sort the names in the file needs to be sorted alpha, both b/g 
# set does not allow duplicate entries as well dicts 
# 

    final_list = []
    name_rank = {}

    with open(filename) as open_file:
        for l in open_file:
            year_match_obj = re.search(r'Popularity\sin\s(\d\d\d\d)', l)
            if year_match_obj:
                # final_list.append(year.string[-10:-6])
                year = year_match_obj.group(1)
                final_list.append(year)
            match = re.search('<tr', l)
            if match:
                row = match.string
                match_obj = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', row)
                if match_obj:
                    rank, boy, girl = match_obj[0]
                    pass
                    name_rank[boy] = rank
                    name_rank[girl] = rank
    


    for val in name_rank:
        final_list.append(val + ' ' + name_rank[val])
    final_list = sorted(final_list)

    return final_list
                    
                


    

def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    create_summary = args.summaryfile

   
    for file in file_list:
         results = '\n'.join(extract_names(file)) + '\n'
         print(results)
         if create_summary:
             with open(file + '.summary', "w") as new_file:
                 new_file.write(results) 
            #  append_summary(pretty_results)

    




if __name__ == '__main__':
    main()
