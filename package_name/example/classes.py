# -*- coding: utf-8 -*-

"""CLASSES MODULE.

This module provides examples of how write classes according to the standards
proposed by this template.

.. warning::

    The `D107 <https://www.pydocstyle.org/en/latest/error_codes.html>`_ error
    is supressed througout the package to avoid havving to document
    ``__init__`` methods, which is permitted by numpydoc standards.

"""

from numpy import pi


class StefBoltz(object):
    r"""The Stefan–Boltzmann Law.

    A basic class implementation of the Stefan-Boltzmann law.

    Attributes
    ----------
    sigma : float
        Stefan-Boltzmann constant (:math:`5.6704\times 10^{-8} \mathrm{W}
        \mathrm{m}^{-2}\mathrm{K}^{-4}`)

    Parameters
    ----------
    radius : float
        Stellar radius
    eff_temp : float
        Effective temperature

    """

    def __init__(self, radius: float, eff_temp: float):
        # The Stefan-Boltzmann constant
        self.sigma = 5.6704e-8  # Wm^−2K^−4
        self._radius = radius  # m
        self._eff_temp = eff_temp  # K
        self._const_fac = 4 * pi * self.sigma

    def luminosity(self) -> float:
        r"""Luminosity.

        Calculate the luminosity of a star.

        Returns
        -------
        float
            Stellar luminosity in Watts

        Examples
        --------
        Calculate the luminosity of the Sun

        >>> from configure_package_name.example.classes import StefBoltz
        >>> r_sun = 7e8
        >>> t_sun = 5800
        >>> StefBoltz(r_sun, t_sun).luminosity()
        3.951223664081994e+26

        Notes
        -----
        This method implements the following equation

        .. math::

            L = 4\pi R^2\sigma T_e^4

        where:

        - :math:`L` is the luminosity,
        - :math:`R` is the stellar radius,
        - :math:`\sigma` is Stefan-Boltzmann constant,
        - and :math:`T_e` is the effective temperature.

        """
        return self._const_fac * self._radius ** 2 * self._eff_temp ** 4
