====
lcoe
====

A command line tool and Python package to calculate levelised cost of electricity

Description
===========

Calculate levelised cost of electricity on the command line with the ``lcoe`` command::

    $ lcoe 500000000 2000000000 25000000 0.07 20
    LCOE is 0.03609823143581392

Use the lcoe library in your Python code::

    from lcoe.lcoe import lcoe

    operating_cost = 25000000  #$million/year
    capital_cost = 500000000  # $million
    discount_rate = 0.07  # %
    lifetime = 20
    annual_output = 2000000000  # kWh

    lcoe(annual_output, capital_cost, operating_cost, discount_rate, lifetime)
