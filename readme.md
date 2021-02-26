[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/5215)

# Research Project Example

This is an example project to show the setup of singlarity.

To build image locally, run:
`sudo singularity build main.simg Singularity`

### Jupyter Notebook fix

```
jupyter notebook --generate-config -y
echo "c.NotebookApp.allow_remote_access = True" >> /root/.jupyter/jupyter_notebook_config.py
```
