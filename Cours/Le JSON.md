### Définition de JSON

---

JSON est un format de données léger qui permet de stocker et d'échanger des données entre les applications. Il est facile à lire et à écrire pour les humains, et facile à analyser et à générer pour les machines.

<br>

### Exemple de JSON

---

Voici un exemple de données JSON :

```json
{
  "nom": "John",
  "prenom": "Doe",
  "age": 30
}
```

<br>

### Comment utiliser JSON

---

En Python, vous pouvez utiliser le module `json` pour travailler avec des données JSON.

```python
import json

# Conversion d'un dictionnaire Python en JSON
data = {"nom": "John", "prenom": "Doe", "age": 30}
json_data = json.dumps(data)

# Conversion de JSON en dictionnaire Python
json_str = '{"nom": "Alice", "prenom": "Smith", "age": 25}'
python_data = json.loads(json_str)
```

<br>

### Définition de Sérialisation

---

La sérialisation est le processus de conversion de données en un format JSON.

<br>

### Exemple de Sérialisation

---

```python
import json

data = {"nom": "John", "prenom": "Doe", "age": 30}
json_data = json.dumps(data)
print(json_data)
```

<br>

### Définition de Désérialisation

---

La désérialisation est le processus de conversion de données JSON en un format utilisable en Python.

<br>

### Exemple de Désérialisation

---

```python
import json

json_str = '{"nom": "Alice", "prenom": "Smith", "age": 25}'
python_data = json.loads(json_str)
print(python_data)
```

<br>

### La transformation de types entre Python et JSON

---

Lors de la sérialisation et de la désérialisation, les types de données Python sont convertis en équivalents JSON et vice versa. Par exemple, les dictionnaires Python deviennent des objets JSON, les listes Python deviennent des tableaux JSON, etc.
