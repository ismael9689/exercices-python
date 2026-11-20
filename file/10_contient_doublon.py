"""Exercice 10 : contient doublon

Renvoie True si au moins deux éléments de L sont égaux.
"""


def contient_doublon(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            if L[i] == L[j]:
                return True
    return False


if __name__ == "__main__":
    assert contient_doublon([1, 2, 1])
    assert not contient_doublon([1, 2, 3])
    assert not contient_doublon([])
    print("Exercice 10 : tous les tests passent.")
