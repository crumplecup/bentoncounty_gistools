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
PYTEST_CREATE = os.getenv("PYTEST_CREATE")
TEMPLATE_DIR = os.getenv("TEMPLATE_DIR")

TEST_ADDRESS_MAP = "a08fb19797cb4e61b1536fbc4961cce6"
TEST_ANNO_0020_MAP = "63d113c5b06940bd9acd82eaa740ff31"
TEST_ANNO_0050_MAP = "39be32a0a607428cb19affee732c64f9"
TEST_BOUNDARIES_MAP = "3c1a1c04eeb2404380365b00d7d2ecb6"
TEST_CONTOURS_MAP = "0b7ae5ebff5f4859b6c4696b556ebb47"
TEST_COUNTY_BASEMAP = "50ef97f3f25742fe9f8954948ad18b63"
TEST_ENVIRONMENT_MAP = "313f8d220cbe4c40b052a69c942e9bcc"
TEST_HCP_BUTTERFY_MAP = "9cd23c96be10410ba85c1c9329bd292d"
TEST_HPSV_MAP = "6c2e1b71533d4755a0b455fef2264fd6"
TEST_NATURAL_LAYERS_MAP = "9b3770d8ef684e529690f3956cc19e1a"
TEST_NFI_FEATURES_MAP = "d2608a049bed4d4b8b29c87608110137"
TEST_NFI_FLOOD_MAP = "23020f6d205c4e27bd28ae183adef5a7"
TEST_NFI_HAZARD_MAP = "692cf8d0949b40e380decdc2b7ad3b54"
TEST_NFI_MAP = "df21a6eb07ea439c80092ddcb2cf7108"
TEST_PPSV_MAP = "2a2bd64af0c747cdafcacf54f94c6e65"
TEST_RIPARIAN_MAP = "6dc956a2be7847b5a031df1973245f96"
TEST_SURVEY_MAP = "7ff1b1363e204b0396f56c6270c1bfbc"
TEST_TAXLOT_MAP = "c98a7f2f24974e09ac1a44017aa5774a"
TEST_TRANSPORTATION_MAP = "cb212d30a70a468d850a83eb4cc6bc08"
TEST_ZONING_MAP = "224f58c8813840da82b59cf3f8a58678"

