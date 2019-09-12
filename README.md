# Python Package Template

In order to use this template please do the following:

1. Fork this repository.
1. Update the directory `package_name` to the name of your package.
1. Update the variable `__name__` in `setup.py` to your package name.
1. Set `testpaths` in `setup.cfg` to your package name.
1. Set `package_name` in `.travis.yml` to your package name.
1. Update `info.py` with your package details.
1. Finally, run the following in the `docs` directory.
```bash
$ sphinx-quickstart
```
    When the prompted

  > > Separate source and build directories (y/n) [n]:

    type `y`.

Optionally, you can also do the following:

1. Define your contribution guidelines in `CONTRIBUTING.md`.
