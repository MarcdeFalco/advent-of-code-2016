"""Advent of Code 2016, jour 9 : longueur d'un texte décompressé.

Partie 1 : la liste renversée des caractères sert de pile ; on dépile un
marqueur (n x r), on recopie r fois les n caractères suivants, et le texte
décompressé est réellement construit. Partie 2 (marqueurs imbriqués) : le
texte serait bien trop long, on calcule sa longueur par une récursion sur des
intervalles sans jamais décompresser.
"""


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip()


def partie1(texte):
    pile = list(reversed(texte))
    resultat = []
    while pile != []:
        c = pile.pop()
        if c == "(":
            marqueur = ""
            c = pile.pop()
            while c != ")":
                marqueur += c
                c = pile.pop()
            n, r = map(int, marqueur.split("x"))
            morceau = pile[-n:]  # les n caractères suivants, à l'envers
            morceau.reverse()
            resultat += morceau * r
            pile = pile[:-n]
        else:
            resultat.append(c)
    return len(resultat)


def partie2(texte):
    def longueur(i, j):
        """Longueur décompressée de texte[i:j]."""
        if i >= j or i >= len(texte):
            return 0
        if texte[i] != "(" or ")" not in texte[i:j]:
            return 1 + longueur(i + 1, j)
        k = i + 1
        while texte[k] != ")":
            k += 1
        n, r = map(int, texte[i + 1:k].split("x"))
        # le marqueur répète r fois les n caractères qui le suivent
        return r * longueur(k + 1, k + 1 + n) + longueur(k + 1 + n, j)

    return longueur(0, len(texte) + 1)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
