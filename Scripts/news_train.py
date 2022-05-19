from sklearn.datasets import fetch_20newsgroups
from Modules.params import get_params
from top2vec import Top2Vec
from os.path import join


newsgroups = fetch_20newsgroups(subset='all',
                                remove=('headers',
                                        'footers',
                                        'quotes'))
params = get_params()
filename = join(params["path data"],
                params["news model"])
model = Top2Vec(documents=newsgroups.data,
                speed="learn",
                embedding_model="doc2vec",
                workers=8)
model.save(filename)
