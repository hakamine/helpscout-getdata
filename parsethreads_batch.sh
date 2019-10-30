#!/bin/bash

file="data/list_all.txt"
while IFS=' ' read -r f1 f2
do
    printf 'Generating hs%s.html from threads-%s.json\n' "$f1" "$f1"
    ./hs-parse-from-json-threads.py --infile data/threads_json/threads-$f1.json --outfile data/html/hs$f1.html
done <"$file"