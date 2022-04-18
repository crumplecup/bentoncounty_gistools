"""Tests for bentoncounty_gistools package."""
from arcgis.gis import GIS
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import WebMap
from bentoncounty_gistools import bentoncounty_gistools as bc
import os
import pytest
import json
import random
from dotenv import load_dotenv

load_dotenv()
ARCGIS_USERNAME = os.getenv("ARCGIS_USERNAME")
ARCGIS_PASSWORD = os.getenv("ARCGIS_PASSWORD")
PYTEST_SKIP = os.getenv("PYTEST_SKIP")
TEMPLATE_DIR = os.getenv("TEMPLATE_DIR")


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_build_template_dictionary():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    addr_ref = gis.content.search("test_address_template_bc")[0]
    bnd_ref = gis.content.search("test_boundaries_template_bc")[0]
    nat_ref = gis.content.search("test_natural_layers_template_bc")[0]
    nfi_ref = gis.content.search("nfi_template")[0]
    srv_ref = gis.content.search("test_survey_template_bc")[0]

    template_dict = {}

    template_dict.update(bc.build_template_dictionary("address", addr_ref))
    template_dict.update(bc.build_template_dictionary("boundary", bnd_ref))
    template_dict.update(bc.build_template_dictionary("natural", nat_ref))
    template_dict.update(bc.build_template_dictionary("nfi", nfi_ref))
    template_dict.update(bc.build_template_dictionary("survey", srv_ref))
    dict_keys = list(template_dict.keys())
    file_name = os.path.join(TEMPLATE_DIR, "template.json")
    with open(file_name, "w") as fp:
        json.dump(template_dict, fp, sort_keys=True, indent=4)
    assert dict_keys[0] == "driveways"
    assert dict_keys[4] == "parks_popup"


# load template after making
template_name = "template.json"
file_name = os.path.join(TEMPLATE_DIR, template_name)
with open(file_name) as json_file:
    template = json.load(json_file)


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


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
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
    bc.county_basemap(test_item, template)


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
    bc.county_boundaries(test_group, template)
    assert test_group["layers"][0]["title"] == "Boundaries"


def test_tranport_layers():
    test_group = bc.group_layer("test")
    bc.transport_layers(test_group)
    assert test_group["layers"][0]["title"] == "Transportation"


def test_survey_layers():
    test_group = bc.group_layer("test")
    bc.survey_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Survey"


def test_taxlot_layers():
    test_group = bc.group_layer("test")
    bc.taxlot_layers(test_group)
    assert test_group["layers"][0]["title"] == "Taxlot"


def test_address_layers():
    test_group = bc.group_layer("test")
    bc.address_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Address"


def test_natural_layers():
    test_group = bc.group_layer("test")
    bc.natural_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "WATER|SOILS|WETLANDS"


def test_zoning_layers():
    test_group = bc.group_layer("test")
    bc.zoning_layers(test_group)
    assert test_group["layers"][0]["title"] == "Zoning"


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_address_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # build template
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_address_template"})
    # item_props.update(
    #     {
    #         "description": "Reference web map for common address layers for community development planners. Reference layer for testing. Do not use or modify."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    # item_props.update({"tags": ["community development", "test", "address"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props)

    # build test map
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_address_map"})
    # item_props.update(
    #     {
    #         "description": "Test web map for common address layers for community development planners. Overwritten during testing. Do not use."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use."})
    # item_props.update({"tags": ["community development", "test", "address"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props)
    test_item = gis.content.search("test_address_map")[0]
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.address_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_county_boundaries_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # build template
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_boundaries_template_bc"})
    # item_props.update(
    #     {
    #         "description": "Reference web map of boundary layers for community development planners. Reference layer for testing. Do not use or modify."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    # item_props.update({"tags": ["community development", "test", "boundaries"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props)

    # build test map
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_county_boundaries_map"})
    # item_props.update(
    #     {
    #         "description": "Test web map of boundary layers for community development planners. Overwritten during testing. Do not use."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use."})
    # item_props.update({"tags": ["community development", "test", "boundary"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props)
    test_item = gis.content.search("test_county_boundaries_map")[0]
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.county_boundaries, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_natural_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # build template
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_natural_layers_template_bc"})
    # item_props.update(
    #     {
    #         "description": "Reference web map of water, soil and wetland layers for community development planners. Reference layer for testing. Do not use or modify."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    # item_props.update({"tags": ["community development", "test", "natural features"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props)

    # build test map
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_natural_layers_map"})
    # item_props.update(
    #     {
    #         "description": "Test web map of water, soil and wetland layers for community development planners. Overwritten during testing. Do not use."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use."})
    # item_props.update({"tags": ["community development", "test", "natural features"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="tests")
    test_item = gis.content.search("test_natural_layers_map")[0]
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.natural_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_survey_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # build template
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_survey_template_bc"})
    # item_props.update(
    #     {
    #         "description": "Reference web map of survey layers for testing. Do not use or modify."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    # item_props.update({"tags": ["community development", "test", "survey"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="templates")

    # build test map
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_survey_map"})
    # item_props.update(
    #     {
    #         "description": "Test web map of survey layers for community development planners. Overwritten during testing. Do not use."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use."})
    # item_props.update({"tags": ["community development", "test", "survey"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="tests")
    test_item = gis.content.search("test_survey_map")[0]
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.survey_layers, template)
