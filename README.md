pychrone
=============
Python 3 module for generatings isochrones from point

## How to install

You can install python-digitalocean using **pip**

    pip install -U pychrone

or via sources:

    python setup.py install

If you have serveral python versions installed you will probably use **pip3** and **python3** commands accordingly.



## Features

This module generates walking [isochrone](https://en.wiktionary.org/wiki/isochrone) from the set point with defined latitude and longtitude with defined time.

All details of walking routes and coordinates are from OpenStreetMap, so you will need an internet connection for this module to work.

Also module will try to optimize isochrone shape with [α-shape algorithm](https://en.wikipedia.org/wiki/Alpha_shape) to make it more natural and clean.

Main function of module takes the following arguments:

**Create_isochrone(**_longtitude, latitude, speed=4.5, output="geojson"_**)**

- _longitude_ - longitude of point to create isochrone from;
- _latitude_ - latitude of point to create isochrone from;
- _speed_ - pedestrian speed in km/h, default is 4.5;
- _output_ - output format, default is "geojson", wich generates valid [GeoJSON](http://geojson.org) polygon. Other option is "shape", that generates [Shapely](http://shapely.readthedocs.io/) object.

## Usage:

In this small example module will return 5-minute isochrone from point with coordinates (37.847591, 55.920284) in GeoJSON format assuming pedestrian speed as 4.5 km/h.

IN:
```python
from pychrone import Create_isochrone

Create_isochrone(37.847591, 55.920284, 5)
```

OUT:
```json
{"coordinates": [[[37.8460729, 55.9174363], [37.8464059, 55.9175894], [37.847672, 55.9178994], [37.8485452, 55.9179112], [37.8489915, 55.9179172], [37.8490785, 55.9179534], [37.8502528, 55.918252], [37.8508537, 55.9190215], [37.8521326, 55.9193121], [37.8523401, 55.9195966], [37.8523826, 55.9196535], [37.8526471, 55.920433], [37.8527015, 55.9206193], [37.852584, 55.9210867], [37.8512857, 55.9218685], [37.8500913, 55.9216824], [37.8481064, 55.9218883], [37.8480311, 55.9218827], [37.8464856, 55.9216235], [37.8458339, 55.9220129], [37.8452347, 55.9223078], [37.8451153, 55.9223076], [37.843753, 55.9214498], [37.8434385, 55.9211565], [37.8432352, 55.9210091], [37.843344, 55.9201537], [37.8436392, 55.9200188], [37.8442215, 55.9195563], [37.8445491, 55.9189478], [37.8453806, 55.9179848], [37.8458505, 55.9173872], [37.8460729, 55.9174363]]], "type": "Polygon"}
```