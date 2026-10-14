"""Advent of Code 2016, jour 11 : transport d'objets entre étages.

Parcours en largeur sur les états du casse-tête. Un état est un couple
(étage de l'ascenseur, quatre n-uplets triés d'objets) : le tri donne une
représentation canonique et hachable. Les voisins s'obtiennent en emmenant
un ou deux objets à l'étage voisin ; `valide` élimine les états interdits
(une puce sans son générateur à côté d'un autre générateur).
"""
from collections import defaultdict, deque
from itertools import combinations


def lire_entree(nom="input.txt"):
    """Liste de quatre listes de couples (élément, 'G' ou 'M')."""
    etages = [[], [], [], []]
    with open(nom) as fichier:
        lignes = fichier.read().strip().split("\n")
    for numero in range(4):
        ligne = lignes[numero]
        ligne = ligne[ligne.index("contains") + len("contains "):]
        if ligne == "nothing relevant.":
            continue
        if ", and" in ligne:
            debut, fin = ligne[:-1].split(", and ")
            objets = debut.split(", ") + [fin]
        else:
            objets = ligne[:-1].split(" and ")
        for objet in objets:
            mots = objet.split()
            # on désigne un élément par ses deux premières lettres
            if mots[2] == "generator":
                etages[numero].append((mots[1][0:2], "G"))
            else:
                element = mots[1].split("-")[0]
                etages[numero].append((element[0:2], "M"))
    return etages


def complet(etat):
    return all(len(etage) == 0 for etage in etat[1][:3])


def valide(etat):
    for etage in etat[1]:
        a_generateur = any(genre == "G" for _, genre in etage)
        for element, genre in etage:
            if a_generateur and genre == "M" and (element, "G") not in etage:
                return False
    return True


def nombre_deplacements(etages):
    initial = (0, tuple(tuple(etage) for etage in etages))
    a_visiter = deque([initial])  # appendleft pour enfiler, pop pour défiler
    visite = defaultdict(bool)
    distance = {initial: 0}
    while len(a_visiter) != 0:
        etat = a_visiter.pop()
        if visite[etat]:
            continue
        visite[etat] = True
        ascenseur, contenu = etat
        if complet(etat):
            return distance[etat]
        for direction in [-1, 1]:
            if not 0 <= ascenseur + direction <= 3:
                continue
            arrivee = ascenseur + direction
            voisins = []
            depart = contenu[ascenseur]
            for objet in depart:
                nouveau = list(contenu)
                nouveau[arrivee] = tuple(sorted(contenu[arrivee] + (objet,)))
                nouveau[ascenseur] = tuple(sorted(o for o in depart
                                                  if o != objet))
                voisins.append(tuple(nouveau))
            for a, b in combinations(depart, 2):
                nouveau = list(contenu)
                nouveau[arrivee] = tuple(sorted(contenu[arrivee] + (a, b)))
                nouveau[ascenseur] = tuple(sorted(o for o in depart
                                                  if o != a and o != b))
                voisins.append(tuple(nouveau))
            for voisin in voisins:
                suivant = (arrivee, voisin)
                if suivant not in distance and valide(suivant):
                    distance[suivant] = 1 + distance[etat]
                    a_visiter.appendleft(suivant)


def partie1(etages):
    return nombre_deplacements(etages)


def partie2(etages):
    # deux paires supplémentaires au rez-de-chaussée : elerium et dilithium
    supplement = [("el", "G"), ("el", "M"), ("di", "G"), ("di", "M")]
    etages = [etages[0] + supplement] + etages[1:]
    return nombre_deplacements(etages)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
