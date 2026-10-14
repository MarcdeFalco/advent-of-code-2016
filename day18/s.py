"""Advent of Code 2016, jour 18 : automate cellulaire à une dimension.

Chaque ligne se déduit de la précédente par une règle sur trois cases (les
cases hors de la ligne sont sûres) ; les quatre cas de `piege` reviennent à
« la case de gauche diffère de celle de droite ». On ne garde que la ligne
courante et on compte les cases sûres sur 40 puis 400 000 lignes.
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return [c == "^" for c in fichier.read().strip()]


def piege(gauche, centre, droite):
    return ((gauche and centre and not droite)
            or (centre and droite and not gauche)
            or (gauche and not centre and not droite)
            or (droite and not centre and not gauche))


def ligne_suivante(ligne):
    gauche = False
    centre = ligne[0]
    suivante = []
    for droite in ligne[1:] + [False]:
        suivante.append(piege(gauche, centre, droite))
        gauche, centre = centre, droite
    return suivante


def cases_sures(ligne, nombre_lignes):
    total = 0
    for _ in range(nombre_lignes):
        total += ligne.count(False)
        ligne = ligne_suivante(ligne)
    return total


def partie1(ligne):
    return cases_sures(ligne, 40)


def partie2(ligne):
    return cases_sures(ligne, 400000)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
