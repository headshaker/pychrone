pychrone
=============

.. image:: https://api.travis-ci.org/headshaker/pychrone.svg?branch=master
   :target: http://travis-ci.org/headshaker/pychrone
.. image:: https://img.shields.io/pypi/v/pychrone.svg
   :target: https://pypi.python.org/pypi/pychrone
.. image:: https://img.shields.io/pypi/pyversions/pychrone.svg
   :target: https://pypi.python.org/pypi/pychrone

Python 3 module for generatings isochrones from point


History
-------

0.0.2 - Added several types of isochrone generation: walking, driving or biking.

0.0.1 - Initial version, only walking isochrones supported.

How to install
--------------

You can install ``pychrone`` using ``pip``:

::

   pip install -U pychrone

or via sources:

::

   python setup.py install

If you have serveral python versions installed you will probably use ``pip3`` and ``python3`` commands accordingly.



Features
--------

This module generates `isochrone <https://en.wiktionary.org/wiki/isochrone>`__ from the set point with defined latitude and longtitude with defined time.

All details of walking routes and coordinates are from OpenStreetMap, so you will need an internet connection for this module to work.

Also module will try to optimize isochrone shape with `α-shape algorithm <https://en.wikipedia.org/wiki/Alpha_shape>`__ to make it more natural and clean.

Main function of module takes the following arguments:

**Create_isochrone(** *longtitude, latitude, speed=4.5, output="geojson", route="walk"* **)**

- *longitude* - longitude of point to create isochrone from;
- *latitude* - latitude of point to create isochrone from;
- *speed* - pedestrian speed in km/h, default is 4.5;
- *output* - output format, default is "geojson", wich generates valid `GeoJSON <http://geojson.org>`__ polygon. Other option is "shape", that generates `Shapely <http://shapely.readthedocs.io/>`__ object;
- *route* - type of routing for isochrone generation. Default is "walk", that means that isochrone will be generated for pedestrians. Other possible options are "drive" (for cars) and "bike" (for bikes).

Usage:
------

In this small example ``pychrone`` will return 5-minute walking isochrone from point with coordinates (37.847591, 55.920284) in GeoJSON format assuming pedestrian speed as 4.5 km/h:

``IN:``

.. code:: python

   from pychrone import Create_isochrone

   Create_isochrone(37.847591, 55.920284, 5)

``OUT:``

.. code:: json

   {"coordinates": [[[37.8460729, 55.9174363], [37.8464059, 55.9175894], [37.847672, 55.9178994], [37.8485452, 55.9179112], [37.8489915, 55.9179172], [37.8490785, 55.9179534], [37.8502528, 55.918252], [37.8508537, 55.9190215], [37.8521326, 55.9193121], [37.8523401, 55.9195966], [37.8523826, 55.9196535], [37.8526471, 55.920433], [37.8527015, 55.9206193], [37.852584, 55.9210867], [37.8512857, 55.9218685], [37.8500913, 55.9216824], [37.8481064, 55.9218883], [37.8480311, 55.9218827], [37.8464856, 55.9216235], [37.8458339, 55.9220129], [37.8452347, 55.9223078], [37.8451153, 55.9223076], [37.843753, 55.9214498], [37.8434385, 55.9211565], [37.8432352, 55.9210091], [37.843344, 55.9201537], [37.8436392, 55.9200188], [37.8442215, 55.9195563], [37.8445491, 55.9189478], [37.8453806, 55.9179848], [37.8458505, 55.9173872], [37.8460729, 55.9174363]]], "type": "Polygon"}


And here we will build a 5-minute biking isochrone from the same point in GeoJSON format assuming bike speed as 15 km/h:

``IN:``

.. code:: python

   from pychrone import Create_isochrone

   Create_isochrone(37.847591, 55.920284, 5, speed=15, route='bike')

``OUT:``

.. code:: json

   {"coordinates": [[[37.8567192, 55.9159054], [37.8566902, 55.917482], [37.8574327, 55.9183582], [37.8596827, 55.9179265], [37.8606264, 55.9174921], [37.8607145, 55.9174898], [37.8616878, 55.9182527], [37.8623098, 55.9184031], [37.8623315, 55.9186923], [37.8623347, 55.9187348], [37.8617334, 55.9187584], [37.8601876, 55.9216012], [37.8601928, 55.9216375], [37.8625041, 55.9234816], [37.8606823, 55.9239551], [37.8602133, 55.9240344], [37.859944, 55.9240621], [37.8596538, 55.9240835], [37.858323, 55.9265212], [37.858095, 55.9258876], [37.8579296, 55.9254856], [37.8577715, 55.9252287], [37.857535, 55.9249517], [37.8571648, 55.9246052], [37.8570523, 55.9244923], [37.8567998, 55.9242646], [37.8564721, 55.9239992], [37.8551838, 55.9236002], [37.8550675, 55.9236167], [37.854535, 55.9236923], [37.8539227, 55.9237794], [37.8537368, 55.9238044], [37.8517414, 55.9236685], [37.8506852, 55.9233489], [37.8503534, 55.9223657], [37.8481771, 55.9215311], [37.8461656, 55.9213583], [37.8453504, 55.9211411], [37.8434385, 55.9211565], [37.8424404, 55.922531], [37.8414824, 55.9219328], [37.839682, 55.9204985], [37.8381736, 55.919545], [37.8379558, 55.9195288], [37.8378175, 55.9195185], [37.8368864, 55.9194489], [37.8355386, 55.9177032], [37.8349836, 55.9175541], [37.8351224, 55.9173399], [37.8353122, 55.91707], [37.8354487, 55.9168568], [37.8357087, 55.9170776], [37.8382045, 55.9171129], [37.8392138, 55.9171165], [37.8404943, 55.9171611], [37.8418891, 55.9172097], [37.8435035, 55.915587], [37.8435064, 55.9154623], [37.841976, 55.9137454], [37.8421039, 55.9136196], [37.842337, 55.9138113], [37.8445747, 55.9138635], [37.8453206, 55.9139934], [37.8453969, 55.9139946], [37.8456471, 55.9139985], [37.8458805, 55.9140022], [37.8461503, 55.9140065], [37.8466495, 55.9139142], [37.8470988, 55.9138738], [37.8472903, 55.9138372], [37.8485149, 55.9145846], [37.8494446, 55.9152114], [37.8494888, 55.9152412], [37.850287, 55.9162542], [37.8526657, 55.9159628], [37.8546403, 55.9159654], [37.8549614, 55.9159579], [37.8565237, 55.9159109], [37.8566544, 55.915907], [37.8567192, 55.9159054]]], "type": "Polygon"}