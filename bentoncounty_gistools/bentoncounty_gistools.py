import random
import string
from arcgis.mapping import MapServiceLayer

ZONING_UGB_CORVALLIS_URL = "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/zoning_service_test/FeatureServer/0"
ZONING_UGB_PHILOMATH_URL = "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/zoning_service_test/FeatureServer/2"
ZONING_URL = "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/zoning_service_test/FeatureServer/3"
ZONING_AIRPORT_URL = "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/zoning_service_test/FeatureServer/5"
ZONING_FEMA_FLOODPLAIN_URL = "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/zoning_service_test/FeatureServer/4"

BC_TAXLOTS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TaxlotOwners/FeatureServer/0"
BC_ROADS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/FeatureServer/3"
BC_RAILROADS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/FeatureServer/4"
BC_SECTION_LINES = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/5"
BC_SECTION_NUMBERS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/3"
BC_BOUNDARIES = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer"
)
BC_TRANSPORTATION = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/MapServer"
BC_TAXLOT_MAP = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/TaxlotService/MapServer"
)
BC_ADDRESS_CORVALLIS = (
    "https://gis.corvallisoregon.gov/pub2/rest/services/Base/CorvallisAddress/MapServer"
)
BC_ADDRESS_COUNTY = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/AddressService/MapServer"
)
FEMA_FLOOD_HAZARDS = (
    "https://hazards.fema.gov/gis/nfhl/rest/services/public/NFHL/MapServer"
)
BC_ZONING_COMPLIANCE = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/ZoningCompliance/MapServer"
)
BC_WATER_SOILS_WETLANDS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/NaturalService/MapServer"
)
BC_BOUNDARIES_CITIES = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/0"
)
BC_BOUNDARIES_COUNTY = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/1"
)
BC_BOUNDARIES_PRECINCTS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/2"
)
BC_BOUNDARIES_PARKS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/3"
)
BC_BOUNDARIES_ZIP_CODES = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/4"
)
BC_BOUNDARIES_SCHOOL = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/5"
)
BC_BOUNDARIES_FIRE = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/6"
)
BC_BOUNDARIES_ALL_DISTRICTS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/Boundaries/MapServer/7"
)

TRANSPORTATION_ROAD_NAMES = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/MapServer/0"
TRANSPORTATION_ROAD_SURFACE = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/MapServer/1"
TRANSPORTATION_CENTERLINES = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/MapServer/2"
TRANSPORTATION_ROADS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/MapServer/3"
TRANSPORTATION_RAILROADS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/TransportationService/MapServer/4"

SURVEY_BENCHMARKS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/0"
SURVEY_DLC_CORNERS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/1"
SURVEY_GEODETIC_CONTROL = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/2"
SURVEY_SECTION_NUMBERS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/3"
SURVEY_SECTION_CORNERS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/4"
SURVEY_SECTION_LINES = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/5"
SURVEY_SECTION_POLYGONS = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/6"
SURVEY_DLC = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/7"
SURVEY_INDEX = "https://gis.co.benton.or.us/arcgis/rest/services/Public/SurveyService/FeatureServer/8"

TAXLOT_ANNO_0020_SCALE = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/TaxlotService/MapServer/0"
)
TAXLOT_ANNO_0050_SCALE = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/TaxlotService/MapServer/38"
)

ADDRESS_COUNTY = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/AddressService/MapServer/0"
)
ADDRESS_BUILDINGS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/AddressService/MapServer/1"
)
ADDRESS_DRIVEWAYS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/AddressService/MapServer/2"
)

NATURAL_HYDRO_HUCS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/NaturalService/MapServer/0"
)
NATURAL_HYDRO_POLYS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/NaturalService/MapServer/1"
)
NATURAL_HYDRO_LINES = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/NaturalService/MapServer/2"
)
NATURAL_SOILS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/NaturalService/MapServer/3"
)
NATURAL_WETLANDS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/NaturalService/MapServer/5"
)

# current zoning service
BC_ZONING_UGB = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/ZoningService/MapServer/0"
)
BC_WILLAMETTE_GREENWAY = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/ZoningService/MapServer/1"
)
BC_ZONING_OVERLAYS = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/ZoningService/MapServer/3"
)
BC_ZONING_AIRPORT = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/ZoningService/MapServer/4"
)
BC_ZONING_CURRENT = (
    "https://gis.co.benton.or.us/arcgis/rest/services/Public/ZoningService/MapServer/5"
)


def zoning_layers(group_lyr):
    bc_zoning_ugb = MapServiceLayer(BC_ZONING_UGB)
    bc_willamette_greenway = MapServiceLayer(BC_WILLAMETTE_GREENWAY)
    bc_zoning_overlays = MapServiceLayer(BC_ZONING_OVERLAYS)
    bc_zoning_airport = MapServiceLayer(BC_ZONING_AIRPORT)
    bc_zoning_current = MapServiceLayer(BC_ZONING_CURRENT)

    bc_zoning_ugb_fc = feature_class(bc_zoning_ugb)
    bc_willamette_greenway_fc = feature_class(bc_willamette_greenway, 0.4)
    bc_zoning_overlays_fc = feature_class(bc_zoning_overlays, 0.4)
    bc_zoning_airport_fc = feature_class(bc_zoning_airport, 0.4)
    bc_zoning_current_fc = feature_class(bc_zoning_current, 0.4)

    zoning_group = group_layer("Zoning")
    zoning_group["layers"].append(bc_zoning_current_fc)
    zoning_group["layers"].append(bc_zoning_airport_fc)
    zoning_group["layers"].append(bc_zoning_overlays_fc)
    zoning_group["layers"].append(bc_willamette_greenway_fc)
    zoning_group["layers"].append(bc_zoning_ugb_fc)

    group_lyr["layers"].append(zoning_group)


