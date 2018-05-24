#!/usr/bin/env python3
"""
Tests for mailroom metaprogramming assignment.
"""
import os
import pytest
from mailroom import DonorDonations, Donor

initial_data = [
    ["Jimmy Nguyen", [653772.32, 12.17]],
    ["Steve Smith", [877.33, 55.67]],
    ["Julia Norton", [663.23, 43.87, 1.32]],
    ["Ed Johnson", [1663.23, 4300.87, 10432.15]],
    ["Elizabeth McBath", [1663.23, 4300.87, 10432.25]]
]

def test_add_donor():
    """Test for adding a new donor in DMS."""
    name = "Teddy Tulip"

    donor = Donor.add_donor(name)
    donor.add_donation(55.55)
    assert donor.name == "Teddy Tulip"
    assert donor.last_donation == 55.55
    assert Donor.find_donor(name) == donor


def test_list_donors():
    """Test displaying donors in the DMS."""
    dr = Donor.list_donors()

    assert "Below is the current donor list:" in dr
    assert "Jimmy Nguyen" in dr
    assert "Elizabeth McBath" in dr


def test_donor_lookup(data):
    """Test finding a donor in the DMS."""
    dl = Donor.donor_lookup("Jimmy Nguyen")

    assert dl.name == "Jimmy Nguyen"


def test_create_donor_report():
    """Test the donor report from the DMS records."""
    dr = Donor.create_donor_report()

    assert dr.startswith("""Donor name                 | Total Donation | Number of Gifts | Average Gifts
--------------------------------------------------------------------------------""")
    assert """Donor name                 | Total Donation | Number of Gifts | Average Gifts
--------------------------------------------------------------------------------
Jimmy Nguyen               |        1505.00 |               3 |        501.67
Steve Smith                |        1198.00 |               3 |        399.33
Julia Norton               |        4500.00 |               3 |       1500.00
Ed Johnson                 |         150.00 |               1 |        150.00
Elizabeth McBath           |       11200.00 |               2 |       5600.00""" in report
