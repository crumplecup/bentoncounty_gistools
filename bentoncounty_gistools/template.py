from arcgis.gis import GIS
from bentoncounty_gistools import bentoncounty_gistools as bc
import os
import json
from dotenv import load_dotenv

# load user name, password and template directory from .env
load_dotenv()
ARCGIS_USERNAME = os.getenv("ARCGIS_USERNAME")
ARCGIS_PASSWORD = os.getenv("ARCGIS_PASSWORD")
TEMPLATE_DIR = os.getenv("TEMPLATE_DIR")

# map ids for template maps
TEMPLATE_AERIAL_IMAGERY_MAP = "4cb460dcb6464724b2e99ba696d5dd77"
TEMPLATE_ADDRESS_MAP = "5c507b0f03084f33b8da587cbd4b830b"
TEMPLATE_ANNO_0020_MAP = "47679a569cd9421d806e981fffa49b72"
TEMPLATE_ANNO_0050_MAP = "e6ad704ebb53408f8e111d1ace1c45b9"
TEMPLATE_BOUNDARIES_MAP = "c8595e39c1fe4971819d74e7318d1dbd"
TEMPLATE_CONTOURS_MAP = "1e0e9975687741a897e2ff4c7dd3b8e0"
TEMPLATE_CORVALLIS_IMAGERY = "8dea2f0d5c604fa5ba9e231a7a462bbb"
TEMPLATE_ENVIRONMENT_MAP = "a2612a21ccf3458e945ac971390cf5dc"
TEMPLATE_HCP_BUTTERFY_MAP = "6f3467fcdeea4d839d01bff403a5e891"
TEMPLATE_HPSV_MAP = "d9b5d23af3044405afe06e8d488d8b64"
TEMPLATE_FEMA_NFHL = "80f8d00a788743458e344f1e94ddf8c5"
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


def build_template():
    """
    Build template dictionary from template maps.  The template stores layer
    definition information (style, labels, whether popups are enabled, etc.)
    referenced by the package when constructing a new map.

    :return: Updates the template.json file.
    """
    gis = GIS(
        "https://bentoncountygis.maps.arcgis.com/", ARCGIS_USERNAME, ARCGIS_PASSWORD
    )
    address_map = gis.content.get(TEMPLATE_ADDRESS_MAP)
    boundary_map = gis.content.get(TEMPLATE_BOUNDARIES_MAP)
    contour_map = gis.content.get(TEMPLATE_CONTOURS_MAP)
    environment_map = gis.content.get(TEMPLATE_ENVIRONMENT_MAP)
    hcp_map = gis.content.get(TEMPLATE_HCP_BUTTERFY_MAP)
    hpsv_map = gis.content.get(TEMPLATE_HPSV_MAP)
    nfi_features_map = gis.content.get(TEMPLATE_NFI_FEATURES_MAP)
    nfi_flood_map = gis.content.get(TEMPLATE_NFI_FLOOD_MAP)
    nfi_hazard_map = gis.content.get(TEMPLATE_NFI_HAZARD_MAP)
    ppsv_map = gis.content.get(TEMPLATE_PPSV_MAP)
    riparian_map = gis.content.get(TEMPLATE_RIPARIAN_MAP)
    survey_map = gis.content.get(TEMPLATE_SURVEY_MAP)
    taxlot_map = gis.content.get(TEMPLATE_TAXLOT_MAP)
    transport_map = gis.content.get(TEMPLATE_TRANSPORTATION_MAP)
    zoning_map = gis.content.get(TEMPLATE_ZONING_MAP)

    template = {}

    template.update(bc.build_template_dictionary("address", address_map))
    template.update(bc.build_template_dictionary("boundary", boundary_map))
    template.update(bc.build_template_dictionary("contour", contour_map))
    template.update(bc.build_template_dictionary("environment", environment_map))
    template.update(bc.build_template_dictionary("hcp", hcp_map))
    template.update(bc.build_template_dictionary("hpsv", hpsv_map))
    template.update(bc.build_template_dictionary("nfi_features", nfi_features_map))
    template.update(bc.build_template_dictionary("nfi_flood", nfi_flood_map))
    template.update(bc.build_template_dictionary("nfi_hazard", nfi_hazard_map))
    template.update(bc.build_template_dictionary("ppsv", ppsv_map))
    template.update(bc.build_template_dictionary("riparian", riparian_map))
    template.update(bc.build_template_dictionary("survey", survey_map))
    template.update(bc.build_template_dictionary("taxlot", taxlot_map))
    template.update(bc.build_template_dictionary("transport", transport_map))
    template.update(bc.build_template_dictionary("zoning", zoning_map))
    file_name = os.path.join(TEMPLATE_DIR, "template.json")
    with open(file_name, "w") as fp:
        json.dump(template, fp, sort_keys=True, indent=4)
