from pandas import DataFrame
from typing import Callable
from hdbscan import HDBSCAN
from numpy import mean


def get_centroid_topics(cluster: DataFrame, top2vec_model: Callable) -> dict:
    centroids = {}
    topics = list(set(cluster["topic"]))
    for topic in topics:
        centroids[topic] = {}
        topic_name = create_topic_name(top2vec_model.topic_words[topic], topic)
        subcluster = cluster[cluster["topic"] == topic]
        x = subcluster["x"].to_numpy()
        y = subcluster["y"].to_numpy()
        c_x = mean(x)
        c_y = mean(y)
        c = [c_x, c_y]
        centroids[topic]["centroid"] = c
        centroids[topic]["topic name"] = topic_name
    return centroids


def create_topic_name(topic_words: list, index: int) -> str:
    text = "{}: {}\n{}\n{}".format(index, topic_words[0], topic_words[1],
                                   topic_words[2])
    return text


def get_hierarchy_topic(top2vec_model: Callable) -> dict:
    num_clusters = 20
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
