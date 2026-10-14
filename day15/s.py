"""Advent of Code 2016, jour 15 : instant où des disques tournants s'alignent.

Le disque k (numéroté à partir de 0), à n positions et en position p à
l'instant 0, est bien placé si t + k + 1 + p est divisible par n. On teste
t = 0, 1, 2, ... jusqu'à ce que toutes les congruences soient satisfaites.
La partie 2 ajoute un disque de 11 positions, en position 0.
"""
import re


def lire_entree(nom="input.txt"):
    """Liste des couples (nombre de positions, position initiale)."""
    disques = []
    with open(nom) as fichier:
        for ligne in fichier.read().strip().split("\n"):
            nombres = [int(x) for x in re.findall(r"\d+", ligne)]
            disques.append((nombres[1], nombres[3]))
    return disques


def premier_instant(disques):
    t = 0
    while True:
        if all((t + k + 1 + p) % n == 0 for k, (n, p) in enumerate(disques)):
            return t
        t += 1


def partie1(disques):
    return premier_instant(disques)


def partie2(disques):
    return premier_instant(disques + [(11, 0)])


if __name__ == "__main__":
    donnees = lire_entree()
    print("Partie 1 :", partie1(donnees))
    print("Partie 2 :", partie2(donnees))
