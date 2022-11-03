# Python Packing & Project Structure
This is an example project demostrating a common Directory structure for your Python projects and packaging it using setuptools.

## Virtual Environment
VENV comes out-of-the-box with Python, hence there is no need to install external libraries

For Linux
```
```

For Windows
```
```

## Setup.py

### Generating the packages
Packages are meant for reusability. A python distribution is a versioned file that contains Python pacakges. There are two primary distribution types in use today: i) Source Distributions (sdist) which only contains the source code; and ii) Wheel/Built Distributions (bdist) actually "builds" the package. It is best practice to upload both, wheels and a source distribution, because any built distribution format only works for a subset of target systems.

```python
$ python setup.py sdist bdist_wheel
```

### Setup.py Template
Download the setup.py file:
```
cd your_project

#  download with wget
wget https://raw.githubusercontent.com/garyzava/python-project-structure/main/setup_template.py -O setup.py

#  download with curl
curl -O setup.py https://raw.githubusercontent.com/garyzava/python-project-structure/main/setup_template.py
```
### Requirements.txt
Maintening dependencies in the requirements.txt file is widely used and often recommended for apps deployed on machines you control. The existing project has the requirements.txt and make the setup.py use of it. 

## Installation
Run the following to install:

```python
pip install hellworld
```
or run pip install, do not use install setup.py.
```python
pip install .
```

## Usage
```python
from helloworld import say_hello

#Generate "Hello, World!"
say_hello()

#Generate "Hello, Everybody!"
say_hello("Everybody")
```

## CLI

## Useful Resources:
Publish a (Perfect) Python Package on PyPI - Mark Smith: https://www.youtube.com/watch?v=eZef6bywIdo

Python Packaging: sdist vs bdist: https://dev.to/icncsx/python-packaging-sdist-vs-bdist-5ekb

setup.py for humans: https://github.com/navdeep-G/setup.py

