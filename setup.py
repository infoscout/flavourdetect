import os
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
    description='Django app detects the user device and serves up the appropriate template.',
    url='http://github.com/infoscout/flavourdetect',
    version=version,
    install_requires=[
        'django>=1.4',
    ],
    cmdclass={'test': TestCommand}
)
