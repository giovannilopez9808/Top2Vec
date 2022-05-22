### Organizacion de los archivos

```bash
├── Data
│  ├── Tripadvisor
│  │  ├── Alhóndiga.csv
│  │  ├── Basilica_Colegiata.csv
│  │  ├── Callejón_del_Beso.csv
│  │  ├── Casa_de_Diego_Rivera.csv
│  │  ├── Jardín_de_la_Unión.csv
│  │  ├── Mercado_Hidalgo.csv
│  │  ├── Monumento_Pípila.csv
│  │  ├── Museo_de_las_Momias.csv
│  │  ├── opinions.csv
│  │  ├── Teatro_Juárez.csv
│  │  └── Universidad_de_Guanajuato.csv
│  └── Yahoo
├── Graphics
│  ├── news_clustered.png
│  ├── news_clustered_2.png
│  ├── tripadvisor_clustered.png
│  └── yahoo_clustered.png
├── Models
│  ├── news_model.h5
│  ├── tripadvisor_model.h5
│  └── yahoo_model.h5
├── Modules
│  ├── functions.py
│  ├── params.py
│  └── yahoo_model.py
├── Notebooks
│  ├── news_clustered.ipynb
│  ├── news_map.ipynb
│  ├── news_test.ipynb
│  ├── news_train.ipynb
│  ├── tripadvisor_clustered.ipynb
│  ├── tripadvisor_map.ipynb
│  ├── tripadvisor_test.ipynb
│  ├── tripadvisor_train.ipynb
│  ├── yahoo_clustered.ipynb
│  ├── yahoo_map.ipynb
│  ├── yahoo_test.ipynb
│  └── yahoo_train.ipynb
├── Results
│  ├── news_clustered.csv
│  ├── tripadvisor_clustered.csv
│  └── yahoo_clustered.csv
├── README.md
├── requeriments.txt
├── news_clustered.py
├── news_map.py
├── news_train.py
├── tripadvisor_clustered.py
├── tripadvisor_map.py
├── tripadvisor_train.py
├── yahoo_clustered.py
├── yahoo_map.py
└── yahoo_train.py
```

#### Scripts

- `_map.py`: Genera el mapa semantico de los documentos con los topicos relacionados

- `_train.py`: Entrena el modelo de Top2Vec con el dataset dado

- `_clustered.py`: Genera el documento `_clustered.csv` para el dataset dado

#### Yahoo dataset

El dataset de yahoo Answers puede ser obtenido a partir del siguiente comando

```bash
wget https://drive.google.com/uc?export=download&id=0Bz8a_Dbh9Qhbd2JNdDBsQUdocVU&confirm=t -O yahoo_answers.csv.tar.gz
```
