### Documentation en Python

---

La documentation est un moyen de communication clé de la programmation, car elle rend votre code plus lisible, facilite la collaboration et permet aux autres développeurs de comprendre et d'utiliser votre code.

La documentation en Python est essentielle pour expliquer le but, le fonctionnement et l'utilisation des modules, des fonctions, des classes et des variables.

Il existe plusieurs types de documentation couramment utilisés pour rendre le code plus compréhensible et accessible.

Elle est également utile pour générer automatiquement des documentations conviviales pour les utilisateurs de vos bibliothèques et modules.

<br>

### Commentaires

---

Les commentaires sont le moyen le plus simple de documenter votre code. Ils sont destinés aux développeurs qui lisent le code source et ne sont pas inclus dans la documentation générée automatiquement.

```python
# Ceci est un commentaire simple
```

<br>

### Docstrings

---

Les docstrings sont des chaînes de caractères incluses dans le code source qui décrivent une fonction, une classe, un module ou une variable. Ils sont utilisés pour générer une documentation automatique.

```python
def addition(a, b):
    """
    Cette fonction renvoie la somme de deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme des deux nombres.
    """
    return a + b
```

<br>

### Documentation de Module

---

La documentation de module est généralement placée au début d'un fichier de code et décrit le contenu, le but et l'utilisation du module.

```python
"""
Ce module contient des fonctions pour effectuer des opérations mathématiques de base.
"""

def addition(a, b):
    return a + b
```

<br>

### Documentation de Classe

---

La documentation de classe est utilisée pour décrire les classes et leurs méthodes.

```python
class Personne:
    """
    Cette classe représente une personne avec un nom et un âge.
    """

    def __init__(self, nom, age):
        """
        Initialise une nouvelle instance de la classe Personne.

        Args:
            nom (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        self.nom = nom
        self.age = age
```

<br>

### Documentation de Fonction

---

La documentation de fonction est utilisée pour décrire les fonctions et leurs paramètres. Elle est généralement placée sous la signature de la fonction.

```python
def division(dividende, diviseur):
    """
    Cette fonction renvoie le résultat de la division.

    Args:
        dividende (float): Le nombre à diviser.
        diviseur (float): Le nombre par lequel diviser.

    Returns:
        float: Le résultat de la division.

    Raises:
        ZeroDivisionError: Si le diviseur est égal à zéro.
    """
    if diviseur == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro.")
    return dividende / diviseur
```

<br>

### Documentation de Variable

---

La documentation de variable est utilisée pour expliquer le but d'une variable, en particulier lorsqu'elle n'est pas évidente.

```python
nombre_de_clients: int = 100  # Le nombre total de clients dans la base de données
```

<br>

### Annotations de Type

---

Bien que ce ne soit pas une forme de documentation explicite, l'annotation de type est également un moyen de documenter le code en indiquant le type attendu des paramètres et des valeurs de retour des fonctions.

```python
def addition(a: int, b: int) -> int:
    return a + b
```
