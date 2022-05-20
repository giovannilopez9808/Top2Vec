from Modules.params import get_params
from top2vec import Top2Vec
from pandas import read_csv
from os.path import join

params = get_params()
filename = join(params["path data"],
                params["path tripadvisor"],
                params["tripadvisor data"])
data = read_csv(filename)
corpus = data["Text"].to_list()
filename = join(params["path models"],
                params["tripadvisor model"])
model = Top2Vec(documents=corpus,
                speed="learn",
                embedding_model="distiluse-base-multilingual-cased",
                workers=8)
model.save(filename)
