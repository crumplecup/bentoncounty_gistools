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

Source files, like shapefiles (.shp) and geodatabases (.gdb), contain the spatial data that ArcGIS uses to draw a map.  To make a source available to build maps on the server, first we upload the file onto an ArcGIS server, then publish it as a service.  When using a service, the server references the source data to determine the style and color of the layer.  But there are some drawbacks.  Published services do not include legend groups, so if the layers are nested into groups using ArcGIS Desktop, this information is lost when publishing the source data as a service.  For instance, the Corvallis Natural Features Inventory has two broad categories, Features and Hazards, with several subgroups contained in each branch.  In the published service, this nesting information is lost, and all 30+ layers appear at the same legend level, leaving no distinction between features, hazards, or subcategories like flooding.

If labels are set in the source data, and popups enabled, they will carry through onto the server side, but this is not always the case.  Some of the layers published in the county planning map come from external government sources, such as the USGS soil layer, or the FEMA flood hazard map.  When the county does not own the source data, changes to the labeling, style or popup configuration are still possible by making these modifications on the server side.  Even when the county owns the source data, changing the color or style of a layer, or the size of the labels, can be easier to do by adjusting the settings on the server side, rather than updating the service definition by modifying and uploading new source data.

The primary motivation for this package is the facilitate tweaking of the server-side display settings for layers, and automating the process of updating existing maps and creating new maps incorporating these changed settings.
