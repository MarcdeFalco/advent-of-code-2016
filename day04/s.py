"""Advent of Code 2016, jour 4 : sommes de contrôle et chiffre de César.

Une expression régulière sépare nom, numéro et somme de contrôle. Trier les
couples (-effectif, lettre) ordonne par fréquence décroissante puis par ordre
alphabétique en un seul tri. Le déchiffrement est un décalage de César.
L'espace (issu des tirets) n'entre pas dans le comptage des lettres.
"""
import re

MOTIF_SALLE = re.compile(r"(?P<nom>.*)-(?P<num>\d+)\[(?P<somme>.*)\]")


def lire_entree(nom="input.txt"):
    salles = []
    with open(nom) as fichier:
        for ligne in fichier.read().strip().split("\n"):
            m = MOTIF_SALLE.match(ligne)
            salles.append((m.group("nom").replace("-", " "),
                           int(m.group("num")), m.group("somme")))
    return salles


def somme_controle(nom):
    effectifs = sorted((-nom.count(c), c) for c in set(nom) if c != " ")
    return "".join(c for _, c in effectifs[:5])


def dechiffre(nom, decalage):
    return "".join(" " if c == " "
                   else chr(ord("a") + (ord(c) - ord("a") + decalage) % 26)
                   for c in nom)


def partie1(salles):
    return sum(num for nom, num, somme in salles
               if somme == somme_controle(nom))


def partie2(salles):
    for nom, num, _ in salles:
        if "northpole" in dechiffre(nom, num):
            return num


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
