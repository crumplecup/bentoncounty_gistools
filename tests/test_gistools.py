"""Tests for bentoncounty_gistools package."""
from arcgis.gis import GIS
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap
from bentoncounty_gistools import bentoncounty_gistools as bc
import os
import pytest
import random
from dotenv import load_dotenv

load_dotenv()
ARCGIS_USERNAME = os.getenv("ARCGIS_USERNAME")
ARCGIS_PASSWORD = os.getenv("ARCGIS_PASSWORD")
PYTEST_SKIP = os.getenv("PYTEST_SKIP")


def test_layer_urls():
    """Produces a list of urls from a service."""
    gis = GIS()
    # load natural features inventory feature collection service
    nfi_fs = gis.content.search(
        "NaturalFeaturesInventoryService2022_DRAFT",
        item_type="Feature Layer Collection",
    )[0]
    urls = bc.layer_urls(nfi_fs)
    assert (
        urls[0]
        == "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/0"
    )
    assert (
        urls[1]
        == "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/3"
    )


def test_fc_gen():
    """Produces feature class data format."""
    gis = GIS()
    # load natural features inventory feature collection service
    nfi_fs = gis.content.search(
        "NaturalFeaturesInventoryService2022_DRAFT",
        item_type="Feature Layer Collection",
    )[0]
    urls = bc.layer_urls(nfi_fs)
    streams = MapServiceLayer(urls[0])
    stream = bc.fc_gen(streams)
    assert (
        stream["url"]
        == "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/0"
    )
    assert stream["title"] == "STREAMS"
    assert stream["layerType"] == "ArcGISFeatureLayer"


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_add_nfi():
    """Adds NFI layers to web map."""
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # load natural features inventory feature collection service
    nfi_fs = gis.content.search(
        "NaturalFeaturesInventoryService2022_DRAFT",
        item_type="Feature Layer Collection",
    )[0]
    # load designated web map for unit testing
    nfi_template = gis.content.search("nfi_template")[0]
    nfi_map = gis.content.search("nfi_test_map")[0]
    nfi_test = WebMap(nfi_map)
    test_layers = nfi_test.layers
    # delete current content of test map
    for lyr in test_layers:
        nfi_test.remove_layer(lyr)
    nfi_test.update()
    # add nfi layers
    bc.add_nfi(nfi_map, nfi_fs, nfi_template)


def test_group_layer():
    group_lyr = bc.group_layer("test")
    assert group_lyr["layerType"] == "GroupLayer"
    assert group_lyr["title"] == "test"


# @pytest.mark.skipif(
#     PYTEST_SKIP,
#     reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
# )
def test_county_basemap():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_county_basemap"})
    # item_props.update(
    #     {
    #         "description": "Test web map for common reference layers for community development planners. Overwritten during tests. Do not use."
    #     }
    #  )
    #  item_props.update({"snippet": "For testing purposes. Do not use."})
    #  item_props.update({"tags": ["community development", "test"]})
    #  item_props.update(
    #      {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    #  )
    #  wm.save(item_props)
    test_item = gis.content.search("test_county_basemap")[0]
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.county_basemap(test_item)


def test_county_basemap_layers():
    test_group = bc.group_layer("test")
    bc.county_basemap_layers(test_group)
    assert test_group["layers"][4]["title"] == "Section Numbers"
    assert test_group["layers"][3]["title"] == "Sectionlines"
    assert test_group["layers"][2]["title"] == "Railroads"
    assert test_group["layers"][1]["title"] == "Roads"
    assert test_group["layers"][0]["title"] == "TaxlotOwners"


def test_county_boundaries():
    test_group = bc.group_layer("test")
    bc.county_boundaries(test_group)
    assert test_group["layers"][0]["title"] == "Boundaries"
