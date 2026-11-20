"""Exercice 7 : ecarts croissants

Renvoie True si les écarts entre éléments consécutifs sont strictement croissants.
"""


def ecarts_croissants(L):
    n = len(L)
    for i in range(2, n):
        if L[i] - L[i - 1] <= L[i - 1] - L[i - 2]:
            return False
    return True


if __name__ == "__main__":
    assert ecarts_croissants([0, 1, 3, 6])
    assert not ecarts_croissants([0, 2, 4])
    assert ecarts_croissants([5, 1])
    print("Exercice 7 : tous les tests passent.")
