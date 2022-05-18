import matplotlib.pyplot as plt
from params import get_params
from pandas import DataFrame
from top2vec import Top2Vec
from os.path import join
from numpy import mean
import umap.plot
import hdbscan
import umap


def get_centroid_topics(cluster: DataFrame, top2vec_model: Top2Vec) -> dict:
    centroids = {}
    topics = list(set(cluster["topic"]))
    for topic in topics:
        centroids[topic] = {}
        topic_name = create_topic_name(top2vec_model.topic_words[topic],
                                       topic)
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
    text = "{}: {}\n{}\n{}".format(index,
                                   topic_words[0],
                                   topic_words[1],
                                   topic_words[2])
    return text


def get_hierarchy_topic(top2vec_model: Top2Vec) -> dict:
    num_clusters = 20
    hierarchy = top2vec_model.hierarchical_topic_reduction(num_clusters)
    hierarchy_dict = dict(sum([[(raw_id, i)
                                for raw_id in mapping]
                               for i, mapping in enumerate(hierarchy)], []))
    return hierarchy_dict


def get_labels(umap_model: umap.umap_.UMAP, top2vec_model: Top2Vec) -> tuple:
    # Creaciond el modelo HDBSCAN
    cluster_model = hdbscan.HDBSCAN(min_cluster_size=15,
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


params = get_params()
filename = join(params["path data"],
                params["model name"])
model = Top2Vec.load(filename)
umap_args = {
    "n_neighbors": 15,
    "n_components": 2,
    "metric": "cosine",
}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
umap_model = umap.UMAP(**umap_args)
vectors = umap_model.fit(model.document_vectors)
umap.plot.points(
    umap_model,
    ax=ax1,
)
cluster_model = hdbscan.HDBSCAN(min_cluster_size=15,
                                metric='euclidean',
                                cluster_selection_method='eom')
cluster = cluster_model.fit(umap_model.embedding_)
hierarchy_dict = get_hierarchy_topic(model)
clustered, outliers = get_labels(umap_model,
                                 model)
clustered["topic"] = clustered["doc_top"].apply(
    lambda label: hierarchy_dict[label])
centroids = get_centroid_topics(clustered, model)
plt.subplots(figsize=(20, 20))
plt.scatter(clustered.x,
            clustered.y,
            c=clustered["topic"],
            s=1)
for index, data in centroids.items():
    topic_name = data["topic name"]
    centroid = data["centroid"]
    plt.text(centroid[0],
             centroid[1],
             topic_name,
             fontsize=15,
             weight='bold')
plt.axis("off")
plt.savefig("test.png")
