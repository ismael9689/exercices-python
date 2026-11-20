"""Exercice 12 : majorite superieur

Renvoie True si au moins la moitié des éléments de L sont supérieurs ou égaux au seuil s.
"""


def majoriteSuperieur(L, s):
    sup = 0
    inf = 0
    for x in L:
        if x >= s:
            sup += 1
        else:
            inf += 1
    return sup >= inf


if __name__ == "__main__":
    assert majoriteSuperieur([5, 6, 1], 5)
    assert majoriteSuperieur([5, 1], 5)
    assert not majoriteSuperieur([1, 2, 9], 5)
    print("Exercice 12 : tous les tests passent.")
