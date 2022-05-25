"""
Clase que contiene la organizacion de los datos de Yahoo Anserws
"""
from pandas import DataFrame, read_csv
from os.path import join


class yahoo_data:

    def __init__(self, params: dict) -> None:
        self.params = params
        self._read()
        self._read_topics()

    def _read(self) -> DataFrame:
        """
        Lectura de los datos
        """
        filename = join(self.params["path data"],
                        self.params["yahoo data"])
        # Lecuta de archivo
        data = read_csv(filename,
                        header=None)
        # Rellenado de informacion
        data = data.fillna("")
        # Join de la pregunta, la primer respuesta y la respuesta mas valorada
        data["text"] = data[[1, 2, 3]].apply(lambda x: " ".join(x),
                                             axis=1)
        # Limpieza de los datos
        self.data = data.drop(columns=[1, 2, 3])
        self.data.columns = ["Index", "text"]

    def _read_topics(self) -> dict:
        """
        Lectura de los topicos de cada pregunta
        """
        filename = join(self.params["path data"],
                        self.params["yahoo topics"])
        topics = read_csv(filename,
                          header=None)
        topics = topics.to_dict()
        self.topics = topics[0]

    def get_topic(self, index: int) -> str:
        """
        Regresa el topico de una pregunra dado un indice
        """
        return self.topics[index]

    def get_text(self) -> list:
        """
        Regresa el corpus de la base de datos
        """
        return self.data["text"].to_list()
