import os
import sys
import arcpy

# creates a new gdb and loads the layers for county zoning

# Set local variables
out_path = "S:/maps/ZONING/ZoningRemap2018"
out_name = "BentonZoning2022_DRAFT.gdb"

# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_path, out_name)

out_gdb = "S:/maps/ZONING/ZoningRemap2018/BentonZoning2022_DRAFT.gdb"


in_gdb = "S:/maps/BentonCountyGIS/Zoning_Information/Zoning.gdb"
arcpy.env.workspace = in_gdb

fcs = arcpy.ListFeatureClasses()

# Copy shapefiles to a file geodatabase
for fc in fcs:
    arcpy.CopyFeatures_management(fc, os.path.join(out_gdb, os.path.splitext(fc)[0]))
