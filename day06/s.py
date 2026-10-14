"""Advent of Code 2016, jour 6 : caractère le plus ou moins fréquent par colonne.

Pour chaque colonne, on trie la liste des couples (effectif, caractère) :
le dernier élément est le plus fréquent (partie 1), le premier le moins
fréquent (partie 2).
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def effectifs_tries(lignes, i):
    colonne = [ligne[i] for ligne in lignes]
    return sorted((colonne.count(c), c) for c in set(colonne))


def partie1(lignes):
    return "".join(effectifs_tries(lignes, i)[-1][1]
                   for i in range(len(lignes[0])))


def partie2(lignes):
    return "".join(effectifs_tries(lignes, i)[0][1]
                   for i in range(len(lignes[0])))


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
