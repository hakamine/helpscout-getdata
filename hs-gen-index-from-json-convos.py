#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import sys


def main(arguments):
    parser = argparse.ArgumentParser(description='Generate an html index file from a json conversations file')
    parser.add_argument('--infile', required=True, help='json file containing list of HS conversations')
    parser.add_argument('--outfile', required=True, help='File to save generated index file')
    parser.add_argument('--loglevel', default='INFO')

    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=args.loglevel)

    with open(args.infile, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    logging.info(f"Number of items in list: {len(obj)}")

    outf = open(args.outfile, "w")

    outf.write("<html>")
    outf.write("<head>")
    outf.write('<meta charset="utf-8">')
    outf.write("<title>Help Scout Conversations</title>")
    outf.write('<link href="minimal-table.css" rel="stylesheet" type="text/css">')
    outf.write("</head>")
    outf.write("<body><table>\n")

    for item in obj:
        # For each conversation we display:
        # - number
        # - subject
        # - createdAt
        # - primaryCustomer.email

        logging.info(f"Processing conversation number:{item['number']} id:{item['id']}")
        outf.write("<tr>\n")
        outf.write(f"<td><a href='hs{item['number']}.html'>{item['number']}</a></td>\n")
        try:
            outf.write(f"<td>{item['subject']}</td>\n")
        except KeyError:
            outf.write("<td>(none)</td>\n")

        outf.write(f"<td>{item['createdAt'][0:10]}</td>\n")
        try:
            outf.write(f"<td>{item['primaryCustomer']['email']}</td>\n")
        except KeyError:
            outf.write("<td>(none)</td>\n")

        outf.write("</tr>\n")

    outf.write("</body></table></html>\n")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
