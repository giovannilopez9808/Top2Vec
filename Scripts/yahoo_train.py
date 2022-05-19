from Modules.yahoo_model import yahoo_data
from Modules.params import get_params
from top2vec import Top2Vec
from os.path import join

params = get_params()
yahoo = yahoo_data(params)
corpus = yahoo.get_text()
filename = join(params["path data"],
                params["yahoo model"])
model = Top2Vec(documents=corpus[:10000],
                speed="learn",
                embedding_model="doc2vec",
                workers=8)
model.save(filename)
