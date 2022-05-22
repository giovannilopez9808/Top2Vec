"""
Ejecuccion del modelo Top2Vec con el dataset 20NewsGroup
"""
from sklearn.datasets import fetch_20newsgroups
from Modules.params import get_params
from top2vec import Top2Vec
from os.path import join

# Lectura del conjunto de datos
newsgroups = fetch_20newsgroups(subset='all',
                                remove=('headers',
                                        'footers',
                                        'quotes'))
# Lectura de las rutas y nombres de los archivos
params = get_params()
# Nombre de guardado del modelo
filename = join(params["path models"],
                params["news model"])
# Ejecucion de Top2Vec
model = Top2Vec(documents=newsgroups.data,
                speed="learn",
                embedding_model="doc2vec",
                workers=8)
# Guardado del modelo
model.save(filename)
