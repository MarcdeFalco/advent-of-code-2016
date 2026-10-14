"""Advent of Code 2016, jour 19 : élimination en cercle (variante de Josèphe).

Partie 1 : on fait tourner une file, le premier passe en queue et le suivant
est éliminé. Partie 2 (on élimine la personne d'en face) : le cercle est
coupé en deux files, la première moitié (joueur courant en tête) et la
seconde ; la personne d'en face est à la jonction, ce qui donne chaque
élimination en O(1).
"""
from collections import deque


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return int(fichier.read().strip())


def partie1(nombre):
    cercle = deque(range(1, nombre + 1))
    while len(cercle) > 1:
        cercle.append(cercle.popleft())
        cercle.popleft()
    return cercle[0]


def partie2(nombre):
    moitie1 = deque(range(1, nombre // 2 + 2))
    moitie2 = deque(range(nombre // 2 + 2, nombre + 1))
    while (len(moitie1), len(moitie2)) != (1, 0):
        # la personne d'en face : queue de moitie1 ou tête de moitie2
        if len(moitie1) != len(moitie2):
            moitie1.pop()
        else:
            moitie2.popleft()
        # rotation d'un cran, qui rééquilibre les deux moitiés
        moitie2.append(moitie1.popleft())
        moitie1.append(moitie2.popleft())
    return moitie1[0]


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
