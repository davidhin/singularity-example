[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/5215)

# Research Project Example

This is an example project to show the setup of singlarity.

### Setup without container (requires gdown)

```
bash get_data.sh
pip install -r requirements.txt
pip install -e .
```

### Singularity Commands

Local build

```
sudo singularity build --sandbox main.img Singularity;

singularity run main.img -p main;
```

Deploy to Phoenix

```
sudo singularity build main.simg Singularity;
scp ./main.simg a1720858@phoenix-login1.adelaide.edu.au:/hpcfs/users/a1720858/singularity/singularity-example/main.simg
```

Install package locally. `-e` means editable, which is what we want.

```
pip install -e .
```

### Troubleshooting

#### Jupyter Notebook fix

```
jupyter notebook --generate-config -y
echo "c.NotebookApp.allow_remote_access = True" >> /root/.jupyter/jupyter_notebook_config.py

```
