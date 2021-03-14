#!/bin/bash
# Get Google Drive files here
# To view drive file, go to the link:
# https://drive.google.com/file/d/<file_id>

if [[ -d storage/external ]]; then
    echo "storage exists, starting download"
else
    mkdir --parents storage/external
fi

cd storage/external

if [[ ! -f "iris.csv" ]]; then
    gdown https://drive.google.com/uc\?id\=1T5T_it0sAWikw9qAkYRrIRAHejU7GDmC
else
    echo "Already downloaded iris.csv"
fi

if [[ ! -f "news.csv.zip" ]]; then
    gdown https://drive.google.com/uc\?id\=1bvup5OAYvptsBx8AIvhGGZIjVGZxHAXj
    unzip news.csv.zip
else
    echo "Already downloaded news.csv.zip"
fi

cd ..