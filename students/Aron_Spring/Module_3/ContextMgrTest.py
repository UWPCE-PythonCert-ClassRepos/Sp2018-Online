import pytest
import ContextMgr as lk

small_locke = lk.Locke(5)
large_locke = lk.Locke(10)

def small_lk_test(boats=8):
    with pytest.raises(ValueError):
        small_locke.boats_through_locke(boats)

def large_lk_test(boats=12):
    with pytest.raises(ValueError):
        large_locke.boats_through_locke(boats)