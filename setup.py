#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    grim Graph Imputation
#    Copyright (c) 2021 Be The Match operated by National Marrow Donor Program. All Rights Reserved.
#
#    This library is free software; you can redistribute it and/or modify it
#    under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 3 of the License, or (at
#    your option) any later version.
#
#    This library is distributed in the hope that it will be useful, but WITHOUT
#    ANY WARRANTY; with out even the implied warranty of MERCHANTABILITY or
#    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
#    License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this library;  if not, write to the Free Software Foundation,
#    Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.
#
#    > http://www.fsf.org/licensing/licenses/lgpl.html
#    > http://www.opensource.org/licenses/lgpl-license.php
#


"""The setup script."""

from setuptools import setup
from Cython.Build import cythonize

# import numpy


# include_dirs=[numpy.get_include()],
# requires=['numpy', 'Cython'])


from setuptools import setup, find_packages, Extension

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().split("\n")

with open("requirements-tests.txt") as requirements_file:
    test_requirements = requirements_file.read().split("\n")

setup(
    name="py-graph-imputation",
    version="0.1.1",
    author="Pradeep Bashyal",
    author_email="pbashyal@nmdp.org",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Graph Based Imputation",
    install_requires=requirements,
    license="LGPL 3.0",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="grim",
    scripts=["scripts/build-imputation-validation.sh", "scripts/runfile.py"],
    packages=find_packages(
        include=[
            "grim",
            "grim.imputation",
            "graph_generation",
            "graph_generation.output",
            "data",
            "data.subjects",
            "conf",
        ]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/nmdp-bioinformatics/py-grim",
    zip_safe=False,
    ext_modules=cythonize(
        [
            Extension(
                "grim.imputation.cutils",
                ["grim/imputation/cutils.pyx"],
            )
        ],
        language_level="3",
    ),
)
