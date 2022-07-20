Usage
=====

Installation
------------

To use Benton County GIS tools, first install it using pip:

.. code-block:: console

   (.venv) $ pip install bentoncounty_gistools

The Benton County Community Development Department uses ArcGIS to record mapping information necessary for processing new permits and other public services. To make this information available online for staff and public access, the county leases space on an ArcGIS Online server, as well as running their own installation on an ArcGIS server locally.  The tools in this package interact with maps stored on an ArcGIS server, allowing staff to update the format and content of these maps quickly and efficiently.

For county staff, if you are interested in changing the format of maps, such as the color and style of a layer, or the size and description of labels for a layer, please refer to the :doc:`Basic Use` section. Modifying the map format requires minimal use of code, or prior experience with Python.  For adjusting the map content, such as adding new layers, or replacing existing layers with updated source data, see the `Development Guide`.  Adjusting map content may require adding additional lines of code, or modifying existing code in the package, but will not introduce programming concepts beyond the beginner level.

Basic Use
---------
