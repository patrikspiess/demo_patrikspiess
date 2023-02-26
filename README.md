![Author](https://img.shields.io/badge/author-patrikspiess-blue?style=plastic)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/patrikspiess/demo_patrikspiess/tests.yaml?style=plastic)
![GitHub](https://img.shields.io/github/license/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub open issues](https://img.shields.io/github/issues-raw/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub Repo stars](https://img.shields.io/github/stars/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub watchers](https://img.shields.io/github/watchers/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub forks](https://img.shields.io/github/forks/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/patrikspiess/demo_patrikspiess?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/patrikspiess/demo_patrikspiess/total?style=plastic)

These badges are all generated with [shields.io](https://shields.io/).

***

# Official Documentation

For the official documentation of this project please got to
[demo-patrikspiess.readthedocs.io](https://demo-patrikspiess.readthedocs.io/)


# Contents

- [Reference](#reference)
- [Package Installation](#package-installation)
  - [Upgrade](#upgrade)
- [CI/CD with Github Actions](#cicd-with-github-actions)
- [Documentation](#documentation)

# Reference

This project is a demo project from the **Packaging Python Projects** Tutorial which can be found at
https://packaging.python.org/en/latest/tutorials/packaging-projects/#

Other than in the tutorial mentioned above I use poetry as a package manager. Therefore some of the
configuration or commands differ from what you see in the tutorial.

Additionally I use some test and build features to try out some workflow/actions stuff.

# License

MIT License

Copyright (c) 2023 Patrik Spiess

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


***

# CI/CD with Github Actions

I use tox with Github actions. Tox ist configured in the pyproject.toml file as legacy_tox_ini. See https://tox.wiki/en/latest/example/basic.html.

For using Github actions you define your configuration in ./.github/workflows/*.yaml. Example for pylint is given there. In the Github actions I use the prepared tox environments. So I may execute the same tests locally.

# Documentation

For documentation I use sphinx and autodoc. The generated docs are published to readthedocs.com.

The directory used for the documentation is docs in the project root. So create this directory and initialize sphinx from there.

Installing and setup sphinx

    poetry add --group dev sphinx
    poetry add --group dev sphinx-rtd-theme
    mkdir docs
    cd docs
    poetry run sphinx-quickstart
        > Separate source and build directories (y/n) [n]: y
        > Project name: demops
        > Author name(s): Patrik Spiess
        > Project release []:
        > Project language [en]:

Building the documentation from the projects root folder (one level above docs) is then possible with:

    poetry run sphinx-build -b html docs/source docs/build

I do not use the option to build the documentation with `poetry run make html` as I prefer to do everything with poetry. therefore I added a tox env for creating the documentation:

    poetry run tox -e docs

## readthedocs Configuration

This projects documentation has been published on readthedocs.io. The path to the docs is:

[demo-patrikspiess.readthedocs.io](https://demo-patrikspiess.readthedocs.io/)

For readthedocs being able to create the docs from the github repository I added a .readthedocs.yaml
in the root of the project. The important statements are the python version and the requirements
file.

Although the package dependencies are managed by poetry, readthedocs needs a classic
requirements.txt file. Therefore a tox env was created to generate the requirements.txt into the
source directory.

    poetry export --without-hashes --format=requirements.txt --output=source/requirements.txt

run it with

    poetry run tox -e requirements
