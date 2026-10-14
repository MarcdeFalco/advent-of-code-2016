"""Advent of Code 2016, jour 13 : labyrinthe défini par une formule.

La grille n'est jamais construite : `est_mur` décide d'une case par la parité
du nombre de bits à 1 d'un polynôme en (x, y). Parcours en largeur depuis
(1, 1) : distance jusqu'à (31, 39) en partie 1 ; en partie 2, on arrête
l'exploration à la profondeur 50 et on compte les cases visitées.
La limite de profondeur 50 ne s'applique pas en partie 1 : la cible est
plus loin.
"""
from collections import defaultdict, deque

CIBLE = (31, 39)


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return int(fichier.read().strip())


def est_mur(x, y, n):
    v = x * x + 3 * x + 2 * x * y + y + y * y + n
    return bin(v)[2:].count("1") % 2 == 1


def parcours(n, cible=None, profondeur_max=None):
    """Distance jusqu'à la cible, ou nombre de cases visitées sans cible."""
    a_visiter = deque([(1, 1)])  # appendleft pour enfiler, pop pour défiler
    visite = defaultdict(bool)
    distance = {(1, 1): 0}
    while len(a_visiter) != 0:
        x, y = a_visiter.pop()
        if (x, y) == cible:
            return distance[x, y]
        if visite[x, y]:
            continue
        visite[x, y] = True
        if distance[x, y] == profondeur_max:
            continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            voisin = (x + dx, y + dy)
            if 0 <= voisin[0] and 0 <= voisin[1] and not est_mur(*voisin, n):
                if voisin not in distance:
                    distance[voisin] = 1 + distance[x, y]
                    a_visiter.appendleft(voisin)
    return sum(1 for case in visite if visite[case])


def partie1(n):
    return parcours(n, cible=CIBLE)


def partie2(n):
    return parcours(n, profondeur_max=50)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
