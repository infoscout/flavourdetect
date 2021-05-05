# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import Command, find_packages, setup

with open('VERSION', 'r') as f:
    version = f.read().strip()


class TestCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import django
        from django.conf import settings
        from django.core.management import call_command

        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3',
                },
            },
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'flavourdetect',
            )
        )
        django.setup()
        call_command('test', 'flavourdetect')


setup(
    name='flavourdetect',
    packages=find_packages(),
    description=(
        'Django app detects the user device and serves up the '
        'appropriate template.'
    ),
    url='http://github.com/infoscout/flavourdetect',
    version=version,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
        'Topic :: Utilities',
    ],
    install_requires=[
        'Django >= 1.8, < 3.1a0'
    ],
    cmdclass={'test': TestCommand}
)
