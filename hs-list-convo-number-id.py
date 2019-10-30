#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import sys


def main(arguments):
    parser = argparse.ArgumentParser(description='Get list of conversation number and id pairs from conversation list json file')
    parser.add_argument('--infile', required=True, help='conversation list json file')
    parser.add_argument('--outfile', required=True, help='File to save number and id pairs')
    parser.add_argument('--loglevel', default='INFO')

    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=args.loglevel)

    with open(args.infile, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    logging.info(f"Number of items in list: {len(obj)}")

    outf = open(args.outfile, "w")
 
    for conv in obj:
        conv_id = conv['id']
        conv_number = conv['number']
        outf.write(f"{conv_number} {conv_id}\n")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
