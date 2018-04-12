#!/usr/bin/env python

try:
    with open('package_description.rst', 'r') as file_description:
		description = file_description.read()
except IOError:
    description = "https://github.com/fieldcloud/iot-gtw-clouding-things"

from setuptools import setup, find_packages

import CloudingThings4Pi

setup(
    name = "CloudingThings4Pi",
    version = "0.4.0",

    description = "Python library used to easily develop an IoT gateway "\
                  "based on RaspBerry Pi and Dexter Grove Pi sensor board "\
                  "connected to Clouding Things use cases prototyping "\
                  "platform",
    long_description = description,

    author = "fieldcloud SAS",
    author_email = "contact@fieldcloud.com",

    license = 'MIT',
    classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url = "https://github.com/fieldcloud/iot-gtw-clouding-things",

    keywords = ['iot', 'grove', 'internet of things', 'prototyping',
                'clouding things', 'fieldcloud'],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires = ['grovepi', 'paho-mqtt', 'twisted']
)
