import random
import string

"""
Copied verbatim from https://community.esri.com/t5/arcgis-api-for-python-questions/python-api-add-group-layer-to-webmap/td-p/1112126

To build a web map from a published service, we generate feature layers pointed to each service. Each feature layer requires a unique layer id, produced by this function.
"""
# generates random ids for layers
def create_layer_id(layerIndex):
    return ''.join(random.choices(string.ascii_lowercase + \
        string.digits, k=11)) + "-layer-" + str(layerIndex)


"""
To create group layers, we wrap each service in a feature layer. This function formats the feature layer based upon the service layer.
"""
# generate feature class data for layer
def fc_gen(layer):
    fc_dict = {}
    fc_dict.update({"id": create_layer_id(random.randint(10000, 99999))})
    fc_dict.update({"url": layer.url})
    fc_dict.update({"title": layer.properties.name})
    fc_dict.update({"itemId": layer.properties.serviceItemId})
    fc_dict.update({"layerType": "ArcGISFeatureLayer"})
    return fc_dict
