#!/bin/bash

file="data/list_all.txt"
tokenid="<ACCESS_TOKEN>"
while IFS=' ' read -r f1 f2
do
    printf 'Get threads from convo id:%s number:%s to file threads-%s.json\n' "$f2" "$f1" "$f1"
    ./hs-getthreads.py --token-id $tokenid --convo-id $f2 --outfile data/threads_json/threads-$f1.json
    # prevent exceeding HS API request limit
    sleep 0.2s
done <"$file"