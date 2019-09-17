# Python Package Template

This template is designed to enable users to quickly package a Python project. After following the set-up instructions you should be able to run CI tests and automatically generate API documentation for your code.

## Set-Up

In order to use this template please follow the instructions provided below.

### Step 1: Get a remote copy of the template

The following instructions are for the GitHub website.

1. Click the `Use this template` button.
2. Specify a `Repository name` for your package. Ideally your package name should match the repository name. Note that you can change the name later if necessary.
3. Click the `Create repository from template` button. This should create a new repository on your GitHub account. Take note of your repository URL.

### Step 2: Configure the template

The following instructions should be run in a terminal on your local machine.

1. Clone your remote repository using your repository URL. *e.g.* for a packaged called `mypackage` you would run:
```bash
git clone https://github.com/username/mypackage
```
2. Go to the package directory. *e.g.*
```bash
cd mypackage
```
3. Run the configuration script
```bash
./configure
```
4. Push your changes to GitHub.
```bash
git add .
git commit -m "updated template"
git push
```

### Step 3: Activate CI tests

The following instructions are for the Travis-CI website.

1. Go to https://travis-ci.org/
2. Log in using your GitHub account details.
3. Go to your list of repositories (https://travis-ci.org/account/repositories).
4. Find the package name you provided for the repository and click the switch on the right to activate CI tests.

### Step 4: Automate API documentation build

1. In the root directory of your package run:
```bash
git checkout -b gh-pages
git rm -rf .
git push --set-upstream origin gh-pages
```
2. On your GitHub page, go to Settings>Developer settings>Personal access tokens.
3. Click on the `Generate new token` button and copy the token string.
4. On the Travis website, click on your package and go to More options>Settings.
5. Under `Environment Variables` provide the name `GH_TOKEN`, then paste the value of your personal access token, and click the `Add` button.

> More detailed instructions are provided in the [travis-sphinx documentation](https://github.com/Syntaf/travis-sphinx).

### Step 5: Run tests

Please do the following to make sure everything is working as expected.

1. On your machine, create a new branch. *e.g.*
```bash
git checkout -b new_branch
```
2. Make a modification to any of the files. *e.g.* add a new function to `math.py`.
```python
def add_float(x, y):
    """Add Floats

    Add two float values.

    Parameters
    ----------
    x : float
        First value
    y : float
        Second value

    Retunrs
    -------
    float
        Result of addition

    Raises
    ------
    TypeError
        For invalid input types.

    """

    if not isinstance(x, float) or not isinstance(y, float):
        raise TypeError('Inputs must be floats.')

    return x + y
```
3. Add, commit and push your changes.
```bash
git add .
git commit -m "testing"
git push origin new_branch
```
4. Go to the your remote repository and click on the `Create pull request` button that should have appeared for your branch.
5. Follow the instruction to open your pull request.
6. Once open your pull request should automatically launch the Travis CI tests. Click on the link that appears to follow their progress.
7. Once your CI tests have passed you can merge your pull request, which should automatically generate your package API documentation. Go to *e.g.* https://username.github.io/mypackage/ to view your documentation.

## Management

Now that your package is set up you can start managing your own code.

### Add new content

1. Add new module following the contents `example` folder. Be sure to include a `__init__.py` file in every new directory you create.
2. Add new submodules following the contents of `hello.py` and `math.py`. Be sure to follow the [Numpy docstring conventions](https://numpydoc.readthedocs.io/en/latest/format.html) in writing your API documentation.
3. Write unit tests as you add new functions and classes to retain the highest possible code coverage. Follow the examples in `tests`.

### Clean up

1. Once you have added some of your own content remove the `example` module.
2. Update `info.py` with a description of what your code does.
3. Replace this `README.md` with your own package documentation.
4. Update `docs/source/index.rst` with a more detailed description of your package.

### Optional

1. Define your package contribution guidelines in `CONTRIBUTING.md`.
2. Customise your API documentation in `docs/source/conf.py`.
3. Customise your CI and coverage tests in `setup.cfg`.
4. Customise the running of your CI tests in `.travis.yml`.

## Deployment

Details coming soon!
