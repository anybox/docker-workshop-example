#!/usr/bin/env bash

COUNTER_PATH=${COUNTER_PATH:-'/tmp/counter.txt'}

USAGE="Usage: $0 -d DEST [-h]
This tool backup the counter file (default: $COUNTER_PATH, you can overload
this setting setting COUNTER_PATH env variable) into the destination DEST file

Options:
    -d DEST     Give the destination file where to save the counter file.
    -h          Display this help
"

while getopts "d:h" OPTION
do
    case $OPTION in
        d) DEST="$OPTARG" ;;
        h) echo "$USAGE"; exit;;
        *) echo "File not found"; echo "$USAGE";exit 1;;
    esac
done

if [ -z "${DEST}" ]; then
    echo "-d option is required..."
    echo "$USAGE"
    exit 1
fi

echo "Copy '$COUNTER_PATH' to '$DEST'"

mkdir -p $(dirname "$DEST")
cp "$COUNTER_PATH" "$DEST"
