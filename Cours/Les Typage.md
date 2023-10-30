### Annotation de Type en Python

---

Python est un langage typé dynamiquement, ce qui signifie que les types sont associés aux valeurs au moment de l'exécution, mais l'annotation de type permet d'introduire une forme de typage statique facultatif pour améliorer la qualité et la lisibilité du code.

Les type sont associés aux variables, aux paramètres de fonction et aux valeurs de retour.

Elle n'affecte pas l'exécution du code, mais elle peut être utilisée par des outils et des IDE pour détecter des erreurs potentielles et améliorer la documentation du code.

<br>

### Entiers (int)

---

```python
age: int = 25
```

<br>

### Flottants (float)

---

```python
prix: float = 10.99
```

<br>

### Chaînes de caractères (str)

---

```python
nom: str = "Alice"
```

<br>

### Booléens (bool)

---

```python
est_actif: bool = True
```

<br>

### Listes

---

```python
from typing import List

nombres: List[int] = [1, 2, 3]
```

<br>

### Tuples

---

```python
from typing import Tuple

coordonnees: Tuple[float, float] = (2.5, 3.0)
```

<br>

### Typage de Dictionnaires

---

```python
from typing import Dict

informations: Dict[str, str] = {"nom": "Bob", "ville": "Paris"}
```

<br>

### Typage de Paramètres et de Retours de Fonctions

---

```python
def ajouter(a: int, b: int) -> int:
    return a + b
```

<br>

### Fonctions avec des Paramètres Optionnels

---

```python
from typing import Optional

def afficher_message(age: int, nom: Optional[str] = None) -> None:
    if nom:
        print(f"{nom} a {age} ans.")
    else:
        print(f"Cet individu a {age} ans.")
```

<br>

### Typage d'Objets Personnalisés

---

Si vous avez défini une classe, vous pouvez indiquer le type de l'objet qui sera créé à partir de cette classe.

```python
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
```

Vous pouvez annoter le type de l'objet créé avec cette classe comme suit :

```python
def creer_personne(nom: str, age: int) -> Personne:
    return Personne(nom, age)
```

<br>

### Avantages de l'Annotation de Type

---

- Amélioration de la documentation du code en spécifiant clairement les types attendus.
- Détection plus rapide d'erreurs de typage lors de la vérification statique du code.
- Amélioration de la complétion automatique et de l'aide contextuelle dans les IDE.
- Facilité de maintenance du code grâce à une meilleure compréhension des types de données.
