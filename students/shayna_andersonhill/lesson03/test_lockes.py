import pytest
import lockes

small_locke = lockes.Locke(5)
large_locke = lockes.Locke(10)
boat_count = 8

def test_raise_error():
    with pytest.raises(ValueError) as exc_info:
        small_locke.move_boats_through(boat_count)
        assert exc_info.value == "Boat count exceeds Locke capacity."

def test_simulation():
    """No error should be raised"""
    large_locke.move_boats_through(boat_count)
    

