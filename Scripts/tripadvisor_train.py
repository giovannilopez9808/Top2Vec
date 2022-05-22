"""
Ejecuccion del modelo Top2Vec con el dataset Tripadvisor
"""
from Modules.params import get_params
from top2vec import Top2Vec
from pandas import read_csv
from os.path import join

# Lectura del conjunto de datos
params = get_params()
# Lectura de las rutas y nombres de los archivos
filename = join(params["path data"],
                params["path tripadvisor"],
                params["tripadvisor data"])
data = read_csv(filename)
corpus = data["Text"].to_list()
# Nombre de guardado del modelo
filename = join(params["path models"],
                params["tripadvisor model"])
# Ejecucion de Top2Vec
model = Top2Vec(documents=corpus,
                speed="learn",
                embedding_model="distiluse-base-multilingual-cased",
                workers=8)
# Guardado del modelo
model.save(filename)