def natural_layers(group_lyr):
    natural_hydro_hucs = MapServiceLayer(NATURAL_HYDRO_HUCS)
    natural_hydro_polys = MapServiceLayer(NATURAL_HYDRO_POLYS)
    natural_hydro_lines = MapServiceLayer(NATURAL_HYDRO_LINES)
    natural_soils = MapServiceLayer(NATURAL_SOILS)
    natural_wetlands = MapServiceLayer(NATURAL_WETLANDS)

    natural_hydro_hucs_fc = feature_class(natural_hydro_hucs)
    natural_hydro_hucs_fc.update({"visibility": False})
    natural_hydro_polys_fc = feature_class(natural_hydro_polys)
    natural_hydro_lines_fc = feature_class(natural_hydro_lines)
    natural_soils_fc = feature_class(natural_soils)
    natural_soils_fc.update({"visibility": False})
    natural_wetlands_fc = feature_class(natural_wetlands)
    natural_wetlands_fc.update({"visibility": False})

    natural_group = group_layer("WATER|SOILS|WETLANDS")
    natural_group["layers"].append(natural_wetlands_fc)
    natural_group["layers"].append(natural_soils_fc)
    natural_group["layers"].append(natural_hydro_lines_fc)
    natural_group["layers"].append(natural_hydro_polys_fc)
    natural_group["layers"].append(natural_hydro_hucs_fc)

    group_lyr["layers"].append(natural_group)


def address_map(project_map, template):
    basemap = group_layer("Base")
    address_layers(basemap, template)
    map_def = project_map.get_data()
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})


def address_layers(group_lyr, template):
    address_county = MapServiceLayer(ADDRESS_COUNTY)
    address_buildings = MapServiceLayer(ADDRESS_BUILDINGS)
    address_driveways = MapServiceLayer(ADDRESS_DRIVEWAYS)
    popup_info = addr_popup_info(template)
    labels = addr_labels(template)

    address_county_fc = feature_class(address_county)
    address_county_fc.update({"popupInfo": popup_info["address"]})
    address_county_fc.update({"layerDefinition": labels["labels"]})
    address_buildings_fc = feature_class(address_buildings)
    address_buildings_fc.update({"visibility": False})
    address_driveways_fc = feature_class(address_driveways)
    address_driveways_fc.update({"visibility": False})
    address_driveways_fc.update({"popupInfo": popup_info["driveways"]})

    address_group = group_layer("Address")
    address_group["layers"].append(address_buildings_fc)
    address_group["layers"].append(address_driveways_fc)
    address_group["layers"].append(address_county_fc)

    group_lyr["layers"].append(address_group)


def taxlot_layers(group_lyr):
    taxlot_anno_0020_scale = MapServiceLayer(TAXLOT_ANNO_0020_SCALE)
    taxlot_anno_0050_scale = MapServiceLayer(TAXLOT_ANNO_0050_SCALE)
    taxlot_anno_0020_scale_fc = feature_class(taxlot_anno_0020_scale)
    taxlot_anno_0020_scale_fc.update({"visibility": False})
    taxlot_anno_0050_scale_fc = feature_class(taxlot_anno_0050_scale)
    taxlot_anno_0050_scale_fc.update({"visibility": False})

    taxlot_group = group_layer("Taxlot")
    taxlot_group["layers"].append(taxlot_anno_0050_scale_fc)
    taxlot_group["layers"].append(taxlot_anno_0020_scale_fc)

    group_lyr["layers"].append(taxlot_group)


def survey_layers(group_lyr):
    survey_benchmarks = MapServiceLayer(SURVEY_BENCHMARKS)
    survey_dlc_corners = MapServiceLayer(SURVEY_DLC_CORNERS)
    survey_geodetic_control = MapServiceLayer(SURVEY_GEODETIC_CONTROL)
    survey_section_numbers = MapServiceLayer(SURVEY_SECTION_NUMBERS)
    survey_section_corners = MapServiceLayer(SURVEY_SECTION_CORNERS)
    survey_section_lines = MapServiceLayer(SURVEY_SECTION_LINES)
    survey_section_polygons = MapServiceLayer(SURVEY_SECTION_POLYGONS)
    survey_dlc = MapServiceLayer(SURVEY_DLC)
    survey_index = MapServiceLayer(SURVEY_INDEX)

    survey_benchmarks_fc = feature_class(survey_benchmarks)
    survey_benchmarks_fc.update({"visibility": False})
    survey_dlc_corners_fc = feature_class(survey_dlc_corners)
    survey_dlc_corners_fc.update({"visibility": False})
    survey_geodetic_control_fc = feature_class(survey_geodetic_control)
    survey_geodetic_control_fc.update({"visibility": False})
    survey_section_numbers_fc = feature_class(survey_section_numbers)
    survey_section_corners_fc = feature_class(survey_section_corners)
    survey_section_corners_fc.update({"visibility": False})
    survey_section_lines_fc = feature_class(survey_section_lines)
    survey_section_polygons_fc = feature_class(survey_section_polygons, 0.5)
    survey_section_polygons_fc.update({"visibility": False})
    survey_dlc_fc = feature_class(survey_dlc)
    survey_dlc_fc.update({"visibility": False})
    survey_index_fc = feature_class(survey_index)
    survey_index_fc.update({"visibility": False})

    survey_group = group_layer("Survey")
    survey_group["layers"].append(survey_benchmarks_fc)
    survey_group["layers"].append(survey_section_polygons_fc)
    survey_group["layers"].append(survey_dlc_fc)
    survey_group["layers"].append(survey_dlc_corners_fc)
    survey_group["layers"].append(survey_geodetic_control_fc)
    survey_group["layers"].append(survey_section_corners_fc)
    survey_group["layers"].append(survey_section_lines_fc)
    survey_group["layers"].append(survey_index_fc)
    survey_group["layers"].append(survey_section_numbers_fc)

    group_lyr["layers"].append(survey_group)


def transport_layers(group_lyr):
    """
    Append transportation layers to web map group layer.

    :param group_lyr: Group layer definition to append with layers.
    :return: Group layer definition with transportation layers appended.
    :rtype: None.
    """
    transport_road_names = MapServiceLayer(TRANSPORTATION_ROAD_NAMES)
    transport_road_surface = MapServiceLayer(TRANSPORTATION_ROAD_SURFACE)
    transport_centerlines = MapServiceLayer(TRANSPORTATION_CENTERLINES)
    transport_roads = MapServiceLayer(TRANSPORTATION_ROADS)
    transport_railroads = MapServiceLayer(TRANSPORTATION_RAILROADS)

    transport_road_names_fc = feature_class(transport_road_names)
    transport_road_names_fc.update({"visibility": False})
    transport_road_surface_fc = feature_class(transport_road_surface)
    transport_road_surface_fc.update({"visibility": False})
    transport_centerlines_fc = feature_class(transport_centerlines)
    transport_centerlines_fc.update({"visibility": False})
    transport_roads_fc = feature_class(transport_roads, 0.5)
    transport_roads_fc.update({"visibility": False})
    transport_railroads_fc = feature_class(transport_railroads)

    transport_group = group_layer("Transportation")

    transport_group["layers"].append(transport_road_surface_fc)
    transport_group["layers"].append(transport_roads_fc)
    transport_group["layers"].append(transport_centerlines_fc)
    transport_group["layers"].append(transport_road_names_fc)
    transport_group["layers"].append(transport_railroads_fc)

    group_lyr["layers"].append(transport_group)


def zoning_map(project_map):
    ugb_corv = MapServiceLayer(ZONING_UGB_CORVALLIS_URL)
    ugb_phil = MapServiceLayer(ZONING_UGB_PHILOMATH_URL)
    zoning = MapServiceLayer(ZONING_URL)
    zoning_airport = MapServiceLayer(ZONING_AIRPORT_URL)
    zoning_fema = MapServiceLayer(ZONING_FEMA_FLOODPLAIN_URL)

    ugb_corv_fc = fc_gen(ugb_corv, 0.75)
    ugb_phil_fc = fc_gen(ugb_phil, 0.75)
    zoning_fc = fc_gen(zoning, 0.75)
    zoning_airport_fc = fc_gen(zoning_airport, 0.75)
    zoning_fema_fc = fc_gen(zoning_fema, 0.75)


def county_boundaries(group_lyr):
    """
    Add boundaries layers to group for web map.
    Layers include cities and places, counties, precincts, parks, zip codes, school districts and fire districts.

    :param group_lyr: Group layer definition to append with boundary layers.
    :return: Group layer definition with boundary layers appended.
    :rtype: None.
    """
    bc_boundaries_cities = MapServiceLayer(BC_BOUNDARIES_CITIES)
    bc_boundaries_county = MapServiceLayer(BC_BOUNDARIES_COUNTY)
    bc_boundaries_precincts = MapServiceLayer(BC_BOUNDARIES_PRECINCTS)
    bc_boundaries_parks = MapServiceLayer(BC_BOUNDARIES_PARKS)
    bc_boundaries_zip = MapServiceLayer(BC_BOUNDARIES_ZIP_CODES)
    bc_boundaries_school = MapServiceLayer(BC_BOUNDARIES_SCHOOL)
    bc_boundaries_fire = MapServiceLayer(BC_BOUNDARIES_FIRE)
    # bc_boundaries_all = MapServiceLayer(BC_BOUNDARIES_ALL_DISTRICTS)

    bc_boundaries_cities_fc = feature_class(bc_boundaries_cities)
    bc_boundaries_county_fc = feature_class(bc_boundaries_county)
    bc_boundaries_precincts_fc = feature_class(bc_boundaries_precincts)
    bc_boundaries_precincts_fc.update({"visibility": False})
    bc_boundaries_parks_fc = feature_class(bc_boundaries_parks)
    bc_boundaries_zip_fc = feature_class(bc_boundaries_zip)
    bc_boundaries_zip_fc.update({"visibility": False})
    bc_boundaries_school_fc = feature_class(bc_boundaries_school)
    bc_boundaries_school_fc.update({"visibility": False})
    bc_boundaries_fire_fc = feature_class(bc_boundaries_fire)
    bc_boundaries_fire_fc.update({"visibility": False})
    # bc_boundaries_all_fc = feature_class(bc_boundaries_all)

    boundary_group = group_layer("Boundaries")

    # group_layer["layers"].append(bc_boundaries_all_fc)
    boundary_group["layers"].append(bc_boundaries_fire_fc)
    boundary_group["layers"].append(bc_boundaries_school_fc)
    boundary_group["layers"].append(bc_boundaries_zip_fc)
    boundary_group["layers"].append(bc_boundaries_parks_fc)
    boundary_group["layers"].append(bc_boundaries_precincts_fc)
    boundary_group["layers"].append(bc_boundaries_county_fc)
    boundary_group["layers"].append(bc_boundaries_cities_fc)

    group_lyr["layers"].append(boundary_group)


