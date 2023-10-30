### Introduction

---

CSV signifie "Comma Separated Values" (Valeurs Séparées par des Virgules). Il s'agit d'un format de fichier couramment utilisé pour stocker des données tabulaires, telles que des feuilles de calcul. Python offre de nombreuses bibliothèques pour travailler avec des fichiers CSV de manière efficace.

<br>

### Comment ouvrir un fichier CSV

---

Pour lire un fichier CSV en Python, vous pouvez utiliser la bibliothèque `csv`. Tout d'abord, vous devez ouvrir le fichier en mode de lecture.

```python
import csv

with open('donnees.csv', mode='r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
```

<br>

### Comment lire les données d'un fichier CSV

---

Après avoir ouvert le fichier CSV, vous pouvez lire les données en utilisant la boucle `for`.

```python
import csv

with open('donnees.csv', mode='r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)

    for ligne in lecteur_csv:
        print(ligne)
```

<br>

### Comment accéder à des colonnes spécifiques

---

Pour accéder à des colonnes spécifiques dans un fichier CSV, vous pouvez simplement utiliser l'index de colonne.

```python
import csv

with open('donnees.csv', mode='r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)

    for ligne in lecteur_csv:
        nom = ligne[0]
        age = ligne[1]
        print(f"Nom : {nom}, Age : {age}")
```

<br>

### Comment créer un fichier CSV

---

Pour créer un nouveau fichier CSV en Python, vous pouvez utiliser la bibliothèque `csv` en mode d'écriture.

```python
import csv

with open('nouveau_fichier.csv', mode='w', newline='') as fichier_csv:
    redacteur_csv = csv.writer(fichier_csv)
```

<br>

### Comment écrire des données dans un fichier CSV

---

Après avoir ouvert le fichier CSV en mode d'écriture, vous pouvez écrire des données dans le fichier.

```python
import csv

with open('nouveau_fichier.csv', mode='w', newline='') as fichier_csv:
    redacteur_csv = csv.writer(fichier_csv)

    redacteur_csv.writerow(['Nom', 'Age'])
    redacteur_csv.writerow(['Alice', 25])
    redacteur_csv.writerow(['Bob', 30])
```

<br>

### Bibliothèques CSV populaires

---

Outre la bibliothèque `csv` de base, Python offre des bibliothèques populaires pour travailler avec des fichiers CSV, telles que `pandas` et `openpyxl`. Ces bibliothèques offrent des fonctionnalités avancées pour la manipulation de données tabulaires.

- **Pandas (Optionnel)** : Pandas est une bibliothèque de manipulation de données très puissante. Elle permet de lire et d'écrire des fichiers CSV, ainsi que de réaliser des opérations avancées sur les données.

- **Openpyxl (Optionnel)** : Openpyxl est une bibliothèque pour lire et écrire des fichiers Excel, mais elle peut également être utilisée pour lire et écrire des fichiers CSV.

L'utilisation de ces bibliothèques est optionnelle et dépend des besoins spécifiques de votre projet.
