"""Classes modelling the wreck data domain."""
from enum import auto

from geopandas.array import GeometryDtype
from pandas import StringDtype
from pandera import Category, DataFrameModel, Field
from pandera.typing import Series
from strenum import StrEnum


class WreckCat(StrEnum):
    """The categories of wrecks."""

    NON_DANGEROUS = auto()
    DANGEROUS = auto()
    DIST_REMAINS = auto()
    MAST_SHOWN = auto()
    SUPERSTRUCT_SHOWN = auto()


class ExpositionCat(StrEnum):
    """Exposition of sounding."""

    WITHIN_RNG = auto()
    SHOALER = auto()
    DEEPER = auto()


class Wreck(DataFrameModel):
    """A model for wreck dataframes."""

    geometry: Series[GeometryDtype]
    wreck_id: Series[StringDtype]
    cat: Series[Category(WreckCat)]
    exposition_cat: Series[Category(ExpositionCat)] = Field(nullable=True)

    class Config:
        """pandera config."""

        coerce = True
