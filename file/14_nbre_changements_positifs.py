"""Exercice 14 : nbre changements positifs

Renvoie le nombre de fois où un élément est strictement plus grand que le précédent.
"""


def nbreChangementsPositifs(L):
    n = len(L)
    compteur = 0
    for i in range(1, n):
        if L[i] > L[i - 1]:
            compteur += 1
    return compteur


if __name__ == "__main__":
    assert nbreChangementsPositifs([1, 3, 2, 5]) == 2
    assert nbreChangementsPositifs([3, 2, 1]) == 0
    assert nbreChangementsPositifs([]) == 0
    print("Exercice 14 : tous les tests passent.")
