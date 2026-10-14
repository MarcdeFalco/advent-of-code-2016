"""Advent of Code 2016, jour 3 : triplets qui forment un triangle.

On teste l'inégalité triangulaire sur chaque ligne (partie 1). Pour la
partie 2, on concatène les trois colonnes et on découpe par blocs de trois :
le nombre de lignes étant un multiple de 3, on obtient les triplets verticaux.
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return [tuple(map(int, ligne.split()))
                for ligne in fichier.read().strip().split("\n")]


def est_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def partie1(lignes):
    return sum(1 for a, b, c in lignes if est_triangle(a, b, c))


def partie2(lignes):
    colonnes = ([a for a, _, _ in lignes] + [b for _, b, _ in lignes]
                + [c for _, _, c in lignes])
    return sum(1 for i in range(0, len(colonnes), 3)
               if est_triangle(*colonnes[i:i + 3]))


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
