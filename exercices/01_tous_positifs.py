"""Exercice 1 : tous positifs

Renvoie True si tous les éléments de L sont strictement positifs.
"""


def tous_positifs(L):
    for x in L:
        if x <= 0:
            return False
    return True


if __name__ == "__main__":
    assert tous_positifs([1, 2, 3])
    assert not tous_positifs([1, 0, 3])
    assert not tous_positifs([-1])
    assert tous_positifs([])
    print("Exercice 1 : tous les tests passent.")
