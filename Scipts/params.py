from os import makedirs


def get_params() -> dict:
    params = {
        "path data": "Data",
        "path results": "Results",
        "path graphics": "Graphics",
        "model name": "Model.h5",
    }
    mkdir(params["path results"])
    mkdir(params["path graphics"])
    return params


def mkdir(path: str) -> None:
    makedirs(path, exist_ok=True)
