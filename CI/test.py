import pytest

def test_arcgispro_rrm():
    from arcpy import GetInstallInfo
    print(f"arcpy version: {GetInstallInfo()['Version']}")

    import geopandas
    print(f"geopandas version: {geopandas.__version__}")

    import rasterio
    print(f"rasterio version: {rasterio.__version__}")

    import fiona
    print(f"fiona version: {fiona.__version__}")

    import eoreader
    print(f"eoreader version: {eoreader.__version__}")

    import sertit
    print(f"sertit version: {sertit.__version__}")

    import lxml
    print(f"lxml version: {lxml.__version__}")

    # SAR
    # import eof
    # from importlib.metadata import version
    # print(f"sentineleof version: {version('sentineleof')}")
    #
    # # Specific libs for RUSLE
    # import pyodbc
    # print(f"pyodbc version: {pyodbc.version}")
    # import pysheds
    # print(f"pysheds version: {pysheds.__version__}")
    #
    # # Specific to Import_OSM_Charter
    # import osmnx
    # print(f"osmnx version: {osmnx.__version__}")


    with pytest.raises(ImportError):
        import fzeferzf