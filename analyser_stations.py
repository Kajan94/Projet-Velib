"""Résumer et contrôler un instantané des stations Vélib’ (GBFS)."""

import argparse
import json
import math
import statistics
from pathlib import Path


def resumer_stations(stations):
    identifiants = set()
    capacites = []
    for station in stations:
        identifiant = station['station_id']
        capacite = station['capacity']
        latitude = station['lat']
        longitude = station['lon']
        if identifiant in identifiants:
            raise ValueError(f"Identifiant de station en double : {identifiant}")
        if type(capacite) is not int or capacite < 0:
            raise ValueError(f"Capacité invalide : {identifiant}")
        if not (math.isfinite(latitude) and -90 <= latitude <= 90
                and math.isfinite(longitude) and -180 <= longitude <= 180):
            raise ValueError(f"Coordonnées invalides : {identifiant}")
        identifiants.add(identifiant)
        capacites.append(capacite)

    if not capacites:
        raise ValueError("L’instantané ne contient aucune station.")
    return {
        "stations": len(identifiants),
        "capacité_totale": sum(capacites),
        "capacité_médiane": statistics.median(capacites),
        "capacité_maximale": max(capacites),
        "stations_à_capacité_nulle": capacites.count(0),
    }


def main():
    parser = argparse.ArgumentParser(description="Contrôler le fichier GBFS des stations.")
    parser.add_argument("fichier", nargs="?", type=Path,
                        default=Path(__file__).with_name("station_information.json"))
    options = parser.parse_args()
    try:
        instantane = json.loads(options.fichier.read_text(encoding="utf-8"))
        resume = resumer_stations(instantane["data"]["stations"])
    except (OSError, KeyError, TypeError, ValueError) as erreur:
        parser.error(str(erreur))
    print(json.dumps(resume, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
