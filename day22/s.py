"""Advent of Code 2016, jour 22 : déplacer une donnée dans une grille de nœuds.

On voit la grille comme un taquin : un seul nœud vide, et la donnée cible,
partie du coin (xmax, 0), à amener en (0, 0). On enchaîne des parcours en
largeur sur les états complets de la grille : d'abord amener la case vide
jusqu'au coin de la donnée (ce qui décale celle-ci d'un cran), puis déplacer
la donnée d'un cran vers la gauche à chaque fois. Chaque recherche identifie
les états par la position de la case vide (et de la donnée).
Partie 1 : pas de solution.
"""
from collections import defaultdict, deque


def lire_entree(nom="input.txt"):
    """Dictionnaire (x, y) -> (utilisé, disponible, contient la cible)."""
    noeuds = {}
    with open(nom) as fichier:
        for ligne in fichier.read().strip().split("\n")[2:]:
            nom_noeud, _, utilise, disponible, _ = ligne.split()
            _, x, y = nom_noeud.split("-")
            noeuds[int(x[1:]), int(y[1:])] = (int(utilise[:-1]),
                                              int(disponible[:-1]), False)
    return noeuds


def deplace(grille, depart, arrivee):
    """Grille obtenue en vidant le nœud `depart` dans le nœud `arrivee`."""
    nouvelle = grille.copy()
    u1, a1, cible1 = nouvelle[depart]
    u2, a2, cible2 = nouvelle[arrivee]
    nouvelle[arrivee] = (u1 + u2, a2 - u1, cible1 or cible2)
    nouvelle[depart] = (0, a1 + u1, False)
    return nouvelle


def deplacements(grille):
    """Grilles accessibles en un transfert vers un nœud voisin assez libre."""
    resultat = []
    for (x, y) in grille:
        if grille[x, y][0] > 0:
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                voisin = (x + dx, y + dy)
                if voisin in grille and grille[x, y][0] < grille[voisin][1]:
                    resultat.append(deplace(grille, (x, y), voisin))
    return resultat


def case_vide(grille):
    for case in grille:
        if grille[case][0] == 0:
            return case
    raise ValueError


def case_cible(grille):
    for case in grille:
        if grille[case][2]:
            return case
    raise ValueError


def amene_vide(destination, grille):
    """Parcours en largeur jusqu'à amener la case vide en `destination`."""
    a_visiter = deque([(0, grille)])
    visite = defaultdict(bool)
    while True:
        etapes, grille = a_visiter.pop()
        vide = case_vide(grille)
        if vide == destination:
            return etapes, grille
        if visite[vide]:
            continue
        visite[vide] = True
        for suivante in deplacements(grille):
            a_visiter.appendleft((etapes + 1, suivante))


def amene_cible(destination, grille):
    """Parcours en largeur jusqu'à ce que la donnée soit en `destination`."""
    a_visiter = deque([(0, grille)])
    visite = defaultdict(bool)
    while True:
        etapes, grille = a_visiter.pop()
        vide, cible = case_vide(grille), case_cible(grille)
        if cible == destination:
            return etapes, grille
        if visite[vide, cible]:
            continue
        visite[vide, cible] = True
        for suivante in deplacements(grille):
            a_visiter.appendleft((etapes + 1, suivante))


def partie2(noeuds):
    xmax = max(x for x, _ in noeuds)
    u, a, _ = noeuds[xmax, 0]
    grille = dict(noeuds)
    grille[xmax, 0] = (u, a, True)
    # la case vide arrive en (xmax, 0) : la donnée passe en (xmax - 1, 0)
    total, grille = amene_vide((xmax, 0), grille)
    for x in reversed(range(xmax - 1)):
        etapes, grille = amene_cible((x, 0), grille)
        total += etapes
    return total


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 2 :", partie2(donnees))
