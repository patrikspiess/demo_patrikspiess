# demo_patrikspiess

Demo project to try the package deployment

# Reference

This project is a demo project from the **Packaging Python Projects** Tutorial which can be found at https://packaging.python.org/en/latest/tutorials/packaging-projects/#

Other than in the above tutorial I use poetry as a package manager. Therefore some of the confgiuration or commands differ from what you see in the tutorial.

# build

According to https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives I build the distribution packages but I use poetry.

    poetry build

This builds the packges as described in the tutorial. The packages are stored in the folder ./dist. This folder should be ignored in .gitignore

# package upload

Instead of using twine I use poetry to upload (publish) the package to PyPI.

First the repository has to be registered:

    poetry config repositories.testpypi https://test.pypi.org/legacy/

Then I can upload the package with the following command:

    poetry publish --repository testpypi

I use the test PyPI repository because it's best practice for tests like this.

If you use an API token for authentication use *__token__* as username and the token as password.

# package installation

After the package is uploaded to PyPI you can install it with the following command:

    pip install -i https://test.pypi.org/simple/ demo-patrikspiess

Option -i is only needed because the packeg has to be loaded from the test PyPI repository. For official PyPI packages the -i option may be omited.

## Upgrade

If the package is already installed you may use the option -U to do an upgrade.

# CI/CD

I use tox with Github actions. Tox ist configured in the pyproject.toml file as legacy_tox_ini. See https://tox.wiki/en/latest/example/basic.html.

For using Github actions you define your configuration in ./.github/workflows/*.yaml. Example for pylint is given there. In the Github actions I use the preparfed tox environments. So I may the same tests localy.
