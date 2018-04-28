#!/usr/bin/env python3
"""Tests for Lesson 03 Activity -- Context Manager."""

import pytest
from io import StringIO
from unittest import mock
import locke as lk

small_locke = lk.Locke(5)
large_locke = lk.Locke(10)
boats = 8


def test_error():
    """Too many boats through a small locke will raise an exception."""
    with pytest.raises(ValueError):
        with small_locke as locke:
            locke.move_boats_through(boats)


def test_print_statements():
    """A lock with sufficient capacity can move boats without incident."""
    # Captures all print statements
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        with large_locke as locke:
            locke.move_boats_through(boats)
        res = mock_stdout.getvalue()
        assert "Stopping the pumps." in res
        assert "Opening the doors." in res
        assert "Closing the doors." in res
        assert "Restarting the pumps." in res
