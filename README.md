# Python Packaging & CLI
This is an example project demostrating a common Directory structure for your Python projects and packaging it using setuptools.

## Overview

* [Virtual Environment](#virtual-environment)
* [Setup.py for humans](#setuppy-for-humans)
* [Installation](#installation)
* [Usage](#usage)
* [CLI](#cli)
* [Useful Resources](#useful-resources)

## Virtual Environment
VENV comes out-of-the-box with Python, hence there is no need to install external libraries

For Linux
```
$ python -m venv venv
$ source venv/bin/activate
(venv) $
```

For Windows
```
PS> python -m venv venv
PS> venv\Scripts\activate
(venv) PS>

(venv) PS> deactivate
```

## Setup.py For Humans
Packages are meant for reusability. A python distribution is a versioned file that contains Python pacakges. There are two primary distribution types in use today: i) Source Distributions (sdist) which only contains the source code; and ii) Wheel/Built Distributions (bdist) actually "builds" the package. It is best practice to upload both, wheels and a source distribution, because any built distribution format only works for a subset of target systems.

### Setup.py Template
Download and customize the setup.py file:
```
cd your_project

#  download with wget
wget https://raw.githubusercontent.com/garyzava/python-project-structure/main/setup_template.py -O setup.py

#  download with curl
curl -O setup.py https://raw.githubusercontent.com/garyzava/python-project-structure/main/setup_template.py
```

### Generating the packages
```python
$ pip install wheel
$ python setup.py sdist bdist_wheel
```

### Requirements.txt
Maintening dependencies in the requirements.txt file is widely used and often recommended for apps deployed on machines you control. The existing project has the requirements.txt and make the setup.py use of it. 

Run the following to generate the requirements file:
```python
$ pip freeze > requirements.txt
```

## Installation
Run pip install to install the project, do not use install setup.py.
```python
pip install .
```

## Usage
From a python script
```python
from helloworld import say_hello

#Generate "Hello, World!"
say_hello()

#Generate "Hello, Everybody!"
say_hello("Everybody")
```
From the python command
```
(venv) $ python
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
>>> main.say_hello()
'Hola Mundo!'
>>> main.main()
'Hello, World!'
>>> main.main("a")
'Hello, a!'
>>> exit()
```

## CLI
```
(venv) $ hello-world-dist-cli
Hola Mundo!
```

## Useful Resources:
Publish a (Perfect) Python Package on PyPI - Mark Smith: https://www.youtube.com/watch?v=eZef6bywIdo

Python Packaging: sdist vs bdist: https://dev.to/icncsx/python-packaging-sdist-vs-bdist-5ekb

setup.py for humans: https://github.com/navdeep-G/setup.py

