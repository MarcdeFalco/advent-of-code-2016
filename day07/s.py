"""Advent of Code 2016, jour 7 : motifs dans et hors des crochets.

`segments` découpe récursivement une adresse en morceaux marqués selon qu'ils
sont hors crochets ou entre crochets ; on balaie ensuite chaque morceau par
fenêtres de 4 (motif abba, partie 1) ou de 3 caractères (motifs aba, partie 2).
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def motifs_aba(s):
    """Liste des couples « ab » tels que s contient a, b, a (a != b)."""
    motifs = []
    for i in range(len(s) - 2):
        a, b, c = s[i:i + 3]
        if a == c and b != a:
            motifs.append(a + b)
    return motifs


def contient_abba(s):
    for i in range(len(s) - 3):
        a, b, c, d = s[i:i + 4]
        if a == d and b == c and a != b:
            return True
    return False


def segments(s):
    """Liste des (morceau, True si hors crochets)."""
    if s == "":
        return []
    if s[0] == "[":
        i = s.find("]")
        return [(s[1:i], False)] + segments(s[i + 1:])
    i = 0
    while i < len(s) and s[i] != "[":
        i += 1
    return [(s[:i], True)] + segments(s[i:])


def partie1(adresses):
    total = 0
    for adresse in adresses:
        abba_dehors = False
        abba_dedans = False
        for morceau, dehors in segments(adresse):
            if contient_abba(morceau):
                if dehors:
                    abba_dehors = True
                else:
                    abba_dedans = True
        if abba_dehors and not abba_dedans:
            total += 1
    return total


def partie2(adresses):
    total = 0
    for adresse in adresses:
        aba = []  # motifs hors crochets
        bab = []  # motifs entre crochets
        for morceau, dehors in segments(adresse):
            if dehors:
                aba += motifs_aba(morceau)
            else:
                bab += motifs_aba(morceau)
        if any(m[1] + m[0] in bab for m in aba):
            total += 1
    return total


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
