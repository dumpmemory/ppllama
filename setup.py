# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the GNU General Public License version 3.
import setuptools
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ppllama',
    version='0.0.0',
    packages=setuptools.find_packages(
        where=".",
        exclude=("examples*", "scripts*"),
    ),
    project_urls={
        "Gitter": "https://github.com/MiuGod0126/ppllama",
    },

    install_requires=[
        "paddlepaddle-gpu",
        "fire",
        "fire",
    ],
)