"""Advent of Code 2016, jour 16 : courbe du dragon et somme de contrôle.

On applique la construction (chaîne, 0, chaîne retournée et complémentée)
jusqu'à dépasser la longueur voulue, on tronque, puis on réduit par paires
(1 si les deux caractères sont égaux) tant que la longueur est paire.
Tout se fait sur des chaînes Python : environ 35 millions de caractères en
partie 2, ce qui prend du temps et de la mémoire.
"""

COMPLEMENT = {"0": "1", "1": "0"}


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip()


def dragon(s):
    return s + "0" + "".join(COMPLEMENT[c] for c in reversed(s))


def somme_controle(etat_initial, longueur):
    s = etat_initial
    while len(s) < longueur:
        s = dragon(s)
    s = s[:longueur]
    while len(s) % 2 == 0:
        s = "".join("1" if s[2 * i] == s[2 * i + 1] else "0"
                    for i in range(len(s) // 2))
    return s


def partie1(etat_initial):
    return somme_controle(etat_initial, 272)


def partie2(etat_initial):
    return somme_controle(etat_initial, 35651584)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
