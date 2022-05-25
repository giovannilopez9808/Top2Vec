"""
Conjunto de rutas y nombres de los archivos para los programas creados
"""

from os.path import join
from os import makedirs


def get_params() -> dict:
    params = {
        "root": "..",
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
    params["path data"] = join(params["root"],
                               params["path data"])
    params["path results"] = join(params["root"],
                                  params["path results"])
    params["path models"] = join(params["root"],
                                 params["path models"])
    params["path graphics"] = join(params["root"],
                                   params["path graphics"])
    mkdir(params["path results"])
    mkdir(params["path graphics"])
    mkdir(params["path models"])
    return params


def mkdir(path: str) -> None:
    """
    Estandarizacion del mkdir
    """
    makedirs(path, exist_ok=True)
