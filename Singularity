Bootstrap:docker
From:pytorch/pytorch:1.8.0-cuda11.1-cudnn8-runtime

%labels
    MAINTAINER admin
    WHATAMI admin

%files
    cli.sh /cli.sh
    requirements.txt /requirements.txt

%runscript
    exec /bin/bash /cli.sh "$@"

%post
    chmod u+x /cli.sh

    # Install dependencies here
    add-apt-repository ppa:deadsnakes/ppa
    apt update
    apt install -y build-essential python3.8
    pip install -r /requirements.txt
