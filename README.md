# Vélib’ · Cartographier et contrôler un réseau de stations

Projet d’équipe. À partir d’un instantané des stations, deux cartes permettent d’étudier leurs voisinages, leurs capacités et leurs connexions géométriques dans Paris et les communes voisines.

![Carte de Voronoï du réseau Vélib’](docs/voronoi-velib.jpg)

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

~~~sh
python -m pip install -r requirements.txt
python carte.py
python carte_voronoi
~~~

Les deux fichiers JSON dérivés sont déjà fournis. Ils peuvent être régénérés avec `python code.py` puis `python coordonnés.py`. Les cartes colorent des rapports entre capacité et nombre de voisins géométriques. Cette mesure ne représente pas la fréquentation réelle.

Source de l’instantané du 20 janvier 2025 : [données ouvertes Vélib’ Métropole](https://www.data.gouv.fr/datasets/velib-localisation-et-caracteristique-des-stations). Fond de carte : [contributeurs OpenStreetMap](https://www.openstreetmap.org/copyright).

[Projet dans le portfolio](https://kajan94.github.io/#velib)
