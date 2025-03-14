# Changelog <span style="font-size:small">[[main](README.md)]</span>
 
All notable changes to this project will be documented in this file.
For examples and guidelines see [https://keepachangelog.com/](https://keepachangelog.com/)


# [Unreleased]

For unreleased changes see [WHATSNEW.md](WHATSNEW.md)

# [Released]

## [1.0.1] - 2024-12-24

### Added

### Changed

- Update some dependencies
- Update some documentation

### Removed

- Removed the uppper bound for external packets according to [Henry Schreiner](https://iscinumpy.dev/post/bound-version-constraints/)

## [0.5.4] - 2024-06-20

### Added

### Changed

### Removed

## [demo_patrikspiess 0.5.3] - 2024-06-20

### Added

### Changed

- Change the readthedocs process to use Poetry
- Upgrade black due to dependabot warning
- Upgrade idna due to dependabot warning
- Upgrade jinja2 due to dependabot warning
- Upgrade urllib3 due to dependabot warning

### Removed

## [0.5.2] - 2024-01-27

### Added

### Changed

- Fix version handling in .make_release

### Removed

## [0.5.1] - 2024-01-27

### Added

### Changed

### Removed

## [0.5.0] - 2024-01-27

### Added

- A fanpage to make first pull requests
- Decorator demo

### Changed

### Removed

- Support for Python 3.8 and Python 3.9

## [0.4.5] - 2023-10-22

### Changed

- Update packages and dependencies (due to urllib3 vulnerability)

## [0.4.4] - 2023-08-04

### Changed

- Fix the logo link in README.md so it also shows on pypi

## [0.4.3] - 2023-08-04

### Added

- Add a logo to README.my to test presence on pypi

## [0.4.2] - 2023-08-03

### Changed

- Use WHATSNEW.md as release file instead of full CHANGELOG.md


## [0.3.0] - 2023.05.24

### Added

- Add support for Python 3.11

### Changed

- Update requests to 2.31.0 because of Dependabot security warning


## [0.2.12] - 2023.03.02

### Added

- Script .make_release.py to automatically build, publish and release the project

### Comment

There are some intermediate release not mentioned here. These were used to test the automatic
release of the project.

## [0.2.3] - 2023.02.07

### Changed

- Solve a tox dependency issue (by upgrading tox)
- Add dev dependencies to readthedocs requirements file
- Remove poetry cache from .gitignore


## [0.2.2] - 2023.02.06

### Changed

- Update some documentation on how to publish
- Update README with link to the readthedocs.io documentation


## [0.2.1] - 2023.02.06

### Added

- Introduce logging capabilities
- Introduce a first version of the config module
- Introduce black format checking
- Introduce automatic documentation with sphinx and autodoc (for readthedocs.io)
- Introduce type checking with mypy

### Changed

- Change the tox dependency handling (to not specify deps again in tox config)
- Change the sphinx theme to the beautiful sphinx_rtd_theme
- Cleanup unused files from past experiments


## [0.1.4] - 2022.10.02

### Added

- help screen if no parameter is given
- DemoException
- Parameter with sys.argv to execute some examples (maybe in future typer is used)
- .pylintrc to control pylint

### Changed

- Update README.md (add a 'Contents' and a 'Git Tag' section and fix lots of typos)


## [0.1.3] - 2022.10.02

### Added

- Add Github actions

## [0.1.2] - 2022.10.01

### Changed

- Forgot to reflect the changes in the CHANGELOG.md 😧


## [0.1.1] - 2022.10.01

### Added
- README.md
- CHANGELOG.md
- CONTRIBUTION.md
- LICENSE
- pyproject.toml
- src/demo_patrikspiess/calc.py
- src/demo_patrikspiess/write.py

### Changed

- .gitignore


## [0.1.0] - 2022.10.01

### Added
- Initial release

