# -*- coding: utf-8 -*-

"""UNIT TESTS FOR EXAMPLE SUBPACKAGE.

This module contains unit tests for the example subpackage.

"""

from unittest import TestCase

import numpy as np
from numpy import testing as npt

from configure_package_name.example import classes, hello, math


class ClassesTestCase(TestCase):
    """Test case for ``classes`` module."""

    def setUp(self):
        """Set test parameter values."""
        r_sun = 7e8
        t_sun = 5800
        self._sb_inst = classes.StefBoltz(r_sun, t_sun)
        self._expected_out = 3.951223664081994e26

    def tearDown(self):
        """Unset test parameter values."""
        self._sb_inst = None
        self._expected_out = None

    def test_luminosity(self):
        """Test ``configure_package_name.example.classes.StefBoltz.luminosity`` method.

        See Also
        --------
        configure_package_name.example.classes.StefBoltz : Implementation of the
            ``StefBoltz`` class.

        """
        npt.assert_equal(
            self._sb_inst.luminosity(),
            self._expected_out,
            err_msg='Incorrect luminosity output.',
        )


class HelloTestCase(TestCase):
    """Test case for ``hello`` module."""

    def setUp(self):
        """Set test parameter values."""
        self._expected_out = 'Hello World!'

    def tearDown(self):
        """Unset test parameter values."""
        self._expected_out = None

    def test_hello_world(self):
        """Test ``configure_package_name.example.hello.hello_world`` function.

        See Also
        --------
        configure_package_name.example.hello.hello_world : Implementation of the
            ``hello_world`` function.

        """
        npt.assert_equal(
            hello.hello_world(),
            self._expected_out,
            err_msg='Incorrect hello_world output.',
        )


class MathTestCase(TestCase):
    """Test case for ``math`` module."""

    def setUp(self):
        """Set test parameter values."""
        self._first = 1
        self._second = 2
        self._drake_param = [1, 0.2, 1, 1, 1, 0.1, 1000]
        self._mad_data = np.arange(9).reshape(3, 3)
        self._add_res = 3
        self._drake_res = 20
        self._mad_res = 2.0

    def tearDown(self):
        """Unset test parameter values."""
        self._first = None
        self._second = None
        self._drake_param = None
        self._mad_data = None
        self._add_res = None
        self._drake_res = None
        self._mad_res = None

    def test_add_two_ints(self):
        """Test ``configure_package_name.example.math.add_two_ints`` function.

        See Also
        --------
        configure_package_name.example.math.test_add_two_ints : Implementation of the
            ``test_add_two_ints`` function.

        """
        npt.assert_equal(
            math.add_two_ints(self._first, self._second),
            self._add_res,
            err_msg='Incorrect addition result.',
        )

        npt.assert_raises(
            TypeError, math.add_two_ints, self._first, float(self._second),
        )

    def test_drake_equation(self):
        """Test ``configure_package_name.example.math.drake_equation`` function.

        See Also
        --------
        configure_package_name.example.math.drake_equation : Implementation of the
            ``drake_equation`` function.

        """
        npt.assert_equal(
            math.drake_equation(self._drake_param),
            self._drake_res,
            err_msg='Incorrect Drake eq result.',
        )

    def test_mad(self):
        """Test ``configure_package_name.example.math.mad`` function.

        See Also
        --------
        configure_package_name.example.math.mad : Implementation of the
            ``mad`` function.

        """
        npt.assert_equal(
            math.mad(self._mad_data),
            self._mad_res,
            err_msg='Incorrect median absolute deviation',
        )
