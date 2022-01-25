import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    required = fh.read().splitlines()

with open(os.path.join('gha_aut_test', '_version.py')) as fp:
    exec(fp.read())

setuptools.setup(
    name="gha_aut_test",
    description="GHA Automation Tester",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    author="Doruk Kilitcioglu",
    url="https://github.com/dorukkilitcioglu/sphinx_test",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=required,
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/dorukkilitcioglu/sphinx_test",
        "Documentation": "https://dorukkilitcioglu.github.io/sphinx_test/"
    }
)
