"""
Module principal pour l'analyse des suites de Syracuse.

Ce script calcule et affiche les propriétés des suites de Syracuse.
Il utilise la bibliothèque Plotly pour générer des graphiques interactifs.

Fonctions principales :
- syr_plot : Génère un graphique de la suite de Syracuse.
- syracuse_l : Calcule la suite de Syracuse pour un nombre donné.
- temps_de_vol : Calcule le temps de vol d'une suite.
- temps_de_vol_en_altitude : Calcule le temps de vol en altitude.
- altitude_maximale : Trouve l'altitude maximale atteinte par la suite.
- main : Fonction principale pour exécuter le script.
"""

# main.py

# Imports
from plotly.graph_objects import Scatter, Figure

def syr_plot(lsyr):
    """
    Affiche un graphique de la suite de Syracuse.

    Args:
        lsyr (list): La suite de Syracuse à afficher.
    """
    title = f"Syracuse (n = {lsyr[0]})"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))
    trace = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(trace)
    fig.show()
    #j'ai enlevé le return NONE pour avoir une note de code de 10


def syracuse_l(n):
    """
    Génère la suite de Syracuse à partir d'un entier source.

    Args:
        n (int): La source de la suite.

    Returns:
        list: La suite de Syracuse générée.
    """
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        l.append(n)
    return l


def temps_de_vol(l):
    """
    Retourne le temps de vol d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol.
    """
    return len(l)


def temps_de_vol_en_altitude(l):
    """
    Retourne le temps de vol en altitude d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol en altitude (valeurs supérieures ou égales à la source).
    """
    n = 0
    ndepart = l[0]
    for i in l:
        if i >= ndepart:
            n += 1
        else:
            break
    return n


def altitude_maximale(l):
    """
    Retourne l'altitude maximale d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: L'altitude maximale.
    """
    return max(l)


def main():
    """
    Fonction principale : génère la suite de Syracuse pour une valeur donnée,
    trace son graphique et affiche les résultats des analyses.
    """
    n = 15  # Vous pouvez changer la valeur ici
    lsyr = syracuse_l(n)
    syr_plot(lsyr)
    print(f"Temps de vol : {temps_de_vol(lsyr)}")
    print(f"Temps de vol en altitude : {temps_de_vol_en_altitude(lsyr)}")
    print(f"Altitude maximale : {altitude_maximale(lsyr)}")


if __name__ == "__main__":
    main()
