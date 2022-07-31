#More on setup.py here: https://github.com/kennethreitz/setup.py

'''
Option 1:
'''
from setuptools import find_packages
#The find_packages helper iterates over the filesystem and it will look for things
#have the __init__.py and add those to the package metadata automatically
from setuptools import setup
	
setup(
	name='python-project-structure',
	version='0.0.1',
	description='this package contains some sample hello world code',
	author='Gary Zavaleta',
	author_email='garyzava@umich.edu',
	url='google.com',
	packages=find_packages(exclude=('test*','testing*')),
	entry_points={
		'console_scripts': [
			'python-project-structure-cli = source.main:main',
		],
	},

)


'''
Option 2:
Maintaining dependencies in requirements.txt and make setup.py use it.
Used for Apps being deployed on machines you control.
To generate a requirements file: pip freeze > requirements.txt 

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

...

setup(
    name='package name',
    version='version',
    install_requires=requirements,
    ...
)

'''

'''
Option 3:
Publishing (Perfect) Python Packages splitting production and development dependencies
...

setup(
    name='package name',
    version='version',
	description='A description',
    py_modules=["helloworld"],
    package_dir={'':'source'},
)

To test the package:
$ python setup.py bdist_wheel 
To install it:
$ python setup.py -e .
Let's test it:
$ python
> from helloworld import say_hello
> say_hello()

Production Depedencies:
...
setup(
    install_requires = [
		"blessings ~= 1.7",
	],
    ...
)
$ pip install -e .

Development Dependencies: (eg: pytest)
...
setup(
    extras_require = {
		"dev":[
			"pytest>=3.7",
		],
	},
    ...
)
$ pip install -e .[dev]
'''