#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import sys

import requests


def main(arguments):
    parser = argparse.ArgumentParser(description='Get list of HelpScout threads for a conversation')
    parser.add_argument('--token-id', required=True, help='HS auth access token')
    parser.add_argument('--convo-id', required=True, help='conversation id')
    parser.add_argument('--outfile', required=True, help='File to save threads')
    parser.add_argument('--loglevel', default='INFO')

    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=args.loglevel)

    url = f"https://api.helpscout.net/v2/conversations/{args.convo_id}/threads"
    headers = {
        'Authorization': f'Bearer {args.token_id}'
    }
    session = requests.Session()

    # first check the number of pages in the output
    try:
        r = session.get(url, headers=headers)
        r.raise_for_status()

        num_pages = r.json()['page']['totalPages']
        logging.info(f"Total pages: {num_pages}")

    except Exception as err:
        logging.error(f"Exception: {err}")
        return 1

    threads = []
    page = 1
    while (page <= num_pages):
        payload = {
            'page': f'{page}'
        }
        try:
            r = session.get(url, headers=headers, params=payload)
            r.raise_for_status()

            # each page response is json, with an array _embedded.conversations
            # containing a list of conversation items
            thr_page = r.json()['_embedded']['threads']
            for thr in thr_page:
                threads.append(thr)

        except Exception as err:
            logging.error(f"Exception: {err}")
            return 1
        page += 1

    logging.info(f"Number of threads: {len(threads)}")
    # write conversation list to a file
    outf = open(args.outfile, "w")
    # pretty print json to file
    json.dump(threads, outf, indent=4)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
