#!/usr/bin/env python
'''
USEAGE:

apache_log_parser_split.py some_log_file

This script takes one command line argument: the name of a log file to parse.
It then parses the log file and generates a report which associates remote
hosts with number of bytes transferred to them.
'''

import sys 

def dictify_logline(line):
    '''return a dictionary of the pertinent pieces of an apache combined log file
    
    Currently, the only fields we are instrested in are remote host and bytes sent,
    but we are putting status in there just for good measure.
    '''
    split_line = line.split()
    return {'remote_host': split_line[0],
            'status': split_line[8],
            'bytes_sent': split_line[9],
            }

