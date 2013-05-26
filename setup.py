from setuptools import find_packages
from isc_ops.setup_tools import setup, current_version


setup(name='flavourdetect',
    packages=find_packages(),  
    description = 'Django app detects the user device and serves up the appropriate template.',
    url = 'http://github.com/infoscout/flavourdetect',
    version = current_version(),     
    install_requires=[
        'django==1.4',
    ]
)

