"""Advent of Code 2016, jour 2 : déplacements sur un clavier.

Le clavier est une grille de caractères ; la position avance seulement si la
case visée existe (dans la grille et différente d'un espace). Le clavier carré
(partie 1) et le clavier en losange (partie 2) utilisent la même fonction.
"""

PAS = {"U": (0, -1), "L": (-1, 0), "R": (1, 0), "D": (0, 1)}
CLAVIER_CARRE = ["123", "456", "789"]
CLAVIER_LOSANGE = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def code(clavier, x, y, lignes):
    """Code obtenu en partant de la case (x, y) du clavier."""
    taille = len(clavier)
    resultat = ""
    for ligne in lignes:
        for lettre in ligne:
            dx, dy = PAS[lettre]
            if (0 <= x + dx < taille and 0 <= y + dy < taille
                    and clavier[y + dy][x + dx] != " "):
                x += dx
                y += dy
        resultat += clavier[y][x]
    return resultat


def partie1(lignes):
    return code(CLAVIER_CARRE, 1, 1, lignes)  # départ sur le 5


def partie2(lignes):
    return code(CLAVIER_LOSANGE, 0, 2, lignes)  # départ sur le 5


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
