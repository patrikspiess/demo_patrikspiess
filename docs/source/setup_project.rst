.. demo_patrikspiess set up the project


.. contents:: Table of Contents
    :depth: 2


Setup the Project
#################


The Demo Environment
********************

First let's give a short description on my demo environment. You may use any other environment but I
cannot guarantee that other environments behave the same. For this project I use the following:

- Windows 11 running WLS2
- Ubuntu 24.04 in WLS2

So, all I do is done in Ubuntu even if my machine is Windows. Therefore the project should also run in native Linux machines.

Additionally in Ubuntu I use the following:

- Python 3.13

To install Python 3.13 and use the command ``python`` to start my Python 3.13 interpreter I use the following commands:

::

    sudo apt install python3.13
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.13 1
    sudo apt install python-is-python3

After that you may run ``python`` and should get the following prompt:

::

    $ python
    Python 3.13.0 (main, Oct  8 2024, 08:51:27) [GCC 13.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit

- poetry

As I do my projects dependency and package management with poetry I have to install Poetry with the
following command according to
`Installation <https://python-poetry.org/docs/#installing-with-pipx>`_.

::

    pipx install poetry
    pipx ensurepath
    poetry completions bash >> ~/.bash_completion

After that you may check your poetry version with:

::

    $ poetry --version
    Poetry (version 1.8.5)


Initializing the Project
************************

To start a new project change to the desired directory where you want to create your project and
initialize it with ``poetry new``:

::

    $ poetry new demo_patrikspiess
    Created package demo_patrikspiess in demo_patrikspiess

Change to the new directory:

::

    cd demo_patrikspiess

Within it you'll find two directories and two files:

- demo_patrikspiess (directory)
- tests (directory)
- README.md
- pyproject.toml

The file *README.md* is empty but the file *pyproject.toml* has some initial configuration for the
project:

::

    [tool.poetry]
    name = "demo-patrikspiess"
    version = "0.1.0"
    description = ""
    authors = ["Patrik Spiess <patrik.spiess@bluewin.ch>"]
    readme = "README.md"
    packages = [{include = "demo_patrikspiess"}]

    [tool.poetry.dependencies]
    python = ">=3.10, <4"


    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

You do not have to change anything here (yet).