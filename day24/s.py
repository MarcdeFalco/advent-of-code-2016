"""Advent of Code 2016, jour 24 : visiter tous les points marqués d'un plan.

Un parcours en largeur entre chaque paire de points marqués donne la matrice
des distances ; on essaie ensuite toutes les permutations des points autres
que 0 (voyageur de commerce par force brute), sans retour au départ en
partie 1, avec retour en partie 2.
"""
from collections import deque
from itertools import permutations, product


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def matrice_distances(lignes):
    largeur, hauteur = len(lignes[0]), len(lignes)
    libre = {}
    points = {}
    for x, y in product(range(largeur), range(hauteur)):
        libre[x, y] = lignes[y][x] != "#"
        if lignes[y][x] not in ".#":
            points[int(lignes[y][x])] = (x, y)

    def voisins(x, y):
        # le plan est bordé de murs : pas de test de sortie de la grille
        return [(x + dx, y + dy)
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]
                if libre[x + dx, y + dy]]

    def distance(depart, arrivee):
        a_visiter = deque([(0, depart)])
        vus = set()
        while len(a_visiter) > 0:
            d, case = a_visiter.popleft()
            if case == arrivee:
                return d
            for voisin in voisins(*case):
                if voisin not in vus:
                    vus.add(voisin)
                    a_visiter.append((d + 1, voisin))
        raise ValueError

    n = max(points) + 1
    distances = {}
    for k, l in product(range(n), repeat=2):
        if k < l:
            distances[k, l] = distances[l, k] = distance(points[k], points[l])
    return n, distances


def plus_court_trajet(lignes, retour):
    n, distances = matrice_distances(lignes)
    meilleur = None
    for ordre in permutations(range(1, n)):
        trajet = (0,) + ordre + ((0,) if retour else ())
        longueur = sum(distances[trajet[i], trajet[i + 1]]
                       for i in range(len(trajet) - 1))
        if meilleur is None or longueur < meilleur:
            meilleur = longueur
    return meilleur


def partie1(lignes):
    return plus_court_trajet(lignes, retour=False)


def partie2(lignes):
    return plus_court_trajet(lignes, retour=True)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
