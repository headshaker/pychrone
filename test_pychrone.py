import pychrone
import pytest


def test_negative():
    assert (pychrone.Create_isochrone(37.847591, 55.920284, 5) !=None)