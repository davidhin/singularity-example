[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/5215)

# Research Project Example

This is an example project to show the setup of python and singularity-based experimental research. The aim is to provide a generalised research-oriented framework/workflow that supports reproducible science.
The basic idea is to decouple:

- Development environment (Singularity)
- Experimental code (Python module)
- Path references (based on [this](https://stackoverflow.com/a/50194143/1889006))
- Data storage (storage folder)
- Generated outputs (output folder)
- HPC scripting (hpc folder)

## Quickstart

Production build (for deploying to system through SHUB)

```
git clone https://github.com/davidhin/singularity-example.git
cd singularity-example
singularity pull --name main.simg shub://davidhin/singularity-example:latest
singularity run main.simg -p initialise
```

Then, if on Phoenix, run:

```
sbatch hpc/run_notebook.sh
```

## Development

#### Setup without container (requires gdown)

`-e` means editable, which is what we want when installing the package locally for development purposes.

```
bash get_data.sh
pip install -r requirements.txt
pip install -e .
```

#### Singularity Commands

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

#### Troubleshooting

##### Jupyter Notebook fix

```
jupyter notebook --generate-config -y
echo "c.NotebookApp.allow_remote_access = True" >> /root/.jupyter/jupyter_notebook_config.py

```
