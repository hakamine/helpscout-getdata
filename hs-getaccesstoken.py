#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys

import requests


def main(arguments):
    parser = argparse.ArgumentParser(description='Get HelpScout access token')
    parser.add_argument('--loglevel', default='INFO')
    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=args.loglevel)

    # Check if the required env vars are defined, exit if not
    try:
        hs_app_id = os.environ['HELPSCOUT_APP_ID']
        hs_app_secret = os.environ['HELPSCOUT_APP_SECRET']
    except KeyError as e:
        logging.error("env var not defined: {}".format(e))
        raise SystemExit(1)

    url = "https://api.helpscout.net/v2/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'client_id': '{}'.format(hs_app_id),
        'client_secret': '{}'.format(hs_app_secret),
    }
    r = requests.post(url, data=data)
    print(r.text)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
