"""Advent of Code 2016, jour 1 : marche sur une grille avec virages.

La direction est un indice dans la liste des quatre vecteurs, tournée modulo 4.
On avance case par case : la partie 1 donne la distance de Manhattan du point
d'arrivée, la partie 2 celle du premier point visité deux fois.
"""

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split(", ")


def cases_visitees(instructions):
    """Engendre les cases successives, une par pas."""
    direction = 0
    x, y = 0, 0
    for instruction in instructions:
        virage, longueur = instruction[0], int(instruction[1:])
        if virage == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        dx, dy = DIRECTIONS[direction]
        for _ in range(longueur):
            x, y = x + dx, y + dy
            yield x, y


def partie1(instructions):
    for x, y in cases_visitees(instructions):
        pass
    return abs(x) + abs(y)


def partie2(instructions):
    deja_vues = []  # une liste : le test « in » est linéaire, suffisant ici
    for x, y in cases_visitees(instructions):
        if (x, y) in deja_vues:
            return abs(x) + abs(y)
        deja_vues.append((x, y))


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
