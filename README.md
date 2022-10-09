# demo_patrikspiess

Demo project to try the package deployment. It uses poetry, tox and Github actions. It is not meant to do anything useful.

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

# Building the Package

According to https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives I build the distribution packages but I use poetry.

    poetry build

This builds the package as described in the tutorial. The package is stored in the folder ./dist. This folder should be ignored in .gitignore

# Upload (publish) the Package

Instead of using twine I use poetry to upload (publish) the package to PyPI.

First the repository has to be registered:

    poetry config repositories.testpypi https://test.pypi.org/legacy/

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
