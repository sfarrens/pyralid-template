#! /usr/bin/env python  # noqa: Ignore this line
# -*- coding: utf-8 -*-
"""EXAMPLE SCRIPT.

Example demonstrating how to call code API as an executable script.

Examples
--------
To see the available arguments run:

.. code-block:: bash

  example_script.py -h

For example, to calculate the luminosity of the Sun:

.. code-block:: bash

  example_script.py --radius 7e8 --eff_temp 5800

"""

import argparse as ap
import sys

from configure_package_name.example.classes import StefBoltz
from configure_package_name.example.hello import hello_world

line = '----------------'


def get_args():
    """Get Script Arguments.

    Returns
    -------
    argparse.Namespace
        Command line arguments

    """
    parser = ap.ArgumentParser()
    parser.add_argument(
        '--radius', type=float, help='Radius in meters.',
    )
    parser.add_argument(
        '--eff_temp', type=float, help='Effective temperature in Kelvin.',
    )

    return parser.parse_args()


def call_hello():
    """Call Hello World.

    This function calls the ``hello_world`` function and prints the output.

    See Also
    --------
    configure_package_name.example.hello.hello_world : Implementation of the
        ``hello_world`` function.

    """
    print(line)
    print('Example 1')
    print('Call hello_world')
    print(line)
    print('Result:', hello_world())


def call_stefboltz(radius: float, eff_temp: float):
    """Call StefBoltz.

    This function calls the ``StefBoltz`` class and prints the luminosity
    corresponding to the radius and effective temperature provided.

    Parameters
    ----------
    radius : float
        Stellar radius
    eff_temp : float
        Effective temperature

    See Also
    --------
    configure_package_name.example.classes.StefBoltz : Implementation of the ``StefBoltz``
        class.

    """
    luminosity = StefBoltz(radius, eff_temp).luminosity()

    print(line)
    print('Example 2')
    print('Call StefBoltz')
    print(line)
    print('Result:', 'The luminosity is {0:.2e}w.'.format(luminosity))


def run_steps():
    """Call Script Steps.

    This is the main method called by the script. It runs the various
    steps involved.

    """
    args = get_args()
    call_hello()
    print()
    call_stefboltz(args.radius, args.eff_temp)


if __name__ == "__main__":  # noqa: Ignore main method
    sys.exit(run_steps())
