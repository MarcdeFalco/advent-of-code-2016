"""Advent of Code 2016, jour 8 : rotations de lignes et de colonnes d'un écran.

L'écran est une liste de listes de 0 et de 1. Une rotation de ligne se fait
en une compréhension avec des indices modulo la largeur ; une rotation de
colonne passe par une liste temporaire. Partie 1 : nombre de pixels allumés ;
partie 2 : le texte se lit sur l'écran affiché.
"""

LARGEUR, HAUTEUR = 50, 6


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def simule(instructions):
    ecran = [[0] * LARGEUR for _ in range(HAUTEUR)]
    for instruction in instructions:
        mots = instruction.split()
        if mots[0] == "rect":
            largeur, hauteur = map(int, mots[1].split("x"))
            for x in range(largeur):
                for y in range(hauteur):
                    ecran[y][x] = 1
        elif mots[0] == "rotate":
            n = int(mots[2].split("=")[1])
            decalage = int(mots[4])
            if mots[1] == "row":
                ecran[n] = [ecran[n][(k - decalage) % LARGEUR]
                            for k in range(LARGEUR)]
            else:
                colonne = [ecran[(k - decalage) % HAUTEUR][n]
                           for k in range(HAUTEUR)]
                for k in range(HAUTEUR):
                    ecran[k][n] = colonne[k]
    return ecran


def partie1(instructions):
    return sum(sum(ligne) for ligne in simule(instructions))


def partie2(instructions):
    return "\n".join("".join("#" if v else "." for v in ligne)
                     for ligne in simule(instructions))


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :")
    print(partie2(donnees))
