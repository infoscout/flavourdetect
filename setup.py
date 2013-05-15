from setuptools import setup, find_packages

setup(name='flavourdetect',
    packages=find_packages(),  
    description = 'Django app detects the user device and serves up the appropriate template.',
    url = 'http://github.com/infoscout/flavourdetect',
    version = '0.1dev',    
    install_requires=[
        'django>=1.4',
    ]
)

