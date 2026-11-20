"""Exercice 5 : miroir

Renvoie True si L est un palindrome (se lit pareil dans les deux sens).

Correction : l'ancienne version renvoyait True dès qu'UNE paire L[i] == L[n-1-i]
était égale, et commençait à i = 1 (oubli du premier élément). Pour vérifier
« pour tout i », on renvoie False au premier contre-exemple, et True à la fin.
Il suffit de parcourir la première moitié : range(n // 2).
"""


def miroir(L):
    n = len(L)
    for i in range(n // 2):
        if L[i] != L[n - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    assert miroir([1, 2, 3, 2, 1])
    assert miroir([1, 2, 2, 1])
    assert not miroir([1, 2, 3])
    assert not miroir([5, 1, 1])
    assert miroir([])
    print("Exercice 5 : tous les tests passent.")
