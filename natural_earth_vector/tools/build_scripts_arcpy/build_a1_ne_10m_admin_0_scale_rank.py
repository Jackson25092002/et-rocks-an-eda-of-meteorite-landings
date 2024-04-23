# ---------------------------------------------------------------------------
# build_a1_ne_10m_admin_0_scale_rank.py
# Created on: Sat Aug 19 2017 11:43:00 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
ne_10m_admin_0_boundary_lines_land_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_boundary_lines_land.shp"
ne_10m_admin_0_label_points_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_label_points.shp"
ne_10m_admin_0_seams_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_seams.shp"
ne_10m_admin_0_boundary_lines_map_units_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_boundary_lines_map_units.shp"
ne_10m_admin_0_boundary_lines_disputed_areas_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_boundary_lines_disputed_areas.shp"
ne_10m_minor_islands_coastline_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_physical\\ne_10m_minor_islands_coastline.shp"
ne_10m_coastline_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_physical\\ne_10m_coastline.shp"
ne_10m_admin_0_scale_rank_minor_islands_tmp_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_scale_rank_minor_islands_tmp.shp"
ne_10m_admin_0_scale_rank_minor_islands_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_scale_rank_minor_islands.shp"
ne_10m_admin_0_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_scale_rank.shp"

# Process: Feature To Polygon...
gp.FeatureToPolygon_management("C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_physical\\ne_10m_coastline.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_physical\\ne_10m_minor_islands_coastline.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_boundary_lines_disputed_areas.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_boundary_lines_map_units.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_seams.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\10m_cultural\\ne_10m_admin_0_boundary_lines_land.shp", ne_10m_admin_0_scale_rank_minor_islands_tmp_shp, "", "ATTRIBUTES", ne_10m_admin_0_label_points_shp)

# Process: Select...
gp.Select_analysis(ne_10m_admin_0_scale_rank_minor_islands_tmp_shp, ne_10m_admin_0_scale_rank_minor_islands_shp, "\"sr_su_a3\" <> ' '")

# Process: Select (2)...
gp.Select_analysis(ne_10m_admin_0_scale_rank_minor_islands_shp, ne_10m_admin_0_scale_rank_shp, "scalerank <= 6")

