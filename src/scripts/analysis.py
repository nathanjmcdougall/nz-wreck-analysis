"""Read-in the dataset and naively analyse it, notebook style."""

from IPython.display import display
from ydata_profiling import ProfileReport

from nz_wreck_analysis.clean import clean_wreck_data
from nz_wreck_analysis.data import download_raw_wreck_data

raw_gdf = download_raw_wreck_data()
gdf = clean_wreck_data(raw_gdf)
profile = ProfileReport(gdf.drop(columns="geometry"))
display(profile)
gdf.explore(
    # Use ESRI aerial imagery basemap
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community",
)
