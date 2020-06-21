#!/bin/sh
user="matteosalvinimi"
tweets="./tweets/salvini.txt"
tmptweets=$(mktemp)
tmp=$(mktemp)

date=$(sed 1q "$tweets" | cut -d" " -f 2,3)
twint -u "$user" --since "$date" -o "$tmptweets"

cat "$tmptweets" "$tweets" > "$tmp"
mv "$tmp" "$tweets"
