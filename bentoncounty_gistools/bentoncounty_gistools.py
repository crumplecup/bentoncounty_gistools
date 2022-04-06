import random
import string
from arcgis.mapping import MapServiceLayer

def layer_urls(item):
    """List service layer urls.

    Keyword arguments:
    item -- ArcGIS Feature Collection Service
    """
    urls = []
    for lyr in item.layers:
        urls.append(lyr.url)
    return urls

def create_layer_id(layerIndex):
    """Generate random ids for layers.
    Copied verbatim from https://community.esri.com/t5/arcgis-api-for-python-questions/python-api-add-group-layer-to-webmap/td-p/1112126. To build a web map from a published service, we generate feature layers pointed to each service. Each feature layer requires a unique layer id, produced by this function.

    Keyword arguments:
    layerIndex -- Layer index number.
    """
    return ''.join(random.choices(string.ascii_lowercase + \
            string.digits, k=11)) + "-layer-" + str(layerIndex)


# generate feature class data for layer
def fc_gen(layer, opacity=1):
    """
    To create group layers, we wrap each service in a feature layer. This function formats the feature layer based upon the service layer.

    Keyword arguments:
    layer -- MapServiceLayer source for feature layer.
    opacity -- Opacity of feature layer.
    """
    fc_dict = {}
    fc_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    fc_dict.update({"url": layer.url})
    fc_dict.update({"title": layer.properties.name})
    fc_dict.update({"itemId": layer.properties.serviceItemId})
    fc_dict.update({"layerType": "ArcGISFeatureLayer"})
    fc_dict.update({"opacity": opacity})
    return fc_dict


def add_nfi(project_map, service):
    urls = layer_urls(service)
    urls

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
    # format as feature layer for grouping


    stream = fc_gen(streams)
    oaksavanna = fc_gen(oak_savanna, 0.4)

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

    # partial protection significant vegetation
    incveg_lo1 = fc_gen(inc_veg_lo_1, 0.4)
    incveg_lo2 = fc_gen(inc_veg_lo_2, 0.4)
    incveg_lo3 = fc_gen(inc_veg_lo_3, 0.4)
    incveg_lo4 = fc_gen(inc_veg_lo_4, 0.4)
    incveg_lo5 = fc_gen(inc_veg_lo_5, 0.4)
    incveg_lo6 = fc_gen(inc_veg_lo_6, 0.4)
    incveg_lo7 = fc_gen(inc_veg_lo_7, 0.4)

    ## Riparian Areas
    buff50 = fc_gen(buff_50, 0.4)
    buff75 = fc_gen(buff_75, 0.4)
    buff100 = fc_gen(buff_100, 0.4)
    buff120 = fc_gen(buff_120, 0.4)
    buffdown = fc_gen(buff_downtown, 0.4)
    wetlandsrip = fc_gen(wetlands_rip, 0.3)

    ## Systems-Critical Wetlands
    wetlandssig = fc_gen(wetlands_sig, 0.3)
    ## Other Wetlands
    wetlandsdsl = fc_gen(wetlands_dsl, 0.19)

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


    # define layer groups for web map


    high_protection = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "High Protection" }

    partial_protection = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Partial Protection" }

    incentive_vegetation = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Incentive Vegetation" }

    significant_vegetation = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Significant Vegetation" }

    riparian_areas = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Riparian Areas" }

    wetlands_critical = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Systems-Critical Wetlands" }

    wetlands_other = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Other Wetlands" }

    features = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Features" }

    flooding = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Flooding" }

    runout_areas = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Landslide Debris Runout Areas" }

    steep_slopes = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Steep Slopes" }

    hazards = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Hazards" }

    nfi_group = {
            "id": create_layer_id(random.randint(10000, 99999)),
            "layers": [],
            "layerType": "GroupLayer",
            "title": "Natural Features Inventory" }


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
    project_map.update({'text': str(map_def)})
