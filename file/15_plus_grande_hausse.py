"""Exercice 15 : plus grande hausse

Renvoie la plus grande hausse entre deux éléments consécutifs (0 s'il n'y a aucune hausse).
"""


def plusGrandeHausse(L):
    diff = 0
    for i in range(1, len(L)):
        hausse = L[i] - L[i - 1]
        if hausse > diff:
            diff = hausse
    return diff


if __name__ == "__main__":
    assert plusGrandeHausse([1, 4, 2, 10]) == 8
    assert plusGrandeHausse([5, 3, 1]) == 0
    assert plusGrandeHausse([]) == 0
    print("Exercice 15 : tous les tests passent.")
