[![ci](https://github.com/dorukkilitcioglu/sphinx_test/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/dorukkilitcioglu/sphinx_test/actions/workflows/test.yml)

# Testing Sphinx on GH pages

## Things to automate
- [x] Unit tests on python versions
- [ ] Update docs on release
- [ ] Upload to (Test)PyPI on release
- [ ] Docs version check with library version
- [ ] Coverage badge

## Steps
- Upload project to PyPI (the instructions below are for Test PyPI)
  ```bash
  pip install setuptools wheel twine
  python setup.py sdist bdist_wheel
  twine upload --repository testpypi dist/*
  ```
- Create an API key in PyPI, making sure to only give upload access to your repo.
- Go to project settings in GitHub, add a new secret called `TEST_PYPI_API_TOKEN`
