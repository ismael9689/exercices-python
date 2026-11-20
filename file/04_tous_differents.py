"""Exercice 4 : tous differents

Renvoie True si tous les éléments de L sont différents deux à deux.

Correction : la première version ne comparait que les voisins (L[i] et L[i-1]),
donc [1, 2, 1] était déclarée « tous différents ». La deuxième version comparait
bien toutes les paires, mais avec != au lieu de == : elle renvoyait False dès que
deux éléments étaient différents. Il faut comparer chaque paire (i, j) avec i < j
et renvoyer False dès qu'on trouve deux éléments ÉGAUX.
"""


def tous_differents(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            if L[i] == L[j]:
                return False
    return True


if __name__ == "__main__":
    assert tous_differents([1, 2, 3])
    assert not tous_differents([1, 2, 1])
    assert not tous_differents([4, 4])
    assert tous_differents([])
    print("Exercice 4 : tous les tests passent.")
