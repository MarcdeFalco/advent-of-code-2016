"""Advent of Code 2016, jour 21 : brouillage d'un mot de passe.

Partie 1 : on simule les opérations sur une liste de caractères. Partie 2 :
on lit les opérations à l'envers et on applique leur inverse. Échanges et
retournements sont leurs propres inverses ; déplacements et rotations
s'inversent en échangeant les arguments ou le sens. La rotation qui dépend de
la position d'une lettre n'a pas d'inverse simple : on tourne vers la gauche
un cran à la fois jusqu'à un état d'où la rotation directe ramènerait ici.
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def tourne_droite(s):
    return [s[-1]] + s[:-1]


def tourne_gauche(s):
    return s[1:] + [s[0]]


def echange(s, mots):
    if mots[1] == "position":
        i, j = int(mots[2]), int(mots[-1])
        s[i], s[j] = s[j], s[i]
    else:
        a, b = mots[2], mots[-1]
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
            elif s[i] == b:
                s[i] = a
    return s


def retourne(s, mots):
    i, j = int(mots[2]), int(mots[-1])
    return s[:i] + list(reversed(s[i:j + 1])) + s[j + 1:]


def deplace(s, i, j):
    lettre = s[i]
    del s[i]
    return s[:j] + [lettre] + s[j:]


def brouille(mot, operations):
    s = list(mot)
    for operation in operations:
        mots = operation.split()
        if mots[0] == "swap":
            s = echange(s, mots)
        elif mots[0] == "reverse":
            s = retourne(s, mots)
        elif mots[0] == "move":
            s = deplace(s, int(mots[2]), int(mots[-1]))
        elif mots[1] == "based":
            i = s.index(mots[-1])
            for _ in range(i + 1 + (1 if i >= 4 else 0)):
                s = tourne_droite(s)
        elif mots[1] == "left":
            for _ in range(int(mots[2])):
                s = tourne_gauche(s)
        else:
            for _ in range(int(mots[2])):
                s = tourne_droite(s)
    return "".join(s)


def debrouille(mot, operations):
    s = list(mot)
    for operation in reversed(operations):
        mots = operation.split()
        if mots[0] == "swap":
            s = echange(s, mots)
        elif mots[0] == "reverse":
            s = retourne(s, mots)
        elif mots[0] == "move":
            s = deplace(s, int(mots[-1]), int(mots[2]))
        elif mots[1] == "based":
            # après qte crans à gauche, la rotation directe ferait qte crans
            # à droite : on s'arrête au premier qte cohérent
            for qte in range(len(s) + 2):
                i = s.index(mots[-1])
                if qte == i + 1 + (1 if i >= 4 else 0):
                    break
                s = tourne_gauche(s)
        elif mots[1] == "right":
            for _ in range(int(mots[2])):
                s = tourne_gauche(s)
        else:
            for _ in range(int(mots[2])):
                s = tourne_droite(s)
    return "".join(s)


def partie1(operations):
    return brouille("abcdefgh", operations)


def partie2(operations):
    return debrouille("fbgdceah", operations)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
