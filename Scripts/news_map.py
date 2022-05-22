"""
Creacion del archivo news_clustered.png a partir del archivo news_clustered.csv
"""
from Modules.functions import get_centroid_topics
from Modules.params import get_params
import matplotlib.pyplot as plt
from pandas import read_csv
from top2vec import Top2Vec
import matplotlib as mpl
from os.path import join

# Lectura de las rutas y nombres de los archivos
params = get_params()
# Nombre del modelo
filename = join(params["path models"],
                params["news model"])
model = Top2Vec.load(filename)
# Nombre del archivo de clusters
filename = join(params["path results"],
                "news_clustered.csv")
clustered = read_csv(filename)
# Cenrtroides de cada cluster
centroids = get_centroid_topics(clustered,
                                model)
bounds = list(range(0, 20))
cmap = mpl.cm.gist_rainbow_r
norm = mpl.colors.BoundaryNorm(bounds,
                               cmap.N)
plt.subplots(figsize=(13, 10))
# Ploteo de los clusters
plt.scatter(clustered.x,
            clustered.y,
            c=clustered["topic"],
            cmap=cmap,
            norm=norm,
            s=1)
# Ploteo de los topicos en el centroide de cada cluster
for index, data in centroids.items():
    topic_name = data["topic name"]
    centroid = data["centroid"]
    plt.text(centroid[0],
             centroid[1],
             topic_name,
             fontsize=12,
             weight='bold')
plt.axis("off")
# Guardado de la grafica
filename = join(params["path graphics"],
                "news_clustered.png")
plt.tight_layout()
plt.savefig(filename)