TEMPLATE_ADDRESS_MAP = "5c507b0f03084f33b8da587cbd4b830b"
TEMPLATE_ANNO_0020_MAP = "47679a569cd9421d806e981fffa49b72"
TEMPLATE_ANNO_0050_MAP = "e6ad704ebb53408f8e111d1ace1c45b9"
TEMPLATE_BOUNDARIES_MAP = "c8595e39c1fe4971819d74e7318d1dbd"
TEMPLATE_CONTOURS_MAP = "1e0e9975687741a897e2ff4c7dd3b8e0"
TEMPLATE_ENVIRONMENT_MAP = "a2612a21ccf3458e945ac971390cf5dc"
TEMPLATE_HCP_BUTTERFY_MAP = "6f3467fcdeea4d839d01bff403a5e891"
TEMPLATE_HPSV_MAP = "d9b5d23af3044405afe06e8d488d8b64"
TEMPLATE_NATURAL_LAYERS_MAP = "c172db7be269462f8f1d1e08e9ecc1db"
TEMPLATE_NFI_FEATURES_MAP = "4b01743efdb94a3fa54e0f542aad987a"
TEMPLATE_NFI_FLOOD_MAP = "ee08f36f69b24f2599bea34563215a17"
TEMPLATE_NFI_HAZARD_MAP = "9db5a09c12454347871a522f6af851d8"
TEMPLATE_NFI_MAP = "c0c19fcc00e9430bb92332e35e19aa13"
TEMPLATE_PPSV_MAP = "a0e7e1cb85c54fd39b95eed20d1aded9"
TEMPLATE_RIPARIAN_MAP = "dbeaf45e240a41178879f64751d6954d"
TEMPLATE_SURVEY_MAP = "28cbe6fcdc7c49cba8f95666644b7fda"
TEMPLATE_TAXLOT_MAP = "a409c55c9e0440488c4ab3ce5e10659d"
TEMPLATE_TRANSPORTATION_MAP = "8cd34cff9a43406dae69c69fa42829b9"
TEMPLATE_ZONING_MAP = "1f417e7ca2c54a8e99ffb7b373c3c229"


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Only build dictionary when templates have changed.",
)
def test_build_template_dictionary():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    address_map = gis.content.get(TEMPLATE_ADDRESS_MAP)
    boundary_map = gis.content.get(TEMPLATE_BOUNDARIES_MAP)
    contour_map = gis.content.get(TEMPLATE_CONTOURS_MAP)
    environment_map = gis.content.get(TEMPLATE_ENVIRONMENT_MAP)
    hcp_map = gis.content.get(TEMPLATE_HCP_BUTTERFY_MAP)
    hpsv_map = gis.content.get(TEMPLATE_HPSV_MAP)
    natural_map = gis.content.get(TEMPLATE_NATURAL_LAYERS_MAP)
    nfi_features_map = gis.content.get(TEMPLATE_NFI_FEATURES_MAP)
    nfi_flood_map = gis.content.get(TEMPLATE_NFI_FLOOD_MAP)
    nfi_hazard_map = gis.content.get(TEMPLATE_NFI_HAZARD_MAP)
    nfi_map = gis.content.get(TEMPLATE_NFI_MAP)
    ppsv_map = gis.content.get(TEMPLATE_PPSV_MAP)
    riparian_map = gis.content.get(TEMPLATE_RIPARIAN_MAP)
    survey_map = gis.content.get(TEMPLATE_SURVEY_MAP)
    taxlot_map = gis.content.get(TEMPLATE_TAXLOT_MAP)
    transport_map = gis.content.get(TEMPLATE_TRANSPORTATION_MAP)
    zoning_map = gis.content.get(TEMPLATE_ZONING_MAP)

    template_dict = {}

    template_dict.update(bc.build_template_dictionary("address", address_map))
    template_dict.update(bc.build_template_dictionary("boundary", boundary_map))
    template_dict.update(bc.build_template_dictionary("contour", contour_map))
    template_dict.update(bc.build_template_dictionary("environment", environment_map))
    template_dict.update(bc.build_template_dictionary("hcp", hcp_map))
    template_dict.update(bc.build_template_dictionary("hpsv", hpsv_map))
    template_dict.update(bc.build_template_dictionary("natural", natural_map))
    template_dict.update(bc.build_template_dictionary("nfi_features", nfi_features_map))
    template_dict.update(bc.build_template_dictionary("nfi_flood", nfi_flood_map))
    template_dict.update(bc.build_template_dictionary("nfi_hazard", nfi_hazard_map))
    template_dict.update(bc.build_template_dictionary("nfi", nfi_map))
    template_dict.update(bc.build_template_dictionary("ppsv", ppsv_map))
    template_dict.update(bc.build_template_dictionary("riparian", riparian_map))
    template_dict.update(bc.build_template_dictionary("survey", survey_map))
    template_dict.update(bc.build_template_dictionary("taxlot", taxlot_map))
    template_dict.update(bc.build_template_dictionary("transport", transport_map))
    template_dict.update(bc.build_template_dictionary("zoning", zoning_map))
    dict_keys = list(template_dict.keys())
    file_name = os.path.join(TEMPLATE_DIR, "template.json")
    with open(file_name, "w") as fp:
        json.dump(template_dict, fp, sort_keys=True, indent=4)
    assert dict_keys[0] == "address_buildings_popup"


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
    test_item = gis.content.get(TEST_COUNTY_BASEMAP)
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.county_basemap(test_item, template)


def test_county_boundaries():
    test_group = bc.group_layer("test")
    bc.county_boundaries(test_group, template)
    assert test_group["layers"][0]["title"] == "Boundaries"


def test_tranport_layers():
    test_group = bc.group_layer("test")
    bc.transport_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Transportation"


def test_survey_layers():
    test_group = bc.group_layer("test")
    bc.survey_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Survey"


def test_taxlot_layers():
    test_group = bc.group_layer("test")
    bc.taxlot_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Taxlot Maps"


def test_address_layers():
    test_group = bc.group_layer("test")
    bc.address_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Addresses"


def test_hpsv_layers():
    test_group = bc.group_layer("test")
    bc.hpsv_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "High Protection"
    # assert test_group["layers"][0].keys() == ["foo", "bar"]


def test_natural_layers():
    test_group = bc.group_layer("test")
    bc.natural_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "WATER|SOILS|WETLANDS"


