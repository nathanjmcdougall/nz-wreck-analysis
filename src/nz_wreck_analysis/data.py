"""The dataset for analysis."""
import urllib.request
from pathlib import Path
from tempfile import TemporaryDirectory

import geopandas as gpd

_DIRURL = r"https://raw.githubusercontent.com/nathanjmcdougall/linz-50518/main/"
_FILENAME = r"wreck-points-hydro-190k-1350k.gpkg"
_URL = _DIRURL + _FILENAME


def download_raw_wreck_data() -> gpd.GeoDataFrame:
    """Download the raw wreck data."""
    with TemporaryDirectory() as tempdirname:
        tempdir = Path(tempdirname)
        filepath = tempdir / _FILENAME
        urllib.request.urlretrieve(  # noqa: S310 since the URL is hardcoded
            _URL,
            filepath,
        )
        gdf = gpd.GeoDataFrame(gpd.read_file(filepath, driver="GPKG"))

    return gdf.dropna(axis="columns", how="all")
