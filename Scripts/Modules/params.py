"""
Conjunto de rutas y nombres de los archivos para los programas creados
"""

from os import makedirs


def get_params() -> dict:
    params = {
        "path data": "Data",
        "path results": "Results",
        "path models": "Models",
        "path graphics": "Graphics",
        "news model": "news_model.h5",
        "yahoo model": "yahoo_model.h5",
        "path yahoo": "Yahoo",
        "yahoo data": "train.csv",
        "yahoo topics": "classes.txt",
        "path tripadvisor": "Tripadvisor",
        "tripadvisor model": "tripadvisor_model.h5",
        "tripadvisor data": "opinions.csv",
    }
    mkdir(params["path results"])
    mkdir(params["path graphics"])
    mkdir(params["path models"])
    return params


def mkdir(path: str) -> None:
    """
    Estandarizacion del mkdir
    """
    makedirs(path, exist_ok=True)
