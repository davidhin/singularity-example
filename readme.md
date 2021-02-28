[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/5215)

# Research Project Example

This is an example project to show the setup of singlarity.

### Setup without container (requires gdown)

`-e` means editable, which is what we want when installing the package locally for development purposes.

```
bash get_data.sh
pip install -r requirements.txt
pip install -e .
```

### Singularity Commands

Local build for development

```
sudo singularity build --sandbox main.img Singularity;
singularity run main.img -p main;
```

Production build (for deploying to phoenix through SCP)

```
sudo singularity build main.simg Singularity;
scp ./main.simg aXXXXXXX@phoenix-login1.adelaide.edu.au:/hpcfs/users/aXXXXXXX/main.simg
```

Production build (for deploying to phoenix through SHUB)

```
singularity pull shub://davidhin/singularity-example:latest
```

### Troubleshooting

#### Jupyter Notebook fix

```
jupyter notebook --generate-config -y
echo "c.NotebookApp.allow_remote_access = True" >> /root/.jupyter/jupyter_notebook_config.py

```
