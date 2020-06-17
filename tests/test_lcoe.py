# -*- coding: utf-8 -*-

from pytest import approx
from lcoe.lcoe import lcoe

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def test_lcoe():
    """
    """
    operating_cost = 25000000  #$million/year
    capital_cost = 500000000  # $million
    discount_rate = 0.07  # %
    lifetime = 20
    annual_output = 2000000000  # kWh

    actual = lcoe(annual_output, capital_cost, operating_cost, discount_rate, lifetime)
    expected = 0.03609823143581392  # $/kWh
    assert actual == approx(expected)