def county_basemap_layers(group_layer):
    """
    Add common reference layers to group layer.
    Layers are taxlots, roads, railroads, section lines and section numbers.

    :param group_layer: Group layer target for reference layers.
    :return: Appends reference layers to group layer.
    :rtype: None.
    """
    bc_taxlots = MapServiceLayer(BC_TAXLOTS)
    bc_roads = MapServiceLayer(BC_ROADS)
    bc_railroads = MapServiceLayer(BC_RAILROADS)
    bc_section_lines = MapServiceLayer(BC_SECTION_LINES)
    bc_section_numbers = MapServiceLayer(BC_SECTION_NUMBERS)

    bc_taxlots_fc = feature_class(bc_taxlots, 0.75)
    bc_roads_fc = feature_class(bc_roads, 1.0)
    bc_railroads_fc = feature_class(bc_railroads, 0.75)
    bc_section_lines_fc = feature_class(bc_section_lines, 0.75)
    bc_section_numbers_fc = feature_class(bc_section_numbers, 0.75)

    # append in reverse legend order
    group_layer["layers"].append(bc_taxlots_fc)
    group_layer["layers"].append(bc_roads_fc)
    group_layer["layers"].append(bc_railroads_fc)
    group_layer["layers"].append(bc_section_lines_fc)
    group_layer["layers"].append(bc_section_numbers_fc)


