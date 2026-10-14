"""Advent of Code 2016, jour 20 : entiers non couverts par des intervalles.

On part de l'intervalle complet des adresses autorisées et on lui soustrait
chaque intervalle bloqué : chaque intervalle autorisé est gardé, raccourci,
coupé en deux ou supprimé selon sa position. La liste reste triée : son
premier élément donne la partie 1, la somme des longueurs la partie 2.
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return [tuple(map(int, ligne.split("-")))
                for ligne in fichier.read().strip().split("\n")]


def autorises(blocs):
    intervalles = [(0, 4294967295)]
    for bas, haut in blocs:
        restants = []
        for a, b in intervalles:
            if bas <= a <= haut:  # début couvert
                if haut < b:
                    restants.append((haut + 1, b))
            elif bas <= b <= haut:  # fin couverte
                restants.append((a, bas - 1))
            elif a < bas <= haut < b:  # bloc strictement à l'intérieur
                restants.append((a, bas - 1))
                restants.append((haut + 1, b))
            else:  # disjoints
                restants.append((a, b))
        intervalles = restants
    return intervalles


def partie1(blocs):
    return autorises(blocs)[0][0]


def partie2(blocs):
    return sum(b - a + 1 for a, b in autorises(blocs))


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
