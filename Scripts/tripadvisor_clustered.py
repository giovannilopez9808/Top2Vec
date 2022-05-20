from Modules.functions import get_labels, get_hierarchy_topic
from Modules.params import get_params
from top2vec import Top2Vec
from os.path import join
import hdbscan
import umap

params = get_params()
filename = join(params["path models"],
                params["tripadvisor model"])
model = Top2Vec.load(filename)
umap_args = {
    "n_neighbors": 15,
    "n_components": 2,
    "metric": "cosine",
}
umap_model = umap.UMAP(**umap_args)
vectors = umap_model.fit(model.document_vectors)
cluster_model = hdbscan.HDBSCAN(min_cluster_size=16,
                                metric='euclidean',
                                cluster_selection_method='eom')
cluster = cluster_model.fit(umap_model.embedding_)
hierarchy_dict = get_hierarchy_topic(model, 15)
clustered, outliers = get_labels(umap_model,
                                 model)
clustered["topic"] = clustered["doc_top"].apply(
    lambda label: hierarchy_dict[label])
filename = join(params["path results"],
                "tripadvisor_clustered.csv")
clustered.to_csv(filename,
                 index=False)
