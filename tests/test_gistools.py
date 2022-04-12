"""Tests for bentoncounty_gistools package."""
from arcgis.gis import GIS
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap
from bentoncounty_gistools import bentoncounty_gistools as bc
import os
import pytest
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
    PYTEST_SKIP, reason="Resource intensive. Test copies are persistent."
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
    test_group = bc.group_layer("test")
    test_keys = ["id", "layers", "layerType", "title", "disablePopup"]
    # dictionary has appropriate fields
    for key in test_group.keys():
        assert key in test_keys
    # title is set as specified
    assert test_group["title"] == "test"
