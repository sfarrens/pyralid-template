# Pyralid Template

For packaging Python projects

| Usage | Development | Release |
| ----- | ----------- | ------- |
| [![docs](https://img.shields.io/badge/docs-Sphinx-blue)](https://configure_ghuser.github.io/configure_package_name/) | [![build](https://github.com/configure_ghuser/configure_package_name/workflows/CI/badge.svg)](https://github.com/configure_ghuser/configure_package_name/actions?query=workflow%3ACI) | [![release](https://img.shields.io/github/v/release/configure_ghuser/configure_package_name)](https://github.com/configure_ghuser/configure_package_name/releases/latest) |
| [![license](https://img.shields.io/github/license/configure_ghuser/configure_package_name)](https://github.com/configure_ghuser/configure_package_name/blob/master/LICENCE.txt) | [![deploy](https://github.com/configure_ghuser/configure_package_name/workflows/CD/badge.svg)](https://github.com/configure_ghuser/configure_package_name/actions?query=workflow%3ACD) | [![pypi](https://img.shields.io/pypi/v/configure_package_name)](https://pypi.org/project/configure_package_name/) |
| [![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide) | [![codecov](https://codecov.io/gh/configure_ghuser/configure_package_name/branch/master/graph/badge.svg?token=XHJIQXV7AX)](https://codecov.io/gh/configure_ghuser/configure_package_name) | [![python](https://img.shields.io/pypi/pyversions/configure_package_name)](https://www.python.org/downloads/source/) |
| [![contribute](https://img.shields.io/badge/contribute-read-lightgrey)](https://github.com/configure_ghuser/configure_package_name/blob/master/CONTRIBUTING.md) | [![CodeFactor](https://www.codefactor.io/repository/github/configure_ghuser/configure_package_name/badge)](https://www.codefactor.io/repository/github/configure_ghuser/configure_package_name) | |
| [![coc](https://img.shields.io/badge/conduct-read-lightgrey)](https://github.com/configure_ghuser/configure_package_name/blob/master/CODE_OF_CONDUCT.md) | [![Updates](https://pyup.io/repos/github/configure_ghuser/configure_package_name/shield.svg)](https://pyup.io/repos/github/configure_ghuser/configure_package_name/) | |

---
> Author: <a href="https://sfarrens.github.io/" target="_blank" style="text-decoration:none; color: #F08080">Samuel Farrens</a>  
> Email: <a href="mailto:samuel.farrens@cea.fr" style="text-decoration:none; color: #F08080">samuel.farrens@cea.fr</a>  
> Year: 2020  
---

The Pyralid template is designed to enable users to quickly package a Python project. After following the set-up instructions you should be able to automatically run CI tests and generate API documentation for your code.

See [pyraliddemo](https://github.com/sfarrens/pyraliddemo) for a demo package created with the Pyralid template.

## Contents

1. [Set-Up](#Set-Up)
1. [Management](#Management)
1. [Deployment](#Deployment)
1. [CosmoStat](#CosmoStat)

## Set-Up

In order to use this template please follow the instructions provided below.

### Step 1: Get a remote copy of the template

The following instructions are for the GitHub website.

1. Click the `Use this template` button.

   This will take you to a page that says "Create a new repository from pyralid-template".

2. Specify a `Repository name` for your package.

   Ideally your package name should match the repository name. Avoid using hyphens or underscores in your package name as this can cause issues later. Note that you can change the name later if necessary.

3. Click the box next to `Include all branches`.

   This will ensure your template includes the `gh-pages` branch you will need for your API documentation.

4. Click the `Create repository from template` button.

   This should create a new repository on your GitHub account.

5. Take note of your repository URL.

### Step 2: Configure the template

The following instructions should be run in a terminal on your local machine.

1. Clone your remote repository using your repository URL. *e.g.* for a package called `mypackage` you would run:
```bash
git clone https://github.com/username/mypackage
```
2. Go to the package directory. *e.g.*
```bash
cd mypackage
```
3. Run the configuration script and follow the instructions.
```bash
./configure.sh
```
4. If you chose not to run git commands in the configuration script then manually push your changes to GitHub.
```bash
git add .
git commit -m "updated template with package name"
git push
```

### Step 3: Activate coverage tests

The following instructions are for the codecov website.

1. Go to https://codecov.io/.
2. Log in using your GitHub account details.
3. Click the `Add new repository` button.
4. Find the your repository from the list provided and click on it.

### Step 4: Activate dependency checks

The following instructions are for the PyUp website.

1. Go to https://pyup.io/.
2. Log in using your GitHub account details.
3. Click the `Add Repo` button.
4. Find the your repository from the list provided and click on the `Add` button.
5. In the pop-up window leave the Setup options as they are and click the `Add` button.

If you added any dependencies with the `configure.sh` script then PyUp will open some pull requests to pin these to the latest versions.

PyUp will also create branch called `pyup-config` with a new `.pyup.yml` file. You can delete this branch as follows:

```bash
git push origin -d pyup-config
```

### Step 5: Check that everything works

Please do the following to make sure everything is working as expected.

1. On your machine, create a new branch. *e.g.*
```bash
git checkout -b new_branch
```
2. Make a modification to any of the files. *e.g.* add a new function to `example/math.py`.
```python
def add_two_floats(first_value: float, second_value: float) -> float:
    """Add Two Floats.

    Add two float values.

    Parameters
    ----------
    first_value : float
        First float value
    second_value : float
        Second float value

    Returns
    -------
    float
        Result of addition

    Raises
    ------
    TypeError
        For invalid input types.

    """
    fv_is_float = isinstance(first_value, float)
    sv_is_float = isinstance(second_value, float)

    if not all((fv_is_float, sv_is_float)):
        raise TypeError('Inputs must be floats.')

    return first_value + second_value
```
3. Add, commit and push your changes.
```bash
git add .
git commit -m "testing CI"
git push origin new_branch
```
4. Go to the your remote repository and click on the `Compare & pull request` button that should have appeared for your branch.
5. Provide a title and description for your pull request and click the `Create pull request` button.
6. Once open, your pull request should automatically launch the GitHub actions CI tests. Note that this may take a few seconds to start. Click on the link that appears if you want to follow the progress of the tests.
7. codecov will raise an error if your new function is not covered by unit tests. You can either add some or ignore this error.
8. Once your CI tests have passed you can merge your pull request, which should automatically launch the CD process. This will generate your package API documentation. Go to *e.g.* https://username.github.io/mypackage/ to view your documentation.

## Management

Now that your package is set up you can start managing your own code.

### Add new content

1. Add new subpackages following the contents of the `example` folder. Be sure to include a `__init__.py` file in every new directory you create.
2. Add new submodules following the contents of `classes.py`, `hello.py` and `math.py`. Be sure to follow the [Numpy docstring conventions](https://numpydoc.readthedocs.io/en/latest/format.html) and [wemake-python-styleguide](https://wemake-python-stylegui.de/) in writing your API documentation and code.
3. Write unit tests as you add new functions and classes to retain the highest possible code coverage. Follow the examples in `tests`.
4. To manage your code development you should follow the procedure described in Step 5 of the set-up. Note that you can continue to work on a branch you created for an open pull request up until it is merged. After merging a branch it is good practice to delete it.

### Clean up

1. Once you have added some of your own content remove the `example` subpackage and corresponding tests.
2. Update `requirements.txt` with a list of your code dependencies so that they can be installed automatically with your package.
3. Replace this `README.md` with your own package documentation.
4. Update `docs/source/index.rst` with a more detailed description of your package.
5. Delete the `configure.sh` script.

### Optional

1. Get a grade for your package from [CodeFactor](https://www.codefactor.io/).
2. Define your package contribution guidelines in `CONTRIBUTING.md`.
3. Customise your API documentation in `docs/source/conf.py`.
4. Customise your CI tests in `setup.cfg`.
5. Customise the running of your CI/CD tests in `.github/workflows`.

### Local Tests

To speed up development of your package it may be convenient to run tests locally before submitting a pull request. This can be done as follows:

1. Install the developer tools.
```bash
pip install -r develop.txt
```
2. Run the tests locally.
```bash
python setup.py test
```

## Deployment

### Make a release

Before deploying your code you should make a *release*.

1. Click the button on the right of your GitHub repo that says `Create a new release`.

2. Specify a *Tag version* (*e.g.* `v0.0.1`).

   This should be identical to the version specified in `setup.py`.

3. Provide a *Release title* (*e.g.* `First Release`).

4. Describe what is included in your release.

   It is good practice to specify things that have changed from previous releases.

### Deploy package on PyPi

In order to upload your package to [PyPi](https://pypi.org/) (which allows users to install your package with `pip`), you should follow these steps:

1. Check if your package name has already been taken. *e.g.*
```bash
pip search mypackage
```
2. If the name is already taken, you may want to rename your package.
3. Create an account on https://pypi.org/.
4. Install twine.
```bash
pip install twine
```
5. Build a distribution of your package.
```bash
python setup.py sdist bdist_wheel
```
6. Finally, upload your distribution to PyPi.
```bash
twine upload dist/*
```
7. Your package can now be installed anywhere using `pip`. *e.g.*
```bash
pip install mypackage
```
8. To update your package, change the version number in `setup.py` and repeat steps 5 and 6.

> Note that step 6 can be simplied by creating a [.pypirc](https://docs.python.org/3.3/distutils/packageindex.html#pypirc) file.
