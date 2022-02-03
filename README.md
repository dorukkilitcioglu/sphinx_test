[![ci](https://github.com/dorukkilitcioglu/sphinx_test/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/dorukkilitcioglu/sphinx_test/actions/workflows/test.yml)
[![PyPI version fury.io](https://badge.fury.io/py/gha-aut-test.svg)](https://pypi.python.org/pypi/gha-aut-test/)
[![PyPI license](https://img.shields.io/pypi/l/gha-aut-test.svg)](https://pypi.python.org/pypi/gha-aut-test/)

# Testing Sphinx on GH pages

## Things to automate
- [x] Unit tests on python versions
- [x] Update docs on release
- [x] Upload to (Test)PyPI on release
- [x] Docs version check with library version
- [ ] Coverage badge
- [ ] Check docs can be built within a PR
- [ ] Schedule periodical testing

## Steps
- Upload project to PyPI (the instructions below are for Test PyPI)
  ```bash
  pip install setuptools wheel twine
  python setup.py sdist bdist_wheel
  twine upload --repository testpypi dist/*
  ```
- Create an API key in PyPI, making sure to only give upload access to your repo.
- Go to project settings in GitHub, add a new secret called `TEST_PYPI_API_TOKEN`
- Add sphinx requirements to `docs/requirements.txt`
- Add documentation source under `docs`.
