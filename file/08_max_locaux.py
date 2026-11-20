"""Exercice 8 : max locaux

Renvoie le nombre de maximums locaux de L : les éléments strictement plus
grands que leurs deux voisins (le premier et le dernier élément ne comptent pas).

Correction : l'ancienne version
- parcourait range(n), donc L[i-1] valait L[-1] pour i = 0 (dernier élément !)
  et L[i+1] provoquait une IndexError pour i = n-1 ;
- testait un minimum local (L[i] < L[i-1] et L[i+1] > L[i]) au lieu d'un maximum ;
- renvoyait True/False au lieu de compter.
On parcourt donc range(1, n-1) et on compte.
"""


def max_locaux(L):
    n = len(L)
    compteur = 0
    for i in range(1, n - 1):
        if L[i] > L[i - 1] and L[i] > L[i + 1]:
            compteur += 1
    return compteur


if __name__ == "__main__":
    assert max_locaux([1, 3, 2, 5, 4]) == 2
    assert max_locaux([1, 2, 3]) == 0
    assert max_locaux([]) == 0
    print("Exercice 8 : tous les tests passent.")
