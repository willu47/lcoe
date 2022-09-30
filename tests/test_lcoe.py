# -*- coding: utf-8 -*-

from pytest import approx
from lcoe.lcoe import lcoe

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def test_lcoe():
    """
    """
    operating_cost = 0.063*810000  #$million/year
    capital_cost = 1413073  # $million
    discount_rate = 0.05  # %
    lifetime = 3
    annual_output = 810000  # kWh

    actual = lcoe(annual_output, capital_cost, operating_cost, discount_rate, lifetime)
    expected = 0.673  # $/kWh
    assert actual == approx(expected, rel=1e-3)