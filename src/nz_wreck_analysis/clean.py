"""Clean the wreck data to conform to the schema."""
import geopandas as gpd
from pandera.typing.geopandas import GeoDataFrame

from nz_wreck_analysis.domain import ExpositionCat, Wreck, WreckCat


def clean_wreck_data(
    gdf: gpd.GeoDataFrame,
) -> GeoDataFrame[Wreck]:
    """Clean the wreck data."""
    gdf = gdf.rename(
        columns={
            "geometry": Wreck.geometry,
            "fidn": Wreck.wreck_id,
            "catwrk": Wreck.cat,
            "expsou": Wreck.exposition_cat,
        },
    )
    gdf = gdf[
        [
            Wreck.geometry,
            Wreck.wreck_id,
            Wreck.cat,
            Wreck.exposition_cat,
        ]
    ]
    gdf[Wreck.cat] = gdf[Wreck.cat].map(
        {
            "1": WreckCat.NON_DANGEROUS,
            "2": WreckCat.DANGEROUS,
            "3": WreckCat.DIST_REMAINS,
            "4": WreckCat.MAST_SHOWN,
            "5": WreckCat.SUPERSTRUCT_SHOWN,
        },
    )
    gdf[Wreck.exposition_cat] = gdf[Wreck.exposition_cat].map(
        {
            "1": ExpositionCat.WITHIN_RNG,
            "2": ExpositionCat.SHOALER,
            "3": ExpositionCat.DEEPER,
        },
    )
    return Wreck.validate(gdf)
