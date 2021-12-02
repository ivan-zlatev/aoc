#!/bin/sh
set -e

year=2021
day=${1:?gimme a day}

output_path="$(printf '%04d/%02d/input.txt' $year $day)"
mkdir -p "$(printf '%04d/%02d' $year $day)"
cookie='session=53616c7465645f5fcac75acc9be4a4bfe0d4f620069d7ab200d68192ab5881dc4fa12a9f1b6de17cfebad7c50e04e45f'  # set this from the login session

[ -f "$output_path" ] && {
    echo already loaded
    exit
} >&2

curl --fail -sS -b "$cookie" "https://adventofcode.com/$year/day/$day/input" -o "$output_path"
cp template.py "$(printf '%04d/%02d/%02.py' $year $day $day)"
