"""Exercice 3 : contient

Renvoie True si x est un élément de L.
"""


def contient(L, x):
    for e in L:
        if e == x:
            return True
    return False


if __name__ == "__main__":
    assert contient([1, 2, 3], 2)
    assert not contient([1, 2, 3], 4)
    assert not contient([], 1)
    print("Exercice 3 : tous les tests passent.")
