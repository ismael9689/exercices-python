"""Exercice 11 : elements communs

Renvoie True si L1 et L2 ont au moins un élément en commun.

Correction : l'ancienne version renvoyait False quand elle trouvait un élément
commun et True sinon, soit l'inverse de ce que dit le nom de la fonction.
"""


def elements_communs(L1, L2):
    for a in L1:
        for b in L2:
            if a == b:
                return True
    return False


if __name__ == "__main__":
    assert elements_communs([1, 2, 3], [5, 3])
    assert not elements_communs([1, 2], [3, 4])
    assert not elements_communs([], [1])
    print("Exercice 11 : tous les tests passent.")
