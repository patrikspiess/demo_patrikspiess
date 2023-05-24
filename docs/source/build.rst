.. demo_patrikspiess building the package


.. contents:: Table of Contents
    :depth: 2


Building the Package
####################

Before you build
****************

CHANGELOG.md
============

For every change update the CHANGELOG.md in the project root directory to reflect the news.
Users and contributors need to know about changes in the project. When bumping the version
the CHANGELOG.md gets a new section with the new version and the `Unreleased` section is cleared
for the next upcoming changes.

Tests
=====

Before I build, the tests run with tox MUST be successful:

::

    poetry run tox

Version Bumb
============

Every released package should have its unique version number. Therefore a version bump has to be
done with poetry:

::

    poetry version [major, minor, patch]

And also the ``__version__ = "x.x.x"`` in the *__init__.py* of the modules code folder should be
changed to the same resulting number.
(Maybe someone can give me a useful GitHub action to automatically update the __version__ in 
*__init__.py* when the version in *pyproject.toml* has changed)

Git Tag
=======

Before committing all the changes for a release a Git tag with the corresponding version number has
to be created. I always use annotated tags. E.g. if you wish to release version 9.8.7 you create
a tag with the following command:

::

    git tag -a v9.8.7 -m "version v9.8.7"

Later you may list all the tags:

::

    git tag --list

Pushing Git Tags
================

After a Git tag has been created it has to be pushed to the remote repository:

::

    git push origin <tag_name>

It's not best practice to use ``git push --tags``.

Building the Package
********************

According to `<https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives>`_
I build the distribution packages but I use poetry.

::

    poetry build

This builds the package as described in the tutorial. The package is stored in the folder *./dist*.
This folder should be ignored in *.gitignore*.

Release the Package
*******************

Publish to PyPI
===============

Instead of using twine I use poetry to upload (publish) the package to PyPI.

First the repository has to be registered:

::

    poetry config repositories.testpypi https://test.pypi.org/legacy/

Second I add my testpypi token to the Git configuration so I don't have to specify it on every
publish:

::

    poetry config pypi-token.testpypi <pypi_api_token>

If the token is not added to the Git config it has to be specified every time with ``-u`` (username,
which is always ``__token__``) and ``-p`` (password which in this case is the token)

Then I can upload the package with the following command:

::

    poetry publish --repository testpypi

I use the test PyPI repository because it's best practice for tests like this.

If you use an API token for authentication use ``__token__`` as username and the token itself as 
password.

After successful publishing to PyPI the project can be found here
`<https://test.pypi.org/project/demo-patrikspiess/>`_


Make a Release on GitHub
========================

At the end do not forget to make a new release on GitHub.