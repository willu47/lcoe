# -*- coding: utf-8 -*-
"""
Levelised cost of electricity
"""

import argparse
import sys
import logging
import numpy_financial as npf

from lcoe import __version__

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def lcoe(annual_output, capital_cost, annual_operating_cost, discount_rate, lifetime):
    """Compute levelised cost of electricity

    Arguments
    ---------
    annual_output : float
    capital_cost : float
    annual_operating_cost : float
    discount_rate : float
    lifetime : int

    Returns
    -------
    float
    """
    annual_cost_capital = npf.pmt(discount_rate, lifetime, -capital_cost)
    total_annual_cost = annual_cost_capital + annual_operating_cost

    return total_annual_cost / annual_output


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="lcoe {ver}".format(ver=__version__))
    parser.add_argument(
        dest="capital_cost",
        help="Capital cost of the plant in $/kWh",
        type=float,
        metavar="FLOAT")
    parser.add_argument(
        dest="annual_output",
        help="Annual output of the plant in kWh",
        type=float,
        metavar="FLOAT")
    parser.add_argument(
        dest="annual_operating_cost",
        help="Annual operating cost of the plant in $",
        type=float,
        metavar="FLOAT")
    parser.add_argument(
        dest="discount_rate",
        help="Discount rate x where 0 <= x < 1",
        type=float,
        metavar="FLOAT")
    parser.add_argument(
        dest="lifetime",
        help="Lifetime of the plant in years",
        type=int,
        metavar="INT")

    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    _logger.debug("Starting crazy calculations...")
    print("LCOE is {}".format(
        lcoe(args.annual_output,
             args.capital_cost,
             args.annual_operating_cost,
             args.discount_rate,
             args.lifetime)
        ))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
