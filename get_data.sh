#!/bin/bash
# Get Google Drive files here
# To view drive file, go to the link:
# https://drive.google.com/file/d/<file_id>

if [[ -d storage ]]; then
    echo "storage exists, starting download"
else
    mkdir storage
fi

cd storage

if [[ ! -f "iris.csv" ]]; then
    gdown https://drive.google.com/uc\?id\=1T5T_it0sAWikw9qAkYRrIRAHejU7GDmC
else
    echo "Already downloaded iris.csv"
fi

if [[ ! -f "ast_ss.parquet" ]]; then
    gdown https://drive.google.com/uc\?id\=1lkA0BRlSD9XGTaGSx6yIHFWbbD60Fdxo
else
    echo "Already downloaded ast_ss.parquet"
fi

cd ..