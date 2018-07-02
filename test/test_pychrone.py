import pytest
import pychrone
import geojson


def test_none():
    assert (pychrone.Create_isochrone(37.847591, 55.920284, 5) !=None)

def test_geojson():
    assert (isinstance(pychrone.Create_isochrone(37.847591, 55.920284, 5), geojson.geometry.Polygon))