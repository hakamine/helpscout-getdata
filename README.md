# helpscout-getdata

Scripts to get data from Help Scout via the [Mailbox API 2.0](https://developer.helpscout.com/mailbox-api/)

These scripts are unmaintained (used these to get our data out, and saved here in case it is useful for anybody)

## hs-getaccesstoken.py

Get access token to authenticate to Help Scout. Before using, from the
Help Scout web UI create an [Oauth2 application](https://developer.helpscout.com/mailbox-api/overview/authentication/) to obtain an App ID and Secret, then set
`HELPSCOUT_APP_ID` and `HELPSCOUT_APP_SECRET` environment variables with these values.

```
> ./hs-getaccesstoken.py
{"token_type":"bearer","access_token":"<ACCESS_TOKEN>","expires_in":7200}
```

## hs-getconversations.py

Get list of all Help Scout conversations and save json to a file.
```
./hs-getconversations.py --token-id <ACCESS_TOKEN>  --outfile data/convers_all.json
```

## hs-list-convo-number-id.py

From a conversations json file, get the conversation id and number pairs and
save to a file (used in other scripts)
```
./hs-list-convo-number-id.py --infile data/convos_json/convers_all.json  --outfile data/list_all.txt
```

## hs-getthreads.py (and getthreads_batch.sh)

Get the threads from a Help Scout conversation and save json to a file.
```
./hs-getthreads.py  --token-id <ACCESS_TOKEN> --convo-id <CONVO_ID>  --outfile data/thread.json
```

`getthreads_batch.sh` can be used to get the threads from all conversations, using the list created by `hs-list-convo-number-id.py` (will create a separate json file
for each conversation)

## hs-parse-from-json-threads.py (and parsethreads_batch.sh)

Parse a threads json file and create an html file from it

```
./hs-parse-from-json-threads.py --infile data/threads_json/threads-6810.json --outfile data/html/hs6810.html
```

`parsethreads_batch.sh` can be used to generate html files from all json threads
files created by `getthreads_batch.sh`

## hs-gen-index-from-json-convos.py

Generate an htnl index file from the conversation list json file, with links to the
html files with thread information (created by `parsethreads_batch.sh`)

```
./hs-gen-index-from-json-convos.py --infile data/convos_json/convers_all.json  --outfile data/html/index.html
```
