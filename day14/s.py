"""Advent of Code 2016, jour 14 : clés repérées dans des hachés successifs.

Un indice est une clé si son haché contient un triplet (seul le premier
compte) et si l'un des 1000 hachés suivants contient le même caractère cinq
fois. On garde ces 1000 hachés dans une file : à chaque pas on retire le plus
ancien et on ajoute le suivant, si bien que chaque haché est calculé une
seule fois, ce qui compte pour la partie 2 (2017 appels à MD5 par haché).
"""
from collections import deque
from hashlib import md5


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip()


def hache(sel, i, repetitions):
    s = sel + str(i)
    for _ in range(repetitions):
        s = md5(s.encode("ascii")).hexdigest()
    return s


def indice_64e_cle(sel, repetitions):
    courant = hache(sel, 0, repetitions)
    suivant = 1001  # prochain indice à hacher
    fenetre = deque(hache(sel, i, repetitions) for i in range(1, suivant))
    cles = []
    while True:
        for i in range(len(courant) - 2):
            c = courant[i]
            if courant[i + 1] == c and courant[i + 2] == c:
                if any(c * 5 in h for h in fenetre):
                    cles.append(suivant - 1001)  # indice de `courant`
                break  # seul le premier triplet est pris en compte
        if len(cles) == 64:
            return cles[-1]
        courant = fenetre.popleft()
        fenetre.append(hache(sel, suivant, repetitions))
        suivant += 1


def partie1(sel):
    return indice_64e_cle(sel, 1)


def partie2(sel):
    return indice_64e_cle(sel, 2017)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
