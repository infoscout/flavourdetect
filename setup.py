from setuptools import find_packages, setup

with open('VERSION','r') as f:
    version = f.read().strip()

setup(name='flavourdetect',
    packages=find_packages(),  
    description = 'Django app detects the user device and serves up the appropriate template.',
    url = 'http://github.com/infoscout/flavourdetect',
    version = version,     
    install_requires=[
        'django>=1.4',
    ]
)

