"""
Conjunto de funciones para el ploteo y organizacion de los clusters
"""
from pandas import DataFrame
from typing import Callable
from hdbscan import HDBSCAN
from numpy import median


def get_centroid_topics(cluster: DataFrame, top2vec_model: Callable) -> dict:
    """
    Obtiene el centroide de los topicos dados
    """
    centroids = {}
    topics = list(set(cluster["topic"]))
    for topic in topics:
        centroids[topic] = {}
        # Obtiene el nombre de los topicos
        topic_name = create_topic_name(top2vec_model,
                                       topic)
        # Obtiene la posicion de cada palabra en el topic
        subcluster = get_cluster_per_topic(cluster,
                                           topic)
        x = subcluster["x"].to_numpy()
        y = subcluster["y"].to_numpy()
        c_x = median(x)
        c_y = median(y)
        c = [c_x, c_y]
        # Guardado del centroide
        centroids[topic]["centroid"] = c
        # Guardado del topico
        centroids[topic]["topic name"] = topic_name
    return centroids


def get_cluster_per_topic(cluster: DataFrame, topic: int) -> DataFrame:
    """
    Obtiene las posiciones correspondientes a cada palabra en el topic
    """
    return cluster[cluster["topic"] == topic]


def create_topic_name(top2vec: Callable, topic: int) -> str:
    """
    Crea un string con las primeras tres palabras más representativas del cluster
    """
    topic_words = top2vec.topic_words[topic]
    text = "{}: {}\n{}\n{}".format(topic,
                                   topic_words[0],
                                   topic_words[1],
                                   topic_words[2])
    return text


def get_hierarchy_topic(top2vec_model: Callable, num_clusters: int) -> dict:
    """
    Obtiene un mapa con los clusters creatos por top2vec y los relaciona con el numero de cluster obtenido por UMAP
    """
    hierarchy = top2vec_model.hierarchical_topic_reduction(num_clusters)
    hierarchy_dict = dict(
        sum([[(raw_id, i) for raw_id in mapping]
             for i, mapping in enumerate(hierarchy)], []))
    return hierarchy_dict


def get_labels(umap_model: Callable, top2vec_model: Callable) -> tuple:
    # Creaciond el modelo HDBSCAN
    cluster_model = HDBSCAN(min_cluster_size=15,
                            metric='euclidean',
                            cluster_selection_method='eom')
    # Obtiene los topicos
    cluster = cluster_model.fit(umap_model.embedding_)
    result = DataFrame(umap_model.embedding_,
                       columns=["x", "y"])
    result["labels"] = cluster.labels_
    result["doc_top"] = top2vec_model.doc_top
    outliers = result.loc[result.labels == -1, :]
    clustered = result.loc[result.labels != -1, :]
    return clustered, outliers
