# tfchain-py

[![Build Status](https://travis-ci.com/GlenDC/tfchain-py.svg?branch=master)](https://travis-ci.com/GlenDC/tfchain-py)
[![Docs](https://img.shields.io/badge/Docs-master-green.svg)](GlenDC.github.io/ttfchain-py/api/tfchain/)

A TFChain client implementation in python.

This client has been ported from a [JumpScaleX Client](http://github.com/threefoldtech/jumpscaleX),
as to be able to use it in environments that require a Python3 client decoupled from any opinionated framework.

NOTE that this library and its API is not finished. Changes can be expected until we reach `v1.0.0`.

Documentation available [API reference](GlenDC.github.io/ttfchain-py/api/tfchain/)


## installation

`pip install tfchain` 


## Developer installation

```bash

git clone https://travis-ci.com/GlenDC/tfchain-py
cd tfchain-py

pipenv shell

```


## Generating documentation

use `make gendocs` to generate documentation

## Publishing flow

- Make sure credentials in ~/.pypirc

```
[distutils]
index-servers =
    pypi

[pypi]
username: PYPI_USERNAME
password: PYPI_PASSWORD
```
use `upload` task in Makefile `make upload`
