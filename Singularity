Bootstrap:docker
From:python:3.6

%labels
    MAINTAINER admin
    WHATAMI admin

%files
    cli.sh /cli.sh
    get_data.sh /get_data.sh
    requirements.txt /requirements.txt
    src /src

%runscript
    exec /bin/bash /cli.sh "$@"

%post
    chmod u+x /cli.sh

    # Install dependencies here
    echo "Installing python dependencies..."
    pip install -r /requirements.txt

    # Download files
    bash /get_data.sh
