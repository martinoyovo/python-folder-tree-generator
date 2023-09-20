**Folder Tre Generator with Python**

Ce programme Python crée une arborescence de répertoires à partir d'un chemin. L'arborescence est composée des répertoires :

* `data`
* `docs`
* `models`
* `reports`
* `src`

**Conception**

Le programme utilise la fonction `os.makedirs()` pour créer tous les répertoires et sous-répertoires nécessaires pour créer l'arborescence.

**Utilisation**

Pour exécuter le programme, vous pouvez utiliser un éditeur de texte pour ouvrir le fichier Python et le sauvegarder. Ensuite, vous pouvez exécuter le programme en utilisant la ligne de commande ou un IDE Python.

**Ligne de commande**

Pour exécuter le programme à partir de la ligne de commande, vous devez vous placer dans le répertoire contenant le fichier Python. Ensuite, vous pouvez exécuter le programme en utilisant la commande suivante :

> chemin_vers_le_dossier est le dossier courant par défaut

```
python create_folder_tree.py {chemin_vers_le_dossier}
```

**IDE Python**

Pour exécuter le programme à partir d'un IDE Python, vous pouvez ouvrir le fichier Python dans l'IDE et cliquer sur le bouton de lecture.

**Exemple**

Supposons que vous avez créé un fichier Python nommé `create_folder_tree.py` dans le répertoire `/Users/alwaysgoodapps/project`. Pour exécuter le programme, vous pouvez utiliser la ligne de commande suivante :

```
cd /Users/alwaysgoodapps/project
python create_folder_tree.py
```

Ce code créera l'arborescence suivante dans le répertoire `/Users/alwaysgoodapps/project` :

```
data
  cleaned
  processed
  raw
docs
LICENSE
Makefile
models
notebooks
      main.ipynb
README.md
reports
requirements.txt_
src
    utils.y
    process.py
    train.py
```