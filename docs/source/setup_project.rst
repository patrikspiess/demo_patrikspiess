.. demo_patrikspiess set up the project


.. contents:: Table of Contents
    :depth: 2


Setup the Project
#################


The Demo Environment
********************

First let's give a shor description on my demo environment. You may use any other environment but I
cannot guarantee that other environments behave the same. For this project I use the following:

- Windows 11 running WLS2
- Ubuntu 22.04 in WLS2

So, all I do is done in Ubuntu 22.04 even if my machine is Windows 11. Therefore the project should
also run in native Linux machines.

Additionally in Ubuntu 22.04 I use the following:

- Python 3.11

To install Python 3.11 and use the command ``python`` to start my Python 3.11 interpreter I use the
following commands:

::

    sudo apt install python3.11
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
    sudo apt install python-is-python3

After that you may run ``python`` and should get the following prompt:

::

    $ python
    Python 3.11.0rc1 (main, Aug 12 2022, 10:02:14) [GCC 11.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()

- poetry

As I do my projects dependency and package management with poetry I have to install Poetry with the
following command according to
`Installation <https://python-poetry.org/docs/#installing-with-the-official-installer>`_.

::

    curl -sSL https://install.python-poetry.org | python3 -

After that you may check your poetry version with:

::

    $ poetry --version
    Poetry (version 1.2.2)


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
    python = "^3.10"


    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

You do not have to change anything here (yet).