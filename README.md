# Python Package Template

In order to use this template please follow these instructions:

> Note: unless specified (*e.g.* "On GitHub:") the instructions should be carried out locally (*i.e.* on your machine).

## Set-Up

1. On GitHub: Click the `Use this template` button.
2. On GitHub: Specify a `Repository name` for your package. Ideally your package name should match the repository name.
3. On GitHub: Click the `Create repository from template` button.
4. Clone your remote repository. *e.g.* for a packaged called `mypackage`
```bash
git clone https://github.com/username/mypackage
```
5. Go to the package directory.
```bash
cd mypackage
```
6. Update the directory `package_name` to the name of your package. *e.g.*
```bash
mv package_name mypackage
```
7. Update the variable `__name__` in `setup.py` to your package name. *e.g.*
```python
__name__ = 'mypackage'
```
8. Set `testpaths` and `cov` in `setup.cfg` to your package name.
```ini
[tool:pytest]
addopts = --verbose --pep8 --cov=mypackage
testpaths = mypackage
```
9. Set `package_name` in `.travis.yml` to your package name. *e.g.*
```yaml
- if [[ $TRAVIS_PYTHON_VERSION == '3.6' ]]; then sphinx-apidoc -feo docs/source mypackage/; fi
```
10. Update `mypackage/info.py` with your package details. *e.g.*
```python
# Set the package details
__author__ = 'Lando Calrissian'
__email__ = 'lando@bespin.org'
__year__ = '2019'
__url__ = 'https://github.com/lando/mypackage'
__description__ = 'A package for managing mining operations'
__long_description__ 'A package for managing mining operations...'
__requires__ = ['numpy', 'matplotlib']  # Your package dependencies
```
11. Install [`sphinx`](http://www.sphinx-doc.org).
```bash
pip install sphinx sphinx-rtd-theme numpydoc
```
12. Change to the `docs` directory and run `sphinx-quickstart`.
```bash
cd docs
sphinx-quickstart
```
    When the prompted

  > > Separate source and build directories (y/n) [n]:

    type `y`.
13. Change back to the root directory and push your changes to GitHub.
```bash
cd ..
git add .
git commit -m "updated template"
git push origin master
```

## Management

Now that you have set up your package management tools you can start adding content to your package. 

## Optional

1. Define your contribution guidelines in `CONTRIBUTING.md`.
