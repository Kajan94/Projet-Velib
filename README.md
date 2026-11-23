# Vélib’ · Cartographier et contrôler un réseau de stations

Projet d’équipe. À partir d’un instantané des stations, deux cartes permettent d’étudier leurs voisinages, leurs capacités et leurs connexions géométriques dans Paris et les communes voisines.

![Carte de Voronoï du réseau Vélib’](docs/voronoi-velib.jpg)

Le projet d’équipe étudiait aussi un scénario de raccordement électrique des stations. L’arbre couvrant minimum relie les stations dans le modèle sans cycle. Les zones de Voronoï aident à lire la proximité géométrique des stations.

## Explorer les deux cartes

- **Voisinages** — la [carte du réseau](https://kajan94.github.io/Projet-Velib/velib_stations_map.html) relie les stations par triangulation de Delaunay et affiche un arbre couvrant de poids minimal construit avec Kruskal.
- **Zones de proximité** — la [carte de Voronoï](https://kajan94.github.io/Projet-Velib/velib_stations_voronoi.html) montre les cellules associées aux stations. Les cellules non bornées ne sont pas affichées.

Les cartes s’ouvrent dans le navigateur. Les fichiers HTML versionnés permettent aussi une consultation locale. Une connexion Internet charge les bibliothèques et le fond de carte. Le menu des calques permet de comparer les représentations. Les résultats décrivent la géométrie du réseau. L’analyse de la disponibilité en temps réel demanderait d’autres données.

## Contrôler l’instantané

~~~sh
python analyser_stations.py
~~~

[Ce script Python](analyser_stations.py) fonctionne sans dépendance externe. Il signale les identifiants dupliqués, les coordonnées hors limites et les capacités invalides. Pour l’instantané fourni, il affiche **1 473 stations**, **46 036 places** et une **capacité médiane de 29**. Les 11 stations à capacité nulle sont comptées séparément.

### Régénérer les cartes

Bibliothèques à installer :

- **folium 0.20.0** : cartes interactives.
- **numpy 2.5.4** : calculs numériques.
- **scipy 1.18.1** : calculs géométriques.

Depuis un terminal à la racine du dépôt, installer les bibliothèques puis lancer les scripts :

~~~sh
python -m pip install -r requirements.txt
python carte.py
python carte_voronoi
~~~

Sur macOS ou Linux, utiliser `python3` à la place de `python` si nécessaire.

Les deux fichiers JSON dérivés sont déjà fournis. Ils peuvent être régénérés avec `python code.py` puis `python coordonnés.py`. Les cartes colorent des rapports entre capacité et nombre de voisins géométriques. Cette mesure ne représente pas la fréquentation réelle.

## Organisation du code

| Chemin | Rôle |
| --- | --- |
| `station_information.json` | Instantané source des informations des stations Vélib’. |
| `code.py` et `coordonnés.py` | Extraction des informations utiles et des coordonnées depuis l’instantané source. |
| `velib_stations.json` et `velib_coordonnées.json` | Données préparées pour les calculs et la génération des cartes. |
| `analyser_stations.py` | Contrôle des identifiants, coordonnées et capacités des stations. |
| `carte.py` | Génération de la carte de Delaunay et de l’arbre couvrant minimum. |
| `carte_voronoi` | Génération de la carte des cellules de Voronoï et des calques du réseau. |
| `triangles.py` et `Liste_adjacence` | Scripts d’étude de la triangulation et des voisinages entre stations. |
| `velib_stations_map.html` et `velib_stations_voronoi.html` | Cartes générées, consultables directement dans le navigateur. |

Source de l’instantané du 20 janvier 2025 : [données ouvertes Vélib’ Métropole](https://www.data.gouv.fr/datasets/velib-localisation-et-caracteristique-des-stations). Fond de carte : [contributeurs OpenStreetMap](https://www.openstreetmap.org/copyright).

[Projet dans le portfolio](https://kajan94.github.io/Portefolio/#velib)