def county_basemap(project_map):
    """
    Add common reference layers to web map.
    Layers are taxlots, roads, railroads, section lines and section numbers.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    basemap = group_layer("Base")
    zoning_layers(basemap)
    natural_layers(basemap)
    address_layers(basemap)
    # taxlot_layers(basemap)
    transport_layers(basemap)
    county_boundaries(basemap)
    survey_layers(basemap)
    # county_basemap_layers(basemap)
    map_def = project_map.get_data()
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})


def layer_urls(item):
    """List service layer urls.

    :param item: Service with target layers.
    :type kind: ArcGISFeatureLayer
    :return: A list of urls for layers in the service.
    :rtype: list[str]

    >>> import bentoncounty_gistools from bentoncounty_gistools as bc
    >>> gis = GIS()
    >>> # load natural features inventory feature collection service
    >>> nfi_fs = gis.content.search(
    >>>     "NaturalFeaturesInventoryService2022_DRAFT",
    >>>     item_type="Feature Layer Collection",
    >>> )[0]
    >>> urls = bc.layer_urls(nfi_fs)
    >>> urls[0]
    "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/0"
    >>> urls[1]
    "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/3"
    """
    urls = []
    for lyr in item.layers:
        urls.append(lyr.url)
    return urls


def create_layer_id(layerIndex):
    """
    Generate random ids for layers. Copied verbatim from https://community.esri.com/t5/arcgis-api-for-python-questions/python-api-add-group-layer-to-webmap/td-p/1112126.

    To build a web map from a published service, we generate feature layers pointed to each service. Each feature layer requires a unique layer id, produced by this function.

    :param layerIndex: Layer index number.
    :return: A randomized string to serve as a unique id.
    :rtype: str
    """
    return (
        "".join(random.choices(string.ascii_lowercase + string.digits, k=11))
        + "-layer-"
        + str(layerIndex)
    )


def feature_class(layer, opacity=1.0):
    """
    Generic feature class wrapper for layer data.

    :param layer: Source for feature layer.
    :type layer: MapServiceLayer
    :param opacity: Opacity of feature layer.
    :type opacity: float
    :return: Feature layer data for map service layer.

    >>> import bentoncounty_gistools from bentoncounty_gistools as bc
    >>> gis = GIS()
    >>> # load natural features inventory feature collection service
    >>> nfi_fs = gis.content.search(
    >>>     "NaturalFeaturesInventoryService2022_DRAFT",
    >>>     item_type="Feature Layer Collection",
    >>> )[0]
    >>> urls = bc.layer_urls(nfi_fs)
    >>> streams = MapServiceLayer(urls[0])
    >>> stream = bc.fc_gen(streams)
    >>> stream["url"]
    "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/0"
    >>> stream["title"]
    "STREAMS"
    >>> stream["layerType"]
    "ArcGISFeatureLayer"
    """
    fc_dict = {}
    fc_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    fc_dict.update({"url": layer.url})
    fc_dict.update({"title": layer.properties.name})
    fc_dict.update({"layerType": "ArcGISFeatureLayer"})
    fc_dict.update({"opacity": opacity})
    return fc_dict


# generate feature class data for layer
def fc_gen(layer, opacity=1.0):
    """
    To create group layers, we wrap each service in a feature layer. This function formats the feature layer based upon the service layer.

    :param layer: Source for feature layer.
    :type layer: MapServiceLayer
    :param opacity: Opacity of feature layer.
    :type opacity: float
    :return: Feature layer data for map service layer.

    >>> import bentoncounty_gistools from bentoncounty_gistools as bc
    >>> gis = GIS()
    >>> # load natural features inventory feature collection service
    >>> nfi_fs = gis.content.search(
    >>>     "NaturalFeaturesInventoryService2022_DRAFT",
    >>>     item_type="Feature Layer Collection",
    >>> )[0]
    >>> urls = bc.layer_urls(nfi_fs)
    >>> streams = MapServiceLayer(urls[0])
    >>> stream = bc.fc_gen(streams)
    >>> stream["url"]
    "https://services5.arcgis.com/U7TbEknoCzTtNGz4/arcgis/rest/services/NaturalFeaturesInventoryService2022_DRAFT/FeatureServer/0"
    >>> stream["title"]
    "STREAMS"
    >>> stream["layerType"]
    "ArcGISFeatureLayer"
    """
    fc_dict = {}
    fc_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    fc_dict.update({"url": layer.url})
    fc_dict.update({"title": layer.properties.name})
    fc_dict.update({"itemId": layer.properties.serviceItemId})
    fc_dict.update({"layerType": "ArcGISFeatureLayer"})
    fc_dict.update({"opacity": opacity})
    return fc_dict


def ms_gen(layer):
    ms_dict = {}
    ms_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    ms_dict.update({"url": layer.url})
    ms_dict.update({"title": layer.properties.name})
    ms_dict.update({"itemId": layer.properties.serviceItemId})
    ms_dict.update({"layerType": "ArcGISMapServiceLayer"})
    return ms_dict


def group_layer(title):
    """
    Generates an empty group layer with a specified title.

    :param title: The title of the layer as shown in the legend.
    :return: A json dictionary for a group layer.
    """
    group_dict = {}
    group_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    group_dict.update({"layers": []})
    group_dict.update({"layerType": "GroupLayer"})
    group_dict.update({"title": title})
    return group_dict


def add_nfi(project_map, service, template):
    """
    Updates a web mab to include the natural features inventory.

    :param project_map: The web map to update with the NFI.
    :param service: The natural features inventory feature collection service.
    :param template: Template layer for popup info.
    :return: None (modifies project_map)
    """
    urls = layer_urls(service)

    # load layers for grouping
    # streams layer
    streams = MapServiceLayer(url=urls[0])

    # Features
    ## significant vegetation
    # protected oak savanna
    oak_savanna = MapServiceLayer(url=urls[1])

    # high protection significant vegetation
    inc_veg_hi_1 = MapServiceLayer(url=urls[2])
    inc_veg_hi_2 = MapServiceLayer(url=urls[3])
    inc_veg_hi_3 = MapServiceLayer(url=urls[4])
    inc_veg_hi_4 = MapServiceLayer(url=urls[5])
    inc_veg_hi_5 = MapServiceLayer(url=urls[6])
    inc_veg_hi_6 = MapServiceLayer(url=urls[7])
    inc_veg_hi_7 = MapServiceLayer(url=urls[8])
    inc_veg_hi_8 = MapServiceLayer(url=urls[9])
    inc_veg_hi_9 = MapServiceLayer(url=urls[10])

    # partial protection significant vegetation
    inc_veg_lo_1 = MapServiceLayer(url=urls[11])
    inc_veg_lo_2 = MapServiceLayer(url=urls[12])
    inc_veg_lo_3 = MapServiceLayer(url=urls[13])
    inc_veg_lo_4 = MapServiceLayer(url=urls[14])
    inc_veg_lo_5 = MapServiceLayer(url=urls[15])
    inc_veg_lo_6 = MapServiceLayer(url=urls[16])
    inc_veg_lo_7 = MapServiceLayer(url=urls[17])

    ## Riparian Areas
    # top-of-bank stream buffers
    buff_50 = MapServiceLayer(url=urls[18])
    buff_75 = MapServiceLayer(url=urls[19])
    buff_100 = MapServiceLayer(url=urls[20])
    buff_120 = MapServiceLayer(url=urls[21])
    buff_downtown = MapServiceLayer(url=urls[22])

    # Wetlands Within Riparian Adjacent Areas - no buffer
    wetlands_rip = MapServiceLayer(url=urls[23])

    ## Systems-Critical Wetlands
    # Locally Significant Wetlands
    wetlands_sig = MapServiceLayer(url=urls[24])

    ## Other Wetlands
    # DSL Wetlands (notify if activities within 25ft)
    wetlands_dsl = MapServiceLayer(url=urls[25])

    # Hazards
    ## Flooding
    # 0.2-Foot Floodway
    floodway = MapServiceLayer(url=urls[26])
    # Willamette, Marys, Mill Race
    flood_will = MapServiceLayer(url=urls[27])
    # Dixon
    flood_dixon = MapServiceLayer(url=urls[28])
    # Dunawi
    flood_dunawi = MapServiceLayer(url=urls[29])
    # Jackson Frazier
    flood_jackson = MapServiceLayer(url=urls[30])
    # Lewisburg
    flood_lewisburg = MapServiceLayer(url=urls[31])
    # Oak Creek
    flood_oak = MapServiceLayer(url=urls[32])
    # Sequoia
    flood_sequoia = MapServiceLayer(url=urls[33])
    # Village Green
    flood_village = MapServiceLayer(url=urls[34])

    ## Landslide Debris Runout Areas
    # Confined Channel
    runout_closed = MapServiceLayer(url=urls[35])
    # Open Channel
    runout_open = MapServiceLayer(url=urls[36])

    ## Landslide Risk
    # Landslides Risk
    landslide = MapServiceLayer(url=urls[37])

    ## Steep Slopes
    # Percent Slope
    steep_slope = MapServiceLayer(url=urls[38])

    # build popupInfo dictionary
    nfi_popup = nfi_popup_info(template)
    # format as feature layer for grouping
    stream = fc_gen(streams)
    stream.update({"popupInfo": nfi_popup["streams"]})
    oaksavanna = fc_gen(oak_savanna, 0.4)
    oaksavanna.update({"popupInfo": nfi_popup["oak_savanna"]})
    # high protection significant vegetation
    incveg_hi1 = fc_gen(inc_veg_hi_1, 0.4)
    incveg_hi2 = fc_gen(inc_veg_hi_2, 0.4)
    incveg_hi3 = fc_gen(inc_veg_hi_3, 0.4)
    incveg_hi4 = fc_gen(inc_veg_hi_4, 0.4)
    incveg_hi5 = fc_gen(inc_veg_hi_5, 0.4)
    incveg_hi6 = fc_gen(inc_veg_hi_6, 0.4)
    incveg_hi7 = fc_gen(inc_veg_hi_7, 0.4)
    incveg_hi8 = fc_gen(inc_veg_hi_8, 0.4)
    incveg_hi9 = fc_gen(inc_veg_hi_9, 0.4)

    incveg_hi1.update({"popupInfo": nfi_popup["hi_inc_1of9"]})
    incveg_hi2.update({"popupInfo": nfi_popup["hi_inc_2of9"]})
    incveg_hi3.update({"popupInfo": nfi_popup["hi_inc_3of9"]})
    incveg_hi4.update({"popupInfo": nfi_popup["hi_inc_4of9"]})
    incveg_hi5.update({"popupInfo": nfi_popup["hi_inc_5of9"]})
    incveg_hi6.update({"popupInfo": nfi_popup["hi_inc_6of9"]})
    incveg_hi7.update({"popupInfo": nfi_popup["hi_inc_7of9"]})
    incveg_hi8.update({"popupInfo": nfi_popup["hi_inc_8of9"]})
    incveg_hi9.update({"popupInfo": nfi_popup["hi_inc_9of9"]})

    # partial protection significant vegetation
    incveg_lo1 = fc_gen(inc_veg_lo_1, 0.4)
    incveg_lo2 = fc_gen(inc_veg_lo_2, 0.4)
    incveg_lo3 = fc_gen(inc_veg_lo_3, 0.4)
    incveg_lo4 = fc_gen(inc_veg_lo_4, 0.4)
    incveg_lo5 = fc_gen(inc_veg_lo_5, 0.4)
    incveg_lo6 = fc_gen(inc_veg_lo_6, 0.4)
    incveg_lo7 = fc_gen(inc_veg_lo_7, 0.4)

    incveg_lo1.update({"popupInfo": nfi_popup["lo_inc_1of7"]})
    incveg_lo2.update({"popupInfo": nfi_popup["lo_inc_2of7"]})
    incveg_lo3.update({"popupInfo": nfi_popup["lo_inc_3of7"]})
    incveg_lo4.update({"popupInfo": nfi_popup["lo_inc_4of7"]})
    incveg_lo5.update({"popupInfo": nfi_popup["lo_inc_5of7"]})
    incveg_lo6.update({"popupInfo": nfi_popup["lo_inc_6of7"]})
    incveg_lo7.update({"popupInfo": nfi_popup["lo_inc_7of7"]})

    ## Riparian Areas
    buff50 = fc_gen(buff_50, 0.4)
    buff50.update({"popupInfo": nfi_popup["buff50"]})
    buff75 = fc_gen(buff_75, 0.4)
    buff75.update({"popupInfo": nfi_popup["buff75"]})
    buff100 = fc_gen(buff_100, 0.4)
    buff100.update({"popupInfo": nfi_popup["buff100"]})
    buff120 = fc_gen(buff_120, 0.4)
    buff120.update({"popupInfo": nfi_popup["buff120"]})
    buffdown = fc_gen(buff_downtown, 0.4)
    buffdown.update({"popupInfo": nfi_popup["buff_downtown"]})
    wetlandsrip = fc_gen(wetlands_rip, 0.3)
    wetlandsrip.update({"popupInfo": nfi_popup["wetlands_rip"]})
    ## Systems-Critical Wetlands
    wetlandssig = fc_gen(wetlands_sig, 0.3)
    wetlandssig.update({"popupInfo": nfi_popup["wetlands_sig"]})
    ## Other Wetlands
    wetlandsdsl = fc_gen(wetlands_dsl, 0.19)
    wetlandsdsl.update({"popupInfo": nfi_popup["wetlands_dsl"]})
    # Hazards
    ## Flooding
    flood = fc_gen(floodway, 0.4)
    floodwill = fc_gen(flood_will, 0.3)
    flooddixon = fc_gen(flood_dixon, 0.3)
    flooddunawi = fc_gen(flood_dunawi, 0.3)
    floodjackson = fc_gen(flood_jackson, 0.3)
    floodlewisburg = fc_gen(flood_lewisburg, 0.3)
    floodoak = fc_gen(flood_oak, 0.3)
    floodsequoia = fc_gen(flood_sequoia, 0.3)
    floodvillage = fc_gen(flood_village, 0.3)
    runoutclosed = fc_gen(runout_closed, 0.3)
    runoutopen = fc_gen(runout_open, 0.3)
    landsliderisk = fc_gen(landslide, 0.3)
    steepslope = fc_gen(steep_slope, 0.19)

    flood.update({"popupInfo": nfi_popup["floodway"]})
    floodwill.update({"popupInfo": nfi_popup["flood_will"]})
    flooddixon.update({"popupInfo": nfi_popup["flood_dixon"]})
    flooddunawi.update({"popupInfo": nfi_popup["flood_dunawi"]})
    floodjackson.update({"popupInfo": nfi_popup["flood_jackson"]})
    floodlewisburg.update({"popupInfo": nfi_popup["flood_lewisburg"]})
    floodoak.update({"popupInfo": nfi_popup["flood_oak"]})
    floodsequoia.update({"popupInfo": nfi_popup["flood_sequoia"]})
    floodvillage.update({"popupInfo": nfi_popup["flood_village"]})
    runoutclosed.update({"popupInfo": nfi_popup["runout_closed"]})
    runoutopen.update({"popupInfo": nfi_popup["runout_open"]})
    landsliderisk.update({"popupInfo": nfi_popup["landslide_risk"]})
    steepslope.update({"popupInfo": nfi_popup["steep_slope"]})

    # define layer groups for web map
    # name of group layer shown to user in map legend
    high_protection = group_layer("High Protection")
    partial_protection = group_layer("Partial Protection")
    incentive_vegetation = group_layer("Incentive Vegetation")
    significant_vegetation = group_layer("Significant Vegetation")
    riparian_areas = group_layer("Riparian Areas")
    wetlands_critical = group_layer("Systems-Critical Wetlands")
    wetlands_other = group_layer("Other Wetlands")
    features = group_layer("Features")
    flooding = group_layer("Flooding")
    runout_areas = group_layer("Landslide Debris Runout Areas")
    steep_slopes = group_layer("Steep Slopes")
    hazards = group_layer("Hazards")
    nfi_group = group_layer("Natural Features Inventory")

    high_protection["layers"].append(incveg_hi9)
    high_protection["layers"].append(incveg_hi8)
    high_protection["layers"].append(incveg_hi7)
    high_protection["layers"].append(incveg_hi6)
    high_protection["layers"].append(incveg_hi5)
    high_protection["layers"].append(incveg_hi4)
    high_protection["layers"].append(incveg_hi3)
    high_protection["layers"].append(incveg_hi2)
    high_protection["layers"].append(incveg_hi1)

    partial_protection["layers"].append(incveg_lo7)
    partial_protection["layers"].append(incveg_lo6)
    partial_protection["layers"].append(incveg_lo5)
    partial_protection["layers"].append(incveg_lo4)
    partial_protection["layers"].append(incveg_lo3)
    partial_protection["layers"].append(incveg_lo2)
    partial_protection["layers"].append(incveg_lo1)

    incentive_vegetation["layers"].append(partial_protection)
    incentive_vegetation["layers"].append(high_protection)
    significant_vegetation["layers"].append(incentive_vegetation)
    significant_vegetation["layers"].append(oaksavanna)

    riparian_areas["layers"].append(wetlandsrip)
    riparian_areas["layers"].append(buffdown)
    riparian_areas["layers"].append(buff120)
    riparian_areas["layers"].append(buff100)
    riparian_areas["layers"].append(buff75)
    riparian_areas["layers"].append(buff50)

    wetlands_critical["layers"].append(wetlandssig)
    wetlands_other["layers"].append(wetlandsdsl)

    features["layers"].append(wetlands_other)
    features["layers"].append(wetlands_critical)
    features["layers"].append(riparian_areas)
    features["layers"].append(significant_vegetation)

    flooding["layers"].append(floodvillage)
    flooding["layers"].append(floodsequoia)
    flooding["layers"].append(floodoak)
    flooding["layers"].append(floodlewisburg)
    flooding["layers"].append(floodjackson)
    flooding["layers"].append(flooddunawi)
    flooding["layers"].append(flooddixon)
    flooding["layers"].append(floodwill)
    flooding["layers"].append(flood)

    runout_areas["layers"].append(runoutclosed)
    runout_areas["layers"].append(runoutopen)
    steep_slopes["layers"].append(steepslope)

    hazards["layers"].append(steepslope)
    hazards["layers"].append(landsliderisk)
    hazards["layers"].append(runout_areas)
    hazards["layers"].append(flooding)

    nfi_group["layers"].append(hazards)
    nfi_group["layers"].append(features)
    nfi_group["layers"].append(stream)

    map_def = project_map.get_data()
    map_def["operationalLayers"].append(nfi_group)
    project_map.update({"text": str(map_def)})


def addr_popup_info(template):
    addr = template.get_data()
    addr_dict = {}
    driveways = addr["operationalLayers"][0]["layers"][0]["layers"][1]["popupInfo"]
    address = addr["operationalLayers"][0]["layers"][0]["layers"][2]["popupInfo"]
    addr_dict.update({"driveways": driveways})
    addr_dict.update({"address": address})
    return addr_dict


def addr_labels(template):
    addr = template.get_data()
    addr_dict = {}
    labels = addr["operationalLayers"][0]["layers"][0]["layers"][2]["layerDefinition"]
    addr_dict.update({"labels": labels})
    return addr_dict


def nfi_popup_info(template):
    """
    Generates dictionary of popupInfo for layers of the natural features inventory.

    :param template: Template web map with pop ups enabled on target layers.
    :return: Dictionary of reference names keys and popupInfo values.
    """
    nfi_def = template.get_data()
    nfi_dict = {}
    streams = nfi_def["operationalLayers"][0]["layers"][2]["popupInfo"]
    oak_savanna = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][
        1
    ]["popupInfo"]
    # high incentive vegetation
    # oak savanna
    hi_inc_oak_sav = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][1]["layers"][0]["popupInfo"]
    # Old Growth Douglar Fir in Chip Ross
    hi_inc_chip = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][
        0
    ]["layers"][1]["layers"][1]["popupInfo"]
    # Native Tree Dominated Vegetation
    hi_inc_nat_veg = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][1]["layers"][2]["popupInfo"]
    # Native Tree Dominated - Timber Hill Hybrid
    hi_inc_timber = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][
        0
    ]["layers"][1]["layers"][3]["popupInfo"]
    # Top 11-25% in UGB
    hi_inc_top10 = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][
        0
    ]["layers"][1]["layers"][4]["popupInfo"]
    # Top Third in UGB
    hi_inc_topthird = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][1]["layers"][5]["popupInfo"]
    # Mitigation Tree Groves
    hi_inc_mit_tree = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][1]["layers"][6]["popupInfo"]
    # Native Tree Dominated
    hi_inc_nat_tree = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][1]["layers"][7]["popupInfo"]
    # Connecting Corridors for WHAs
    hi_inc_whas = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][
        0
    ]["layers"][1]["layers"][8]["popupInfo"]
    # Partial Protection Incentive Vegetation
    # Native Tree Dominated Vegetation
    lo_inc_nat_veg = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][0]["layers"][0]["popupInfo"]
    # Top 11-25% in UGB
    lo_inc_top = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][0][
        "layers"
    ][0]["layers"][1]["popupInfo"]
    # Top Third in UGB
    lo_inc_topthird = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][0]["layers"][2]["popupInfo"]
    # Isolated Tree Groves
    lo_inc_iso_tree = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][0]["layers"][3]["popupInfo"]
    # Mitigation Tree Groves
    lo_inc_mit_tree = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][0]["layers"][4]["popupInfo"]
    # Native Tree Dominated
    lo_inc_nat_tree = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3][
        "layers"
    ][0]["layers"][0]["layers"][5]["popupInfo"]
    # Connecting Corridors for WHAs
    lo_inc_whas = nfi_def["operationalLayers"][0]["layers"][1]["layers"][3]["layers"][
        0
    ]["layers"][0]["layers"][6]["popupInfo"]
    # Riparian Areas
    # Wetlands Within Riparian Adjacent Areas - no buffer
    wetlands_rip = nfi_def["operationalLayers"][0]["layers"][1]["layers"][2]["layers"][
        0
    ]["popupInfo"]
    # Downtown Between Dixon Creek and Marys
    wetlands_downtown = nfi_def["operationalLayers"][0]["layers"][1]["layers"][2][
        "layers"
    ][1]["popupInfo"]
    # 120-Foot TOB Buffers Except Downtown
    rip120 = nfi_def["operationalLayers"][0]["layers"][1]["layers"][2]["layers"][2][
        "popupInfo"
    ]
    # 100-Foot TOB Buffers
    rip100 = nfi_def["operationalLayers"][0]["layers"][1]["layers"][2]["layers"][3][
        "popupInfo"
    ]
    # 75-Foot TOB Buffers
    rip75 = nfi_def["operationalLayers"][0]["layers"][1]["layers"][2]["layers"][4][
        "popupInfo"
    ]
    # 50-Foot TOB Buffers
    rip50 = nfi_def["operationalLayers"][0]["layers"][1]["layers"][2]["layers"][5][
        "popupInfo"
    ]
    # Systems-Critical Wetlands
    wetlands_sig = nfi_def["operationalLayers"][0]["layers"][1]["layers"][1]["layers"][
        0
    ]["popupInfo"]
    # Other Wetlands
    wetlands_other = nfi_def["operationalLayers"][0]["layers"][1]["layers"][0][
        "layers"
    ][0]["popupInfo"]
    # Hazards
    # Percent Slope
    steep_slope = nfi_def["operationalLayers"][0]["layers"][0]["layers"][0]["popupInfo"]
    # Landslides Risk
    landslide_risk = nfi_def["operationalLayers"][0]["layers"][0]["layers"][1][
        "popupInfo"
    ]
    # Landslide Debris Runout Areas
    # Confined Channel
    runout_closed = nfi_def["operationalLayers"][0]["layers"][0]["layers"][2]["layers"][
        0
    ]["popupInfo"]
    # Open Channel
    runout_open = nfi_def["operationalLayers"][0]["layers"][0]["layers"][2]["layers"][
        1
    ]["popupInfo"]
    # Flooding
    # Village Green
    flood_village = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][
        0
    ]["popupInfo"]
    # Sequoia
    flood_sequoia = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][
        1
    ]["popupInfo"]
    # Oak Creek
    flood_oak = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][2][
        "popupInfo"
    ]
    # Lewisburg
    flood_lewisburg = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3][
        "layers"
    ][3]["popupInfo"]
    # Jackson
    flood_jackson = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][
        4
    ]["popupInfo"]
    # Dunawi
    flood_dunawi = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][
        5
    ]["popupInfo"]
    # Dixon
    flood_dixon = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][
        6
    ]["popupInfo"]
    # Willamette, Marys, Mill Race
    flood_will = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][7][
        "popupInfo"
    ]
    # 0.2-Foot Floodway
    floodway = nfi_def["operationalLayers"][0]["layers"][0]["layers"][3]["layers"][8][
        "popupInfo"
    ]

    nfi_dict.update({"streams": streams})
    nfi_dict.update({"oak_savanna": oak_savanna})
    nfi_dict.update({"hi_inc_9of9": hi_inc_oak_sav})
    nfi_dict.update({"hi_inc_8of9": hi_inc_chip})
    nfi_dict.update({"hi_inc_7of9": hi_inc_nat_veg})
    nfi_dict.update({"hi_inc_6of9": hi_inc_timber})
    nfi_dict.update({"hi_inc_5of9": hi_inc_top10})
    nfi_dict.update({"hi_inc_4of9": hi_inc_topthird})
    nfi_dict.update({"hi_inc_3of9": hi_inc_mit_tree})
    nfi_dict.update({"hi_inc_2of9": hi_inc_nat_tree})
    nfi_dict.update({"hi_inc_1of9": hi_inc_whas})
    nfi_dict.update({"lo_inc_7of7": lo_inc_nat_veg})
    nfi_dict.update({"lo_inc_6of7": lo_inc_top})
    nfi_dict.update({"lo_inc_5of7": lo_inc_topthird})
    nfi_dict.update({"lo_inc_4of7": lo_inc_iso_tree})
    nfi_dict.update({"lo_inc_3of7": lo_inc_mit_tree})
    nfi_dict.update({"lo_inc_2of7": lo_inc_nat_tree})
    nfi_dict.update({"lo_inc_1of7": lo_inc_whas})
    nfi_dict.update({"wetlands_rip": wetlands_rip})
    nfi_dict.update({"buff_downtown": wetlands_downtown})
    nfi_dict.update({"buff120": rip120})
    nfi_dict.update({"buff100": rip100})
    nfi_dict.update({"buff75": rip75})
    nfi_dict.update({"buff50": rip50})
    nfi_dict.update({"wetlands_sig": wetlands_sig})
    nfi_dict.update({"wetlands_dsl": wetlands_other})
    nfi_dict.update({"steep_slope": steep_slope})
    nfi_dict.update({"landslide_risk": landslide_risk})
    nfi_dict.update({"runout_open": runout_open})
    nfi_dict.update({"runout_closed": runout_closed})
    nfi_dict.update({"flood_village": flood_village})
    nfi_dict.update({"flood_sequoia": flood_sequoia})
    nfi_dict.update({"flood_oak": flood_oak})
    nfi_dict.update({"flood_jackson": flood_jackson})
    nfi_dict.update({"flood_lewisburg": flood_lewisburg})
    nfi_dict.update({"flood_dunawi": flood_dunawi})
    nfi_dict.update({"flood_dixon": flood_dixon})
    nfi_dict.update({"flood_will": flood_will})
    nfi_dict.update({"floodway": floodway})
    return nfi_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod()
