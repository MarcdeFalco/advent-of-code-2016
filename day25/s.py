"""Advent of Code 2016, jour 25 : plus petit a donnant un signal 0, 1, 0, 1...

On essaie a = 1, 2, ... avec l'interprète des jours 12 et 23 ; l'exécution
s'arrête dès que deux sorties consécutives sont égales. Un signal qui alterne
indéfiniment ne peut pas être constaté par simulation (problème de l'arrêt) :
on l'accepte s'il a alterné pendant un nombre fixé d'instructions.
La limite est de 200 000 instructions : 20 000 ne suffisent pas à produire
la première sortie.
"""

NUMERO_REGISTRE = {"a": 0, "b": 1, "c": 2, "d": 3}
LIMITE_INSTRUCTIONS = 200000


def lire_entree(nom="input.txt"):
    with open(nom) as fichier:
        return fichier.read().strip().split("\n")


def signal_alterne(instructions, a):
    registres = [a, 0, 0, 0]

    def valeur(x):
        if x in NUMERO_REGISTRE:
            return registres[NUMERO_REGISTRE[x]]
        return int(x)

    sorties = []
    i = 0
    for _ in range(LIMITE_INSTRUCTIONS):
        if not 0 <= i < len(instructions):
            break
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
        elif mots[0] == "out":
            sorties.append(valeur(mots[1]))
            if len(sorties) >= 2 and sorties[-1] == sorties[-2]:
                return False
        i += pas
    return len(sorties) > 0


def partie1(instructions):
    a = 1
    while not signal_alterne(instructions, a):
        a += 1
    return a


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
