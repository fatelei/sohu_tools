#!/usr/bin/python
#-*-coding: utf8-*-

from setuptools import find_packages, setup


install_requires = ['requests', 'lxml', 'tornado']

entry_points = """
"""

setup(
    author="fatelei@gmail.com",
    version="0.1",
    name="sohunews",
    install_requires=install_requires,
    entry_points=entry_points,
    packages=find_packages("apps"),
    package_dir={"": "apps"}
)
