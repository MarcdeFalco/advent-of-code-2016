"""Advent of Code 2016, jour 23 : assembleur auto-modifiant.

Interprète du jour 12 avec l'instruction `tgl`, qui modifie le programme.
Dans l'entrée, les instructions 4 à 9 forment une boucle de
multiplication et les instructions 12 à 15 une boucle de doublement : quand
le compteur ordinal y arrive, on applique directement leur effet (raccourci
propre à cette entrée). Une assertion vérifie que `tgl` ne modifie pas la
zone de la multiplication. Le registre a vaut 7 au départ, puis 12.
"""

NUMERO_REGISTRE = {"a": 0, "b": 1, "c": 2, "d": 3}


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def bascule(instruction):
    mots = instruction.split()
    if len(mots) == 2:
        mots[0] = "dec" if mots[0] == "inc" else "inc"
    else:
        mots[0] = "cpy" if mots[0] == "jnz" else "jnz"
    return " ".join(mots)


def execute(programme, a):
    instructions = list(programme)  # copie : `tgl` modifie le programme
    registres = [a, 0, 0, 0]

    def valeur(x):
        if x in NUMERO_REGISTRE:
            return registres[NUMERO_REGISTRE[x]]
        return int(x)

    i = 0
    while i < len(instructions):
        if i == 5:  # a <- c * d, puis c = d = 0
            registres[0] = registres[2] * registres[3]
            registres[2] = 0
            registres[3] = 0
            i = 10
            continue
        if i == 13:  # c <- 2 * c, puis d = 0
            registres[2] *= 2
            registres[3] = 0
            i = 16
            continue
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
        elif mots[0] == "tgl":
            cible = i + valeur(mots[1])
            assert cible not in range(3, 11)
            if 0 <= cible < len(instructions):
                instructions[cible] = bascule(instructions[cible])
        i += pas
    return registres[0]


def partie1(programme):
    return execute(programme, 7)


def partie2(programme):
    return execute(programme, 12)


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
