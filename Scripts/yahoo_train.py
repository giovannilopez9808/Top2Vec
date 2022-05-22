"""
Ejecuccion del modelo Top2Vec con el dataset Yahoo answers
"""
from Modules.yahoo_model import yahoo_data
from Modules.params import get_params
from top2vec import Top2Vec
from os.path import join

# Lectura de las rutas y nombres de los archivos
params = get_params()
# Lectura del conjunto de datos
yahoo = yahoo_data(params)
corpus = yahoo.get_text()
# Nombre de guardado del modelo
filename = join(params["path data"],
                params["yahoo model"])
# Ejecucion de Top2Vec
model = Top2Vec(documents=corpus[:10000],
                speed="learn",
                embedding_model="doc2vec",
                workers=8)
# Guardado del modelo
model.save(filename)
