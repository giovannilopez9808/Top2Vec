import matplotlib.pyplot as plt
from params import get_params
from pandas import DataFrame
from top2vec import Top2Vec
from os.path import join
import umap.plot
import hdbscan
import umap


def get_labels(umap_model: umap.umap_.UMAP) -> tuple:
    # Creaciond el modelo HDBSCAN
    cluster_model = hdbscan.HDBSCAN(min_cluster_size=15,
                                    metric='euclidean',
                                    cluster_selection_method='eom')
    # Obtiene los topicos
    cluster = cluster_model.fit(umap_model.embedding_)
    result = DataFrame(umap_model.embedding_, columns=["x", "y"])
    result["labels"] = cluster.labels_
    outliers = result.loc[result.labels == -1, :]
    clustered = result.loc[result.labels != -1, :]
    return clustered, outliers


params = get_params()
filename = join(params["path data"], params["model name"])
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

clustered, outliers = get_labels(umap_model)
ax2.scatter(
    outliers.x,
    outliers.y,
    color='#d11518',
    s=0.4,
)
ax2.scatter(
    clustered.x,
    clustered.y,
    c=clustered.labels,
    s=1,
    cmap='winter',
)
ax1.axis("off")
ax2.axis("off")
plt.savefig("test.png", dpi=400)
