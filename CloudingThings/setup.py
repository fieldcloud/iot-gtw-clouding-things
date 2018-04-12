#!/usr/bin/python #!/usr/bin/env python

try:
    with open('package_description.rst', 'r') as file_description:
		description = file_description.read()
except IOError:
    description = "https://github.com/fieldcloud/iot-gtw-clouding-things"

from setuptools import setup, find_packages

setup(
    name = "CloudingThings4Pi",
    version = "0.1.1",

    description = "Python library used to easily a Raspberry Pi "\
                  "into an IoT gateway "\
                  "combining grove sensors & Clouding things use case "\
                  "prototyping platform",
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
