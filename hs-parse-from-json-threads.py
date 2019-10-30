#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import sys


def main(arguments):
    parser = argparse.ArgumentParser(description='Parse messages from a json threads file, and create a browser-viewable file')
    parser.add_argument('--infile', required=True, help='json file containing threads from a HS conversation')
    parser.add_argument('--outfile', required=True, help='File to save parsed messages')
    parser.add_argument('--loglevel', default='INFO')

    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=args.loglevel)

    with open(args.infile, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    logging.info(f"Number of items in list: {len(obj)}")

    outf = open(args.outfile, "w")

    for item in obj:
        # we are only parsing threads of type:
        #   - "customer" (message from customer)
        #   - "message" (message to customer)
        #   - "note" (note)
        # for these, we get body, createdBy.email,
        # and createdAt fields

        item_type = item['type']
        if ((item_type == "customer")
           or (item_type == "message")
           or (item_type == "note")):
            outf.write("<h3>")
            if item_type == "note":
                outf.write('<font color="gray">Note ')
            outf.write(f"From: {item['createdBy']['email']}<br>")
            outf.write(f"Date: {item['createdAt']}")
            if item_type == "note":
                outf.write('</font>')
            outf.write("</h3>")
            outf.write(f"{item['body']}")
            outf.write(f"<hr>")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
