#!/bin/bash
set -e

year=`date | cut -d' ' -f 4`
if [ -z "$1" ]; then
    day=`date | cut -d' ' -f 2`
else
    day=$1
fi

output_path="$(printf '%04d/%02d' $year $(( 10#$day )))"
mkdir -p "$output_path"
cookie=`cat SESSIONID`  # set this from the login session

if [ ! -f "$output_path/test.txt" ]; then
    aoc-to-markdown -y $year -d $day > "$output_path/test.txt"
fi
[ -f "$output_path/input.txt" ] && {
    echo already loaded
    exit
} >&2

curl --fail -sS -b "$cookie" "https://adventofcode.com/$year/day/$day/input" -o "$output_path/input.txt"
cp template.py "$(printf '%04d/%02d/%02d.py' $year $day $day)"
cd 2021
