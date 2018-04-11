from setuptools import setup, find_packages

setup(
    name = 'WrapIt',
    version = '0.1.0',
    description = 'A simple HTTP POST API wrapper for Python classes',
    author = 'George A. Mihaila',
    author_email = 'george.mihaila@gmail.com',
    url = 'https://github.com/gamihaila/WrapIt',
    download_url = 'https://github.com/gamihaila/WrapIt/archive/0.1.0.tar.gz',
    packages=['wrapit'],
    install_requires=[
        "Flask"
    ]
)
