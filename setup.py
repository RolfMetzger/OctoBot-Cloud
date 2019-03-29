#  Drakkar-Software OctoBot-Cloud
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import os

from octobot_cloud import PROJECT_NAME, VERSION
from setuptools import setup, find_packages


def find_package_data(path):
    return (path, [os.path.join(dirpath, filename)
                   for dirpath, dirnames, filenames in os.walk(path)
                   for filename in
                   [file for file in filenames if not file.endswith(".py") and not file.endswith(".pyc")]])


PACKAGES = find_packages(exclude=["docs.*", "tests.*", "logs"])
PACKAGES_DATA = [('requirements.txt', ['requirements.txt'])]

# long description from README file
with open('README.md', encoding='utf-8') as f:
    DESCRIPTION = f.read()

REQUIRED = open('requirements.txt').read()
REQUIRES_PYTHON = '>=3.7.2'

setup(
    name=PROJECT_NAME,
    version=VERSION,
    url='https://github.com/Drakkar-Software/OctoBot-Cloud',
    license='LGPL-3.0',
    author='Drakkar-Software',
    author_email='drakkar.software@protonmail.com',
    description='OctoBot cloud runner',
    py_modules=['main'],
    packages=PACKAGES,
    long_description=DESCRIPTION,
    install_requires=REQUIRED,
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    python_requires=REQUIRES_PYTHON,
    data_files=PACKAGES_DATA,
    entry_points={
        'console_scripts': [
            PROJECT_NAME + ' = main:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
    ],
)
