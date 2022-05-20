from Modules.functions import get_centroid_topics
from Modules.params import get_params
import matplotlib.pyplot as plt
from pandas import read_csv
from top2vec import Top2Vec
import matplotlib as mpl
from os.path import join

params = get_params()
filename = join(params["path models"],
                params["tripadvisor model"])
model = Top2Vec.load(filename)
filename = join(params["path results"],
                "tripadvisor_clustered.csv")
clustered = read_csv(filename)
centroids = get_centroid_topics(clustered,
                                model)
bounds = list(range(0, 15))
cmap = mpl.cm.gist_rainbow_r
norm = mpl.colors.BoundaryNorm(bounds,
                               cmap.N)
plt.subplots(figsize=(13, 10))
plt.scatter(clustered.x,
            clustered.y,
            c=clustered["topic"],
            cmap=cmap,
            norm=norm,
            s=1)
for index, data in centroids.items():
    topic_name = data["topic name"]
    centroid = data["centroid"]
    plt.text(centroid[0],
             centroid[1],
             topic_name,
             fontsize=12,
             weight='bold')
plt.axis("off")
filename = join(params["path graphics"],
                "tripadvisor_clustered.png")
plt.savefig(filename)
