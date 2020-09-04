# Milky Way Satellite Selection Function

This repository contains products associated with the observational selection function derived in the context of the Milky Way Satellite Census ([Drlica-Wagner & Bechtol et al. 2019](https://arxiv.org/abs/1912.03302); [Nadler et al. 2019](https://arxiv.org/abs/1912.03303); [Nadler, Drlica-Wagner et al. 2020](https://arxiv.org/abs/2008.00022)). We provide some simple examples in a Jupyter notebook: [ExampleNotebook.ipynb](ExampleNotebook.ipynb). You can view the contents of this notebook on your web browser, or install and run on your local machine following the instructions below.

## Data Products

The selection function model and associated data products can be accessed from the [Releases](../../releases) page of this repository (under the "Assets" of a release). The most recent version of these data products can be found here:

* [mw-sats-data.tar.gz (6.4MB)](https://github.com/des-science/mw-sats/releases/download/v0.2/mw-sats-data.tar.gz)

## Installation

We also provide a simple usage example. To get started, clone this GitHub repository and change into the newly created directory:

```
> git clone https://github.com/des-science/mw-sats.git
> cd mw-sats
```

The easiest way to install the necessary packages and dependencies is with `conda`. We have provided a conda environment file, which should specify the necessary packages and versions. This environment is designed for use with Python 3.

```
> conda env create -v -f conda-env.yaml
```

Once the environment has been installed, you can activate it and start this notebook server on your local machine.

```
> conda activate mw-sats
> jupyter notebook ExampleNotebook.ipynb
```

Running the notebook will download the observational selection function model and associated data products.