def test_zoning_layers():
    test_group = bc.group_layer("test")
    bc.zoning_layers(test_group, template)
    assert test_group["layers"][0]["title"] == "Zoning"


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_address_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    test_item = gis.content.get(TEST_ADDRESS_MAP)
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
def test_boundaries_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    test_item = gis.content.get(TEST_BOUNDARIES_MAP)
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
    test_item = gis.content.get(TEST_NATURAL_LAYERS_MAP)
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
    test_item = gis.content.get(TEST_SURVEY_MAP)
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.survey_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_transport_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    test_item = gis.content.get(TEST_TRANSPORTATION_MAP)
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.transport_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_zoning_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_ZONING_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.zoning_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_anno_0020_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEMPLATE_ANNO_0020_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.anno_0020_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_anno_0050_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # build template
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "template_anno_0050_map"})
    # item_props.update(
    #     {
    #         "description": "Reference web map of taxlot anno 0050 layers for testing. Do not use or modify."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    # item_props.update(
    #     {"tags": ["community development", "template", "test", "taxlot", "anno"]}
    # )
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="templates")

    # build test map
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_anno_0050_map"})
    # item_props.update(
    #     {
    #         "description": "Test web map of taxlot anno 0050 layers for community development planners. Overwritten during testing. Do not use."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use."})
    # item_props.update({"tags": ["community development", "test", "taxlot", "anno"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="tests")

    # overwrite test map with new layers
    test_item = gis.content.get(TEST_ANNO_0050_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    # test_map = WebMap(test_item)
    # test_layers = test_map.layers
    # for lyr in test_layers:
    #     test_map.remove_layer(lyr)
    # test_map.update()
    bc.test_map_layers(test_item, bc.anno_0050_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_taxlot_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_TAXLOT_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.taxlot_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_hpsv_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_HPSV_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.hpsv_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_ppsv_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_PPSV_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.ppsv_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_riparian_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )

    # build template
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "template_riparian_map"})
    # item_props.update(
    #     {
    #         "description": "Reference web map of riparian areas layers for testing. Do not use or modify."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    # item_props.update(
    #     {"tags": ["community development", "template", "test", "natural features"]}
    # )
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="templates")

    # build test map
    # wm = WebMap()
    # item_props = {}
    # item_props.update({"title": "test_riparian_map"})
    # item_props.update(
    #     {
    #         "description": "Test web map of riparian areas layers for community development planners. Overwritten during testing. Do not use."
    #     }
    # )
    # item_props.update({"snippet": "For testing purposes. Do not use."})
    # item_props.update({"tags": ["community development", "test", "natural features"]})
    # item_props.update(
    #     {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    # )
    # wm.save(item_props, folder="tests")

    # overwrite test map with new layers
    test_item = gis.content.get(TEST_RIPARIAN_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.riparian_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_nfi_features_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_NFI_FEATURES_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.nfi_features_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_nfi_flood_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_NFI_FLOOD_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.nfi_flood_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_nfi_hazard_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_NFI_HAZARD_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.nfi_hazard_layers, template)


@pytest.mark.skipif(
    not PYTEST_CREATE,
    reason="Creates new files on the ArcGIS server.  Only run to instantiate new tests.",
)
def test_new():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # build template
    wm = WebMap()
    item_props = {}
    item_props.update({"title": "template_environment_map"})
    item_props.update(
        {
            "description": "Reference web map of environment layers for testing. Do not use or modify."
        }
    )
    item_props.update({"snippet": "For testing purposes. Do not use or modify."})
    item_props.update(
        {
            "tags": [
                "community development",
                "template",
                "test",
                "environment",
            ]
        }
    )
    item_props.update(
        {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    )
    wm.save(item_props, folder="templates")

    # build test map
    wm = WebMap()
    item_props = {}
    item_props.update({"title": "test_environment_map"})
    item_props.update(
        {
            "description": "Test web map of environment layers for community development planners. Overwritten during testing. Do not use."
        }
    )
    item_props.update({"snippet": "For testing purposes. Do not use."})
    item_props.update({"tags": ["community development", "test", "environment"]})
    item_props.update(
        {"serviceItemId": bc.create_layer_id(random.randint(10000, 99999))}
    )
    wm.save(item_props, folder="tests")


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_contour_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_CONTOURS_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.contour_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_hcp_butterfly_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_HCP_BUTTERFY_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.hcp_butterfly_layers, template)


@pytest.mark.skipif(
    PYTEST_SKIP,
    reason="Resource intensive. Test copies overwrite test files on the server, consuming county credit on the ArcGIS server.",
)
def test_environment_map():
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    # overwrite test map with new layers
    test_item = gis.content.get(TEST_ENVIRONMENT_MAP)

    # comment out if new map (no layers yet)
    # todo: add logical check for layers
    test_map = WebMap(test_item)
    test_layers = test_map.layers
    for lyr in test_layers:
        test_map.remove_layer(lyr)
    test_map.update()
    bc.test_map_layers(test_item, bc.environment_layers, template)
