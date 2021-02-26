#!/bin/bash

echo "Welcome to the CLI!"
usage() { echo "Usage: $0 \
[-h help] \
[-p run program <main>] \
[-a arguments] \
[-n run jupyter notebook]" 1>&2; exit 1; }

port=$(shuf -i8000-9999 -n1)
node=$(hostname -s)

while getopts ":hp:a:n" opt; do
    case ${opt} in
        h)
            usage
        ;;
        p)
            p=${OPTARG} 
        ;;
        a)
            a+=("${OPTARG}")
        ;;
        n)
            jupyter notebook --port=${port} --ip=${node}
        ;;
        \?)
            echo "Invalid option"
            usage
        ;;
    esac
done
shift $((OPTIND-1))

if [[ "main" == "${p}" ]]; then
    python3 -u /src/main.py "${a[@]}"
    exit 0
fi

usage