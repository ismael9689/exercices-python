"""Exercice 6 : premiere moitie inf

Renvoie True si chaque élément de la première moitié est strictement inférieur à son symétrique : L[i] < L[n-1-i].
"""


def premiere_moitie_inf(L):
    n = len(L)
    for i in range(n // 2):
        if L[i] >= L[n - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    assert premiere_moitie_inf([1, 2, 5, 6])
    assert not premiere_moitie_inf([1, 7, 5, 6])
    assert premiere_moitie_inf([3])
    print("Exercice 6 : tous les tests passent.")
