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

# demo_patrikspiess

Demo project to try the package deployment. It uses poetry, tox and Github actions. It is not meant
to do anything useful.

# Contents

- [Reference](#reference)
- [Pre Build](#pre-build)
  - [CHANGELOG.md](#changelogmd)
  - [Tests](#tests)
  - [Version Bump](#version-bumb)
  - [Git Tag](#git-tag)
- [Building the Package](#building-the-package)
- [Upload (publish) the Package](#upload-publish-the-package)
- [Package Installation](#package-installation)
  - [Upgrade](#upgrade)
- [CI/CD with Github Actions](#cicd-with-github-actions)
- [Documentation](#documentation)

# Reference

This project is a demo project from the **Packaging Python Projects** Tutorial which can be found at https://packaging.python.org/en/latest/tutorials/packaging-projects/#

Other than in the tutorial mentioned above I use poetry as a package manager. Therefore some of the configuration or commands differ from what you see in the tutorial.

Additionally I use some test and build features to try out some workflow/actions stuff.

# Pre Build

## CHANGELOG.md

For every change update the [CHANGELOG.md](CHANGELOG.md) to reflect the news. Users and contributors need to know about changes in the project. When bumping the version the [CHANGELOG.md](CHANGELOG.md) gets a new section with the new version and the [Unreleased] section is cleared for the next upcoming changes.
## Tests
Before I build, the tests run with tox should be successful:

    poetry run tox

## Version Bumb

Every released package should have its unique version number. Therefore a version bump has to be done with poetry:

    poetry version [major, minor, patch]

And also the \_\_version\_\_ = "x.x.x" in the \_\_init\_\_.py of the modules root folder should be changed to the same resulting number.
(Maybe someone can give me a useful Github action to automatically update the \_\_version\_\_ in \_\_init\_\_.py when the version in pyproject.toml has changed)

## Git Tag

Before committing all the changes for a release a Git tag with the corresponding version number has to be created. We always use annotated tags. E.g. if you wish to release version 9.8.7 you create tag with the following command:

    git tag -a v9.8.7 -m "version v9.8.7"

Later you may list all the tags:

    git tag --list

### Pushing Git Tags

After a git tag has been created it has to be pushed to the remote repository:

    git push origin <tag_name>

It's not best practice to use `git push --tags`.

# Building the Package

According to https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives I build the distribution packages but I use poetry.

    poetry build

This builds the package as described in the tutorial. The package is stored in the folder ./dist. This folder should be ignored in .gitignore

# Upload (publish) the Package

Instead of using twine I use poetry to upload (publish) the package to PyPI.

First the repository has to be registered:

    poetry config repositories.testpypi https://test.pypi.org/legacy/

Second I add my testpypi token to the Git configuration so I don't have to specify it on every
publish:

    poetry config pypi-token.testpypi <pypi_api_token>

If the token is not added to the Git config it has to be specified every time with `-u` (username,
which is always *\_\_token\_\_*) and `-p` (password which in this case is the token)

Then I can upload the package with the following command:

    poetry publish --repository testpypi

I use the test PyPI repository because it's best practice for tests like this.

If you use an API token for authentication use *\_\_token\_\_* as username and the token itself as password.

# Package Installation

After the package is uploaded to PyPI you can install it with the following command:

    pip install -i https://test.pypi.org/simple/ demo-patrikspiess

Option -i is only needed because the package has to be loaded from the test PyPI repository. For official PyPI packages the -i option may be omitted.

## Upgrade

If the package is already installed you may use the option -U to do an upgrade.

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
