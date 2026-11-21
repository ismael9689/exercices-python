"""Exercice 2 : est croissante

Renvoie True si la liste est croissante (au sens large).
"""


def est_croissante(L):
    n = len(L)
    for i in range(1, n):
        if L[i] < L[i - 1]:
            return False
    return True


if __name__ == "__main__":
    assert est_croissante([1, 2, 2, 5])
    assert not est_croissante([1, 3, 2])
    assert est_croissante([])
    print("Exercice 2 : tous les tests passent.")
