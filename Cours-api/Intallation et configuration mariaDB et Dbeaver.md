## installer de MariaDB

---

[installer MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.1.3&os=windows&cpu=x86_64&pkg=msi&m=icam)

Après avoir choisis votre mot_de_passe, exemple : `root` ou encore `password`
cochez `Use UTF8 as default derver's character set`

> [!TIP] mot de passe  
> vous allez devoir choisir un mot de passe pour votre administrateur `root`.
> même si ce n'est pas très sécurisé, ne mettez pas quelques chose de trop long et embétant.
> vous pourrez le changer à tout moment avec les requetes adéquats.

### macos

```
sudo mariadb-secure-installation
```

<br>

## Créer la base de donnée

---

> `votre_utilisateur` et `chemin_vers_votre_script` sont à remplacer avec votre configuration.

```bash
mysql -u votre_utilisateur -p < chemin_vers_votre_script/librairie.sql
```

> depuis le terminal mariaDB

```bash
source chemin\librairie.sql
```

> [!TIPS] chemin script sql
> Si vous vous deplacez avec votre terminal dans le dossier de votre script, alors il n'y aura pas de chemin à renseigner.
>
> Vous pourrez faire uniquement `mysql -u votre_utilisateur -p < librairie.sql`

> [!INFO] mysql et mariadb
> MariaDB est un fork de MySQL créé pour maintenir une alternative open source après l'acquisition de MySQL par Oracle. Les deux partagent une base commune mais diffèrent en termes de licence, communauté, et fonctionnalités.
> 
> C'est pour cela qu'ici on utilise une commande MySQL alors qu'on possède mariaDB

<br>

## DBeaver

---

### Installation

[Téléchager dbeaver](https://dbeaver.io/download/)

Lancer l'installation en tant qu'administrateur
- composant à installer (par défaut) : suivant

<br>

### Execution

lancer DBeaver en tant qu'administrateur

- ajouter connexion (le '+' en haut à gauche)  
- chosir MariaDB  
- Remplissez correctement les champs pour : `database`, `nom d'utilisateur` et `mot de passe`  
- Test de la connexion, puis OK
