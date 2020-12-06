# -*- coding: utf-8 -*-

"""MATH MODULE.

This module provides examples of how write mathematical functions according
to the standards proposed by this template.

.. warning::

    The `RST304 <https://github.com/peterjc/flake8-rst-docstrings>`_ error
    is supressed througout the package to allow
    `sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_
    citations.

"""

from functools import reduce
from operator import mul

import numpy as np


def add_two_ints(first_value: int, second_value: int) -> int:
    r"""Add Two Integers.

    A simple example function demonstatring the addition of two integer values
    and the return of the sum.

    Parameters
    ----------
    first_value : int
        First integer value
    second_value : int
        Second integer value

    Returns
    -------
    int
        Result of addition

    Raises
    ------
    TypeError
        For invalid input types.

    Examples
    --------
    >>> from configure_package_name.example.math import add_two_ints
    >>> add_two_ints(1, 2)
    3

    Notes
    -----
    This function implements the following equation

    .. math::

        z = x + y

    where :math:`x\in\mathbb{Z}` is the first input integer,
    :math:`y\in\mathbb{Z}` is the second input integer and
    :math:`z\in\mathbb{Z}` is the resulting sum.

    """
    fv_is_int = isinstance(first_value, int)
    sv_is_int = isinstance(second_value, int)

    if not all((fv_is_int, sv_is_int)):
        raise TypeError('Inputs must be ints.')

    return first_value + second_value


def drake_equation(drake_parameters: list) -> int:
    r"""Drake's Equation.

    A very basic implementation of Drake's equation as an example of how to
    cite known equations.

    Parameters
    ----------
    drake_parameters : list
        List of parameters of the Drake equation (see Notes).

    Returns
    -------
    int
        The number of civilizations in our galaxy with which communication
        might be possible (*i.e.* which are on our current past light cone).

    Examples
    --------
    >>> from configure_package_name.example.math import drake_equation
    >>> drake_equation([1, 0.2, 1, 1, 1, 0.1, 1000])
    20

    Notes
    -----
    This function implements the following equation from :cite:`Drake:1965`

    .. math::

        N = R_* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L

    where:

    * :math:`R_*` is the average rate of star formation in our galaxy,
    * :math:`f_p` is the fraction of those stars that have planets,
    * :math:`n_e` is the average number of planets that can potentially support
      life per star that has planets,
    * :math:`f_l` is the fraction of planets that could support life that
      actually develop life at some point,
    * :math:`f_i` is the fraction of planets with life that actually go on to
      develop intelligent life (civilizations),
    * :math:`f_c` is the fraction of civilizations that develop a technology
      that releases detectable signs of their existence into space,
    * and :math:`L` is the length of time for which such civilizations release
      detectable signals into space.

    """
    return int(reduce(mul, drake_parameters, 1))


def mad(input_data: np.ndarray) -> float:
    r"""Median Absolute Deviation.

    This method calculates the median absolute deviation (MAD) of some input
    data.

    .. note::

       Implementation taken from
       `ModOpt <https://cea-cosmic.github.io/ModOpt/>`_

    Parameters
    ----------
    input_data : numpy.ndarray
        Input data array

    Returns
    -------
    float
        MAD value

    Examples
    --------
    >>> import numpy as np
    >>> from configure_package_name.example.math import mad
    >>> data = np.arange(9).reshape(3, 3)
    >>> mad(data)
    2.0

    Notes
    -----
    The MAD is calculated as follows:

    .. math::

        \mathrm{MAD} = \mathrm{median}\left(|X_i - \mathrm{median}(X)|\right)

    where :math:`X` is the input data array and :math:`X_i` is a given element.

    """
    return np.median(np.abs(input_data - np.median(input_data)))
