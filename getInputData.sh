#!/bin/bash
set -e

year=`date '+%G'`
if [ -z "$1" ]; then
    day=`date '+%d'`
else
    day=$1
fi

output_path="$(printf '%04d/%02d' $year $(( 10#$day )))"
mkdir -p "$output_path"
cookie=`cat SESSIONID`  # set this from the login session; contents should be 'cookie=1234566122....' where 1234566122.... is the session id

if [ ! -f "$output_path/test.txt" ]; then
    aoc-to-markdown -y $year -d $day > "$output_path/test.txt"
fi
echo "https://adventofcode.com/$year/day/$day"
if [ -f "$output_path/input.txt" ]; then
    echo "$output_path/input.txt already exists"
else
    curl --fail -sS -b "$cookie" "https://adventofcode.com/$year/day/$day/input" -o "$output_path/input.txt"
fi

if [ -f "$(printf '%04d/%02d/%02d.py' $year $day $day)" ]; then
    echo "$(printf '%04d/%02d/%02d.py' $year $day $day) already exists"
else
    cp template.py "$(printf '%04d/%02d/%02d.py' $year $day $day)"
fi
echo "cd "`pwd`"/$output_path"
cd `pwd`"/$output_path"
