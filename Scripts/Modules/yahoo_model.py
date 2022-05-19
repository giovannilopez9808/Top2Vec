from pandas import DataFrame, read_csv
from os.path import join


class yahoo_data:

    def __init__(self, params: dict) -> None:
        self.params = params
        self._read()
        self._read_topics()

    def _read(self) -> DataFrame:
        filename = join(self.params["path data"],
                        self.params["yahoo data"])
        data = read_csv(filename,
                        header=None)
        data = data.fillna("")
        data["text"] = data[[1, 2, 3]].apply(lambda x: " ".join(x),
                                             axis=1)
        self.data = data.drop(columns=[1, 2, 3])
        self.data.columns = ["Index", "text"]

    def _read_topics(self) -> dict:
        filename = join(self.params["path data"],
                        self.params["yahoo topics"])
        topics = read_csv(filename,
                          header=None)
        topics = topics.to_dict()
        self.topics = topics[0]

    def get_topic(self, index: int) -> str:
        return self.topics[index]

    def get_text(self) -> list:
        return self.data["text"].to_list()
