"""Advent of Code 2016, jour 17 : chemins dont les portes dépendent d'un haché.

Les portes ouvertes dépendent du haché MD5 du code suivi du chemin parcouru :
l'état doit donc contenir le chemin entier. Un parcours en largeur sur les
couples (position, chemin) énumère tous les chemins jusqu'à la sortie ; il
termine parce que les portes finissent par se fermer. Le premier chemin
trouvé est le plus court (partie 1), on garde la longueur du plus long
(partie 2).
"""
from collections import deque
from hashlib import md5

LARGEUR, HAUTEUR = 4, 4
SORTIE = (3, 3)
PAS = [("U", 0, -1), ("D", 0, 1), ("L", -1, 0), ("R", 1, 0)]


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip()


def chemins_vers_sortie(code):
    """Liste des chemins menant à la sortie, par longueur croissante."""
    # appendleft pour enfiler, pop pour défiler
    a_visiter = deque([((0, 0), code)])
    chemins = []
    while len(a_visiter) != 0:
        (x, y), chemin = a_visiter.pop()
        if (x, y) == SORTIE:
            chemins.append(chemin[len(code):])
            continue
        portes = md5(chemin.encode("ascii")).hexdigest()[:4]
        for porte, (lettre, dx, dy) in zip(portes, PAS):
            dans_grille = 0 <= x + dx < LARGEUR and 0 <= y + dy < HAUTEUR
            if porte in "bcdef" and dans_grille:
                a_visiter.appendleft(((x + dx, y + dy), chemin + lettre))
    return chemins


def partie1(code):
    return chemins_vers_sortie(code)[0]


def partie2(code):
    return max(len(c) for c in chemins_vers_sortie(code))


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
