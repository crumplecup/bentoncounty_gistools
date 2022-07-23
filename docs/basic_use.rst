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

The standard process for updating the visual representation of a map layer is to open the corresponding template and modify the settings in the ArcGIS Online GUI, then run the `build_template()` function to record the changes for later use.  The following table lists the name and description for each of the current template maps, and clicking on the name of the map will open the corresponding template in ArcGIS Online:

+------------------------------+----------------------------------------------------------------+
|Name                          |Description                                                     |
+==============================+================================================================+
|template_address_map_         | Addresses for County and City of Corvallis.                    |
+------------------------------+----------------------------------------------------------------+
|template_aerial_imagery_map_  | County and ESRI high resolution orthography.                   |
+------------------------------+----------------------------------------------------------------+
|template_contours_map_        | Topographic contour layers.                                    |
+------------------------------+----------------------------------------------------------------+
|template_environment_map_     | General water, soils and wetlands layers.                      |
+------------------------------+----------------------------------------------------------------+
|template_hpc_butterfly_map_   | Fender Blue Butterfly layers.                                  |
+------------------------------+----------------------------------------------------------------+
|template_hpsv_map_            | High protection significant vegetation from Corvallis NFI.     |
+------------------------------+----------------------------------------------------------------+
|template_nfi_features_map_    | Oak Savanna, Critical-Systems Wetlands and DNI Wetland layers. |
+------------------------------+----------------------------------------------------------------+
|template_nfi_flood_map_       | Flooding layers from Corvallis NFI hazards.                    |
+------------------------------+----------------------------------------------------------------+
|template_ppsv_map_            | Partial protection significant vegetation from Corvallis NFI.  |
+------------------------------+----------------------------------------------------------------+
|template_riparian_map_        | Riparian buffers from the Corvallis NFI.                       |
+------------------------------+----------------------------------------------------------------+
|template_taxlot_map_          | Layers from the Benton County taxlot service.                  |
+------------------------------+----------------------------------------------------------------+

.. _template_address_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=5c507b0f03084f33b8da587cbd4b830b
.. _template_aerial_imagery_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=4cb460dcb6464724b2e99ba696d5dd77
.. _template_contours_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=1e0e9975687741a897e2ff4c7dd3b8e0
.. _template_environment_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=a2612a21ccf3458e945ac971390cf5dc
.. _template_hpc_butterfly_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=6f3467fcdeea4d839d01bff403a5e891
.. _template_hpsv_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=d9b5d23af3044405afe06e8d488d8b64
.. _template_nfi_features_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=4b01743efdb94a3fa54e0f542aad987a
.. _template_nfi_flood_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=ee08f36f69b24f2599bea34563215a17
.. _template_ppsv_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=a0e7e1cb85c54fd39b95eed20d1aded9
.. _template_riparian_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=dbeaf45e240a41178879f64751d6954d
.. _template_taxlot_map: https://bentoncountygis.maps.arcgis.com/home/item.html?id=a409c55c9e0440488c4ab3ce5e10659d
