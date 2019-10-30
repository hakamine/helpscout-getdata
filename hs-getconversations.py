#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import sys

import requests


def main(arguments):
    parser = argparse.ArgumentParser(description='Get list of HelpScout conversations')
    parser.add_argument('--token-id', required=True, help='HS auth access token')
    parser.add_argument('--outfile', required=True, help='File to save conversation list')
    parser.add_argument('--loglevel', default='INFO')

    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=args.loglevel)

    url = "https://api.helpscout.net/v2/conversations"
    headers = {
        'Authorization': f'Bearer {args.token_id}'
    }
    payload = {
        'status': 'all'
    }
    session = requests.Session()

    # first check the number of pages in the output
    try:
        r = session.get(url, headers=headers, params=payload)
        r.raise_for_status()

        num_pages = r.json()['page']['totalPages']
        logging.info(f"Total pages: {num_pages}")

    except Exception as err:
        logging.error(f"Exception: {err}")
        return 1

    conversations = []
    page = 1
    while (page <= num_pages):
        payload = {
            'status': 'all',
            'page': f'{page}'
        }
        try:
            r = session.get(url, headers=headers, params=payload)
            r.raise_for_status()

            # each page response is json, with an array _embedded.conversations
            # containing a list of conversation items
            convs_page = r.json()['_embedded']['conversations']
            for conv in convs_page:
                conversations.append(conv)

        except Exception as err:
            logging.error(f"Exception: {err}")
            return 1
        page += 1

    logging.info(f"Number of conversations: {len(conversations)}")
    # write conversation list to a file
    outf = open(args.outfile, "w")
    # pretty print json to file
    json.dump(conversations, outf, indent=4)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
