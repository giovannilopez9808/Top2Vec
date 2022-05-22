"""
Creacion del archivo news_clustered.csv que contiene la posición y la etiqueta del cluster en la columna `topic`.
"""
from Modules.functions import get_labels, get_hierarchy_topic
from Modules.params import get_params
from top2vec import Top2Vec
from os.path import join
import hdbscan
import umap

# Lectura de las rutas y nombres de los archivos
params = get_params()
# Nombre del modelo
filename = join(params["path data"],
                params["news model"])
model = Top2Vec.load(filename)
# Argumentos para el modelo UMAP
umap_args = {
    "n_neighbors": 15,
    "n_components": 2,
    "metric": "cosine",
}
# Ejecuccion del modelo UMAP
umap_model = umap.UMAP(**umap_args)
vectors = umap_model.fit(model.document_vectors)
# Ejecuccion del molode HDBSCAN
cluster_model = hdbscan.HDBSCAN(min_cluster_size=15,
                                metric='euclidean',
                                cluster_selection_method='eom')
cluster = cluster_model.fit(umap_model.embedding_)
# Diccionario con los topicos
hierarchy_dict = get_hierarchy_topic(model,
                                     20)
# Caracterización de cada cluster
clustered, outliers = get_labels(umap_model,
                                 model)
# Caracterizacion de los topicos
clustered["topic"] = clustered["doc_top"].apply(
    lambda label: hierarchy_dict[label])
# Guardado del archivo
filename = join(params["path results"],
                "news_clustered.csv")
clustered.to_csv(filename,
                 index=False)
