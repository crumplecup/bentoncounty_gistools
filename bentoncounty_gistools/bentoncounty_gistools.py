import random
import string
from arcgis.mapping import MapServiceLayer
from arcgis.mapping import MapFeatureLayer
import bentoncounty_gistools.urls as urls


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


def environment_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "natural_wetlands",
        "natural_soils",
        "bc_eq_slope",
        "bc_landslide",
        "shpo_buff",
        "rip_buff",
        "big_game",
        "earthquake_faults",
        "hydro_lines",
        "hydro_polys",
        "hydro_hucs",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("environment_" + lyr + post)
    return layer_name


def environment_layers(group_lyr, template):
    """
    Add layers for topographic contours to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    popup_names = environment_layer_names("_popup")
    label_names = environment_layer_names("_label")
    url_list = urls.environment_urls
    parent_group = group_layer("Environment")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        if fc["title"] == "Wetlands (NWI)":
            fc.update({"title": "Wetlands - NWI (County backup)"})
        if fc["title"] == "benton_eq_slope_region":
            fc.update({"title": "County Slope"})
        if fc["title"] == "benton_landslide_region":
            fc.update({"title": "County Landslide Risk"})
        if fc["title"] == "SHPO BUFFER":
            fc.update({"title": "SHPO Buffer"})
        if fc["title"] == "BENTON RIPARIAN BUFFER":
            fc.update({"title": "County Riparian Buffer"})
        if fc["title"] == "BIG GAME RANGE":
            fc.update({"title": "Big Game Range"})
        if fc["title"] == "EARTHQUAKE FAULTS (advisory only)":
            fc.update({"title": "Earthquake Faults (advisory only)"})
        if fc["title"] == "Hydro_lines":
            fc.update({"title": "Rivers & Streams"})
        if fc["title"] == "Hydro_polys":
            fc.update({"title": "Water Bodies"})
        if fc["title"] == "Hydro_HUCS":
            fc.update({"title": "HUCS Watershed Boundaries"})
        fc.update({"popupInfo": template[popup_names[i]]})
        fc.update({"layerDefinition": template[label_names[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def hcp_butterfly_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "surveyed",
        "nectar",
        "blue_zone",
        "blue_zone_ugb",
        "kincaid",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("hcp_butterfly_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def hcp_butterfly_layers(group_lyr, template):
    """
    Add layers for topographic contours to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    popup_names = hcp_butterfly_layer_names("_popup")
    label_names = hcp_butterfly_layer_names("_label")
    url_list = urls.HCP_BUTTERFLY_URLS
    parent_group = group_layer("HCP Butterfly")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        if fc["title"] == "SurveyedAreas":
            fc.update({"title": "Surveyed Areas"})
        if fc["title"] == "NectarZone":
            fc.update({"title": "Nectar Zone"})
        if fc["title"] == "FendersBlueZone - Official":
            fc.update({"title": "Fenders Blue Zone - Official"})
        if fc["title"] == "FendersBlueZones UGB_USFWS":
            fc.update({"title": "Fenders Blue Zone - UGB (USFWS)"})
        if fc["title"] == "KincaidLupinesZone":
            fc.update({"title": "Kincaid Lupines"})
        fc.update({"popupInfo": template[popup_names[i]]})
        fc.update({"layerDefinition": template[label_names[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def contour_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "100ft",
        "20ft",
        "10ft",
        "2ft",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("contours_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def contour_layers(group_lyr, template):
    """
    Add layers for topographic contours to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    popup_names = contour_layer_names("_popup")
    label_names = contour_layer_names("_label")
    url_list = urls.TOPO_CONTOURS_URLS
    parent_group = group_layer("Topographic Contours")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        # add_single_layer(contour_names[i], url_list[i], parent_group, template)
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        if fc["title"] == "contours100ft":
            fc.update({"title": "100-ft Contours"})
        if fc["title"] == "contours20ft":
            fc.update({"title": "20-ft Contours"})
        if fc["title"] == "contours10ft":
            fc.update({"title": "10-ft Contours"})
        if fc["title"] == "contours2ft":
            fc.update({"title": "2-ft Contours"})
        fc.update({"popupInfo": template[popup_names[i]]})
        fc.update({"layerDefinition": template[label_names[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def nfi_hazard_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "closed_channel",
        "open_channel",
        "landslide",
        "slope",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("nfi_hazard_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def nfi_hazard_layers(group_lyr, template):
    """
    Add layers for nfi hazards to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    url_list = urls.NFI_HAZARD_URLS
    parent_group = group_layer("Hazards")
    parent_group.update({"visibility": False})

    branch = group_layer("Percent Slope")
    add_single_layer("nfi_hazard_slope", url_list[0], branch, template)
    parent_group["layers"].append(branch)

    branch = group_layer("Landslide Risk")
    add_single_layer("nfi_hazard_landslide", url_list[1], branch, template)
    parent_group["layers"].append(branch)

    branch = group_layer("Landslide Debris Runout Areas")
    add_single_layer("nfi_hazard_open_channel", url_list[2], branch, template)
    add_single_layer("nfi_hazard_closed_channel", url_list[3], branch, template)
    parent_group["layers"].append(branch)

    nfi_flood_layers(parent_group, template)

    group_lyr["layers"].append(parent_group)


def nfi_flood_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "0.2_floodway",
        "willamette",
        "dixon",
        "dunawi",
        "jackson",
        "lewisburg",
        "oak_creek",
        "sequoia",
        "village",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("nfi_flood" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def nfi_flood_layers(group_lyr, template):
    """
    Add layers for nfi flooding hazards to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    layer_name = nfi_flood_layer_names("_label")
    popup_name = nfi_flood_layer_names("_popup")
    url_list = urls.NFI_FLOOD_URLS
    parent_group = group_layer("Flooding")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[layer_name[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def nfi_features_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "oak_savanna",
        "wetlands_critical",
        "wetlands_dsl",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("nfi_features_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def add_single_layer(key_name, url, group_lyr, template):
    popup_name = key_name + "_popup"
    label_name = key_name + "_label"
    lyr = MapServiceLayer(url)
    fc = feature_class(lyr, 0.5)
    fc.update({"popupInfo": template[popup_name]})
    fc.update({"layerDefinition": template[label_name]})
    group_lyr["layers"].append(fc)


def nfi_features_layers(group_lyr, template):
    """
    Add layers for riparian areas to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    url_list = urls.FEATURES_URLS
    parent_group = group_layer("Features")
    parent_group.update({"visibility": False})

    branch = group_layer("Other Wetlands")
    add_single_layer("nfi_features_wetlands_dsl", url_list[0], branch, template)
    parent_group["layers"].append(branch)

    branch = group_layer("Systems-Critical Wetlands")
    add_single_layer("nfi_features_wetlands_critical", url_list[1], branch, template)
    parent_group["layers"].append(branch)

    riparian_layers(parent_group, template)

    branch = group_layer("Significant Vegetation")
    ppsv_layers(branch, template)
    hpsv_layers(branch, template)
    add_single_layer("nfi_features_oak_savanna", url_list[2], branch, template)
    parent_group["layers"].append(branch)

    group_lyr["layers"].append(parent_group)


def riparian_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "50foot_buffers",
        "75foot_buffers",
        "100foot_buffers",
        "120foot_buffers",
        "downtown",
        "wetlands",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("riparian_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def riparian_layers(group_lyr, template):
    """
    Add layers for riparian areas to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    layer_name = riparian_layer_names("_label")
    popup_name = riparian_layer_names("_popup")
    url_list = urls.RIPARIAN_URLS
    parent_group = group_layer("Riparian Areas")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[layer_name[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def ppsv_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "connecting_corridors",
        "native_tree_dominated",
        "mitigation_tree_groves",
        "isolated_tree_groves",
        "top_third_ugb",
        "top_11_ugb",
        "native_tree_vegetation",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("ppsv_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def ppsv_layers(group_lyr, template):
    """
    Add layers for high protection incentive vegetation to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    popup_name = ppsv_layer_names("_popup")
    label_name = ppsv_layer_names("_label")
    url_list = urls.NFI_PPSV_URLS
    parent_group = group_layer("Partial Protection")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapFeatureLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[label_name[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def hpsv_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "connecting_corridors",
        "native_tree_dominated",
        "mitigation_tree_groves",
        "top_third_ugb",
        "top_11_ugb",
        "native_tree_timber",
        "native_tree_vegetation",
        "douglas_fir_chip_ross",
        "oak_savanna",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("hpsv_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def hpsv_layers(group_lyr, template):
    """
    Add layers for high protection incentive vegetation to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    popup_name = hpsv_layer_names("_popup")
    label_name = hpsv_layer_names("_label")
    url_list = urls.NFI_HPSV_URLS
    parent_group = group_layer("High Protection")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapFeatureLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[label_name[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def taxlot_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "corners",
        "water_lines",
        "taxlots",
        "tax_code_areas",
        "plss_lines",
        "reference_lines",
        "tax_code_lines",
        "fire_districts",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("taxlot_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def taxlot_layers(group_lyr, template):
    """
    Add layers for BC taxlots to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    layer_name = taxlot_layer_names("_label")
    url_list = urls.TAXLOT_URLS
    taxlot_group = group_layer("Taxlot Maps")
    taxlot_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)

        # customize layer data
        if fc["title"] is not "Corner - Above":
            fc.update({"layerDefinition": template[layer_name[i]]})
        if fc["title"] == "FireDistricts":
            fc.update({"title": "Fire Districts"})

        if fc["title"] == "TaxCodeLines - Below":
            fc.update({"title": "Tax Code Lines"})

        if fc["title"] == "ReferenceLines - Above":
            fc.update({"title": "Reference Lines"})

        if fc["title"] == "PLSSLines - Above":
            fc.update({"title": "PLSS Lines"})

        if fc["title"] == "WaterLines - Above":
            fc.update({"title": "Water Lines"})

        if fc["title"] == "Corner - Above":
            fc.update({"title": "Corners"})

        taxlot_group["layers"].append(fc)

    group_lyr["layers"].append(taxlot_group)


def anno_0050_layers_info(template):
    """
    Build dictionary of layer info.

    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions.
    """
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    zoning_current_popup = ref_list[0]["popupInfo"]
    zoning_current_labels = ref_list[0]["layerDefinition"]
    new_data.update({"zoning_current_popup": zoning_current_popup})
    new_data.update({"zoning_current_labels": zoning_current_labels})
    return new_data


def anno_0050_layers(group_lyr, template):
    """
    Add layers for BC taxlot anno 0050 to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    anno_group = group_layer("Anno 0050")
    # for lyr in urls.ANNO_0020_URLS:
    # map_lyr = MapServiceLayer(lyr)
    # fc = feature_class(map_lyr)
    # fc.update({"visibility": False})
    # anno_group["layers"].append(fc)
    lyr = MapServiceLayer(urls.ANNO_0050_URLS[0])
    fc = feature_class(lyr)
    anno_group["layers"].append(fc)

    group_lyr["layers"].append(anno_group)


def anno_0020_layers_info(template):
    """
    Build dictionary of layer info.

    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions.
    """
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    zoning_current_popup = ref_list[0]["popupInfo"]
    zoning_current_labels = ref_list[0]["layerDefinition"]
    new_data.update({"zoning_current_popup": zoning_current_popup})
    new_data.update({"zoning_current_labels": zoning_current_labels})
    return new_data


def anno_0020_layers(group_lyr, template):
    """
    Add layers for BC taxlot anno 0020 to group layer.

    :param group_lyr: Group layer definition target for layers.
    :return: Updates group layer definition with layers.
    """
    anno_group = group_layer("Anno 0020")
    # for lyr in urls.ANNO_0020_URLS:
    # map_lyr = MapServiceLayer(lyr)
    # fc = feature_class(map_lyr)
    # fc.update({"visibility": False})
    # anno_group["layers"].append(fc)
    lyr = MapServiceLayer(urls.ANNO_0020_URLS[0])
    fc = feature_class(lyr)
    anno_group["layers"].append(fc)

    group_lyr["layers"].append(anno_group)


def zoning_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "ugb_corvallis",
        "ugb_philomath",
        "greenway",
        "overlays",
        "airport",
        "current",
        "flood",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("zoning_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def zoning_layers(group_lyr, template):
    """
    Add zoning layers to definition of a group layer.

    :param group_lyr: Group layer to update with zoning layers.
    :param template: Web map template for feature layer info.
    :return: Updates group layer definition with zoning' layers.
    """
    popup_name = zoning_layer_names("_popup")
    label_name = zoning_layer_names("_label")
    url_list = urls.ZONING_URLS_DRAFT
    parent_group = group_layer("Zoning")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[label_name[i]]})
        if fc["title"] == "ugb_corvallis_draft_jan2022":
            fc.update({"title": "UGB Corvallis"})
        if fc["title"] == "philomath_ugb_draft":
            fc.update({"title": "UGB Philomath"})
        if fc["title"] == "Willamette Greenway Area":
            fc.update({"title": "Willamette Greenway"})
        if fc["title"] == "Official Zoning Overlays":
            fc.update({"title": "Overlays"})
        if fc["title"] == "Airport Overlay Zone":
            fc.update({"title": "Airport Overlay"})
        if fc["title"] == "Zoning - current":
            fc.update({"title": "Zoning"})
        if fc["title"] == "FEMA_floodplain":
            fc.update({"title": "FEMA Floodplain (County backup)"})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def natural_layers_info(template):
    """
    Build dictionary of layer info for natural layers. Includes popup info.

    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the natural layers.
    """
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    wetlands_popup = ref_list[0]["popupInfo"]
    wetlands_labels = ref_list[0]["layerDefinition"]
    soils_popup = ref_list[1]["popupInfo"]
    soils_labels = ref_list[1]["layerDefinition"]
    hydro_lines_labels = ref_list[2]["layerDefinition"]
    hydro_polys_labels = ref_list[3]["layerDefinition"]
    hucs_popup = ref_list[4]["popupInfo"]
    hucs_labels = ref_list[4]["layerDefinition"]
    new_data.update({"wetlands_popup": wetlands_popup})
    new_data.update({"wetlands_labels": wetlands_labels})
    new_data.update({"soils_popup": soils_popup})
    new_data.update({"soils_labels": soils_labels})
    new_data.update({"hydro_lines_labels": hydro_lines_labels})
    new_data.update({"hydro_polys_labels": hydro_polys_labels})
    new_data.update({"hucs_popup": hucs_popup})
    new_data.update({"hucs_labels": hucs_labels})
    return new_data


def natural_layers(group_lyr, template):
    """
    Add natural layers to definition of a group layer. Includes water, soils and wetlands.

    :param group_lyr: Group layer to update with natural layers.
    :param template: Web map template for feature layer info.
    :return: Updates group layer definition with natural layers.
    """
    natural_hydro_hucs = MapServiceLayer(NATURAL_HYDRO_HUCS)
    natural_hydro_polys = MapServiceLayer(NATURAL_HYDRO_POLYS)
    natural_hydro_lines = MapServiceLayer(NATURAL_HYDRO_LINES)
    natural_soils = MapServiceLayer(NATURAL_SOILS)
    natural_wetlands = MapServiceLayer(NATURAL_WETLANDS)

    natural_hydro_hucs_fc = feature_class(natural_hydro_hucs)
    natural_hydro_hucs_fc.update({"title": "Watershed HUCS"})
    natural_hydro_hucs_fc.update({"visibility": False})
    natural_hydro_hucs_fc.update({"disablePopup": False})
    natural_hydro_hucs_fc.update({"popupInfo": template["hucs_popup"]})
    natural_hydro_hucs_fc.update({"layerDefinition": template["hucs_labels"]})
    natural_hydro_polys_fc = feature_class(natural_hydro_polys)
    natural_hydro_polys_fc.update({"title": "Water Bodies"})
    natural_hydro_polys_fc.update({"visibility": False})
    natural_hydro_polys_fc.update({"layerDefinition": template["hydro_polys_labels"]})
    natural_hydro_lines_fc = feature_class(natural_hydro_lines)
    natural_hydro_lines_fc.update({"title": "Rivers & Streams"})
    natural_hydro_lines_fc.update({"visibility": False})
    natural_hydro_lines_fc.update({"layerDefinition": template["hydro_lines_labels"]})
    natural_soils_fc = feature_class(natural_soils)
    natural_soils_fc.update({"title": "Soils"})
    natural_soils_fc.update({"visibility": False})
    natural_soils_fc.update({"disablePopup": False})
    natural_soils_fc.update({"popupInfo": template["soils_popup"]})
    natural_soils_fc.update({"layerDefinition": template["soils_labels"]})
    natural_wetlands_fc = feature_class(natural_wetlands)
    natural_wetlands_fc.update({"title": "Wetlands - NWI (County)"})
    natural_wetlands_fc.update({"visibility": False})
    natural_wetlands_fc.update({"disablePopup": False})
    natural_wetlands_fc.update({"popupInfo": template["wetlands_popup"]})
    natural_wetlands_fc.update({"layerDefinition": template["wetlands_labels"]})

    natural_group = group_layer("WATER|SOILS|WETLANDS")
    natural_group["layers"].append(natural_wetlands_fc)
    natural_group["layers"].append(natural_soils_fc)
    natural_group["layers"].append(natural_hydro_lines_fc)
    natural_group["layers"].append(natural_hydro_polys_fc)
    natural_group["layers"].append(natural_hydro_hucs_fc)

    group_lyr["layers"].append(natural_group)


def address_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "county",
        "corvallis",
        "driveways",
        "buildings",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("address_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def address_layers(group_lyr, template):
    """
    Add address layers to definition of a group layer.

    :param group_lyr: Group layer to update with address layers.
    :param template: Web map template for feature layer info.
    :return: Updates group layer definition with address layers.
    """
    popup_name = address_layer_names("_popup")
    label_name = address_layer_names("_label")
    url_list = urls.ADDRESS_URLS
    parent_group = group_layer("Addresses")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[label_name[i]]})
        if fc["title"] == "County_Addresses":
            fc.update({"title": "County"})
        if fc["title"] == "Structure_AddressCorvallis":
            fc.update({"title": "Corvallis"})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def survey_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "benchmarks",
        "geodetic_control",
        "section_corners",
        "section_polygons",
        "dlc_corners",
        "dlc",
        "survey_index",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("survey_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def update_popup_info(names, template):
    """
    Build dictionary of layer info for layers.

    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the survey layers.
    """
    label_name = names("_popup")
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    for i in range(0, len(label_name)):
        new_data.update({label_name[i]: ref_list[i]["popupInfo"]})

    return new_data


def update_layer_def(names, template):
    """
    Build dictionary of layer info for layers.

    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the survey layers.
    """
    label_name = names("_label")
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    for i in range(0, len(label_name)):
        new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data


def update_layer_info(names, template):
    """
    Build dictionary of layer info for layers. Includes popup info.

    :param template: Web map template for layer fields.
    :return: Dictionary of short keys and layer definitions for the survey layers.
    """
    popup_name = names("_popup")
    label_name = names("_label")
    ref_data = template.get_data()
    ref_list = ref_data["operationalLayers"][0]["layers"][0]["layers"]
    new_data = {}
    for i in range(0, len(popup_name)):
        new_data.update({popup_name[i]: ref_list[i]["popupInfo"]})
        new_data.update({label_name[i]: ref_list[i]["layerDefinition"]})

    return new_data


def test_map_layers(project_map, layers, template):
    """
    Build test map of the target layers.

    :param project_map: Web map to update with target layers.
    :type project_map: Web Map
    :param template: Web map template for feature layer info.
    :type template: Dictionary
    :return: Updates web map to include the target layers.
    :rtype: None
    """
    basemap = group_layer("Base")
    layers(basemap, template)
    map_def = project_map.get_data()
    map_def["operationalLayers"].append(basemap)
    project_map.update({"text": str(map_def)})


def survey_layers(group_lyr, template):
    popup_name = survey_layer_names("_popup")
    label_name = survey_layer_names("_label")
    url_list = urls.SURVEY_URLS
    parent_group = group_layer("Survey")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"popupInfo": template[popup_name[i]]})
        fc.update({"layerDefinition": template[label_name[i]]})
        if fc["title"] == "DLC_corner_index":
            fc.update({"title": "DLC Corners"})
        if fc["title"] == "Section_corner_index":
            fc.update({"title": "Section Corners"})
        if fc["title"] == "Section polygons":
            fc.update({"title": "Sections"})
        if fc["title"] == "Donationlandclaims":
            fc.update({"title": "Donation Land Claims"})
        if fc["title"] == "survey_index":
            fc.update({"title": "Survey Index"})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def transport_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "railroads",
        "centerlines",
        "roads",
        "road_surface",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("transport_" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def transport_layers(group_lyr, template):
    """
    Append transportation layers to web map group layer.

    :param group_lyr: Group layer definition to append with layers.
    :return: Group layer definition with transportation layers appended.
    :rtype: None.
    """
    label_name = transport_layer_names("_label")
    url_list = urls.TRANSPORT_URLS
    parent_group = group_layer("Transportation")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        fc.update({"layerDefinition": template[label_name[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def boundary_layer_names(post):
    """
    Create list of key names for layer definition data.
    """
    layer_stub = [
        "cities",
        "county",
        "precincts",
        "parks",
        "zip_codes",
        "school_districts",
        "fire_districts",
    ]
    layer_name = []
    for lyr in layer_stub:
        layer_name.append("boundary" + lyr + post)
    # layer order is reversed from menu order
    layer_name.reverse()
    return layer_name


def county_boundaries(group_lyr, template):
    """
    Add boundaries layers to group for web map.
    Layers include cities and places, counties, precincts, parks, zip codes, school districts and fire districts.

    :param group_lyr: Group layer definition to append with boundary layers.
    :return: Group layer definition with boundary layers appended.
    :rtype: None.
    """
    label_name = boundary_layer_names("_label")
    popup_name = boundary_layer_names("_popup")
    url_list = urls.BOUNDARY_URLS
    parent_group = group_layer("Boundaries")
    parent_group.update({"visibility": False})
    for i in range(0, len(url_list)):
        map_lyr = MapServiceLayer(url_list[i])
        fc = feature_class(map_lyr, 0.5)
        if fc["title"] not in ["County Parks"]:
            fc.update({"layerDefinition": template[label_name[i]]})
        if fc["title"] in ["Zip Codes"]:
            fc.update({"popupInfo": template[popup_name[i]]})
        parent_group["layers"].append(fc)

    group_lyr["layers"].append(parent_group)


def county_basemap(project_map, template):
    """
    Add common reference layers to web map.
    Layers are taxlots, roads, railroads, section lines and section numbers.

    :param project_map: Web map to update with reference layers.
    :return: Updates the web map, adding reference layers.
    :rtype: None.
    """
    basemap = group_layer("County Planning Maps")
    natural_layers(basemap, template)
    zoning_layers(basemap, template)
    address_layers(basemap, template)
    taxlot_layers(basemap, template)
    transport_layers(basemap, template)
    county_boundaries(basemap, template)
    survey_layers(basemap, template)
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


def build_template_dictionary(template_type, template):
    template_dict = {}
    match template_type:
        case "address":
            template_dict.update(update_layer_info(address_layer_names, template))
        case "boundary":
            template_dict.update(update_layer_info(boundary_layer_names, template))
        case "contour":
            template_dict.update(update_layer_info(contour_layer_names, template))
        case "environment":
            template_dict.update(update_layer_info(environment_layer_names, template))
        case "hcp":
            template_dict.update(update_layer_info(hcp_butterfly_layer_names, template))
        case "hpsv":
            template_dict.update(update_layer_info(hpsv_layer_names, template))
        case "natural":
            template_dict.update(natural_layers_info(template))
        case "nfi":
            template_dict.update(nfi_popup_info(template))
        case "nfi_features":
            template_dict.update(update_layer_info(nfi_features_layer_names, template))
        case "nfi_flood":
            template_dict.update(update_layer_info(nfi_flood_layer_names, template))
        case "nfi_hazard":
            template_dict.update(update_layer_info(nfi_hazard_layer_names, template))
        case "ppsv":
            template_dict.update(update_layer_info(ppsv_layer_names, template))
        case "riparian":
            template_dict.update(update_layer_info(riparian_layer_names, template))
        case "survey":
            template_dict.update(update_layer_info(survey_layer_names, template))
        case "taxlot":
            template_dict.update(update_layer_def(taxlot_layer_names, template))
        case "transport":
            template_dict.update(update_layer_def(transport_layer_names, template))
        case "zoning":
            template_dict.update(update_layer_info(zoning_layer_names, template))

    return template_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod()
