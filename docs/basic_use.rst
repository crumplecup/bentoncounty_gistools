=====
Basic Use
=====

When constructing a web map from a published service, it is possible to customize the viewing experience by changing the layer style, labeling and other aspects.  Once the viewing experience is configured correctly, you will likely want these changes to persist when referencing the source layers on future maps.  For instance, the county zoning and taxlot maps share several common sources.  It would be repetitive and error-prone to repeat the server-side configuration independently for every new map, but it is not always possible to include all the necessary information for building the map in the service definitions of the source layers.  The solution employed by this package is to use template web maps to define the server-specific view settings associated with each layer.

Template web maps serve as a reference for building future web maps.  Each template map is devoted to a single group layer, whereas maps used by staff for planning typically combine several group layers together.  In the legend, group layers are named categories that include several features or layers.  Clicking on a group layer in the legend, or the expansion carrot adjacent to the legend name, will show the list of included layers, but the group layer itself does not hold its own data, merely references to child data.

The package function `build_template()` reads layers information from the template map and stores this info in a local file called `template.json`, which it references for future builds.  The ``json`` format is a widely used standard for storing nested key-value pairs, and under the hood all ArcGIS web maps are essentially ``json`` files telling the server where to find the source data and how to construct the visual representation.  Group layers add a level of nesting to the key-value pairs stored in the ``json`` document, and so in order to use a single function for reading data from multiple template files, the level of nesting in each template file has to be the same.  Therefore, every template map has a parent category (arbitrarily called `Base`), and then a single group category holding the layers specific to the template.  The package does not support template maps that deviate from this structure.

::

        Why is a parent "Base" layer necessary?  In order to make maps more composable, the package
        functions for adding layers insert the desired group into the parent group of a web map.
        Typically the parent group is named after the map's overarching purpose, such as "Benton
        County Zoning Map", or "Benton County Taxlot Map".  Template maps provide the "Base" layer
        as a trunk onto which the package functions attach other groups as branches.

The standard process for updating the visual representation of a map layer is to open the corresponding template and modify the settings in the ArcGIS Online GUI, then run the `build_template()` function to record the changes for later use.

=======                         =======
Name                            Description
=======                         =======
template_address_map_           Addresses for County and City of Corvallis.
template_aerial_imagery_map_    County and ESRI high resolution orthography.
=======                         =======

.. _template_address_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=5c507b0f03084f33b8da587cbd4b830b
.. _template_aerial_imagery_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=4cb460dcb6464724b2e99ba696d5dd77
