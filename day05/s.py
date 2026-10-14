"""Advent of Code 2016, jour 5 : code construit à partir de hachés MD5.

Force brute sur les entiers successifs : on garde les hachés de « clé + i »
qui commencent par cinq zéros. Partie 1 : le sixième caractère est le chiffre
suivant du code. Partie 2 : le sixième donne la position, le septième la
valeur, la première occurrence pour une position l'emportant.
"""
from hashlib import md5


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip()


def hache(cle, i):
    return md5((cle + str(i)).encode("ascii")).hexdigest()


def partie1(cle):
    code = ""
    i = 0
    while len(code) < 8:
        h = hache(cle, i)
        if h[:5] == "00000":
            code += h[5]
        i += 1
    return code


def partie2(cle):
    code = [None] * 8
    i = 0
    while None in code:
        h = hache(cle, i)
        if h[:5] == "00000" and h[5] in "01234567":
            position = int(h[5])
            if code[position] is None:
                code[position] = h[6]
        i += 1
    return "".join(code)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
