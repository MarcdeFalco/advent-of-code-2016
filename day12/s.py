"""Advent of Code 2016, jour 12 : machine à quatre registres.

Interprète direct : chaque instruction est redécoupée à chaque exécution et
un saut relatif modifie le pas. La partie 2 met le registre c à 1 au départ ;
le programme calcule alors un terme plus lointain d'une suite de Fibonacci,
par incréments successifs (quelques dizaines de millions d'instructions).
"""

NUMERO_REGISTRE = {"a": 0, "b": 1, "c": 2, "d": 3}


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def execute(instructions, c):
    registres = [0, 0, c, 0]

    def valeur(x):
        if x in NUMERO_REGISTRE:
            return registres[NUMERO_REGISTRE[x]]
        return int(x)

    i = 0
    while i < len(instructions):
        mots = instructions[i].split()
        pas = 1
        if mots[0] == "cpy":
            registres[NUMERO_REGISTRE[mots[2]]] = valeur(mots[1])
        elif mots[0] == "inc":
            registres[NUMERO_REGISTRE[mots[1]]] += 1
        elif mots[0] == "dec":
            registres[NUMERO_REGISTRE[mots[1]]] -= 1
        elif mots[0] == "jnz" and valeur(mots[1]) != 0:
            pas = valeur(mots[2])
        i += pas
    return registres[0]


def partie1(instructions):
    return execute(instructions, 0)


def partie2(instructions):
    return execute(instructions, 1)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
