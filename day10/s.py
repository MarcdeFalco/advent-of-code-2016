"""Advent of Code 2016, jour 10 : robots qui se passent des jetons.

Les règles de chaque robot sont dans un dictionnaire, les jetons tenus dans
un defaultdict(list). Tant qu'un robot tient deux jetons, il les transmet
(le plus petit puis le plus grand) ; on recommence la recherche depuis le
début après chaque transfert. Partie 2 : produit des sorties 0, 1 et 2.
Partie 1 : pas de solution.
"""
from collections import defaultdict


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def simule(lignes):
    robots = defaultdict(list)
    regles = {}
    for ligne in lignes:
        mots = ligne.split()
        if mots[0] == "value":
            robots[int(mots[5])].append(int(mots[1]))
        else:
            # robot -> (type et numéro du destinataire bas, idem pour haut)
            regles[int(mots[1])] = (mots[5], int(mots[6]),
                                    mots[10], int(mots[11]))

    sorties = defaultdict(list)
    change = True
    while change:
        change = False
        for robot in robots:
            if len(robots[robot]) == 2:
                change = True
                bas, haut = sorted(robots[robot])
                type_bas, num_bas, type_haut, num_haut = regles[robot]
                if type_bas == "bot":
                    robots[num_bas].append(bas)
                else:
                    sorties[num_bas].append(bas)
                if type_haut == "bot":
                    robots[num_haut].append(haut)
                else:
                    sorties[num_haut].append(haut)
                robots[robot] = []
                break  # le dictionnaire a pu changer : on recommence
    return sorties


def partie2(lignes):
    sorties = simule(lignes)
    return sorties[0][0] * sorties[1][0] * sorties[2][0]


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 2 :", partie2(donnees))
