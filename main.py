#YOVO, KOSSI MARTINO, MASTER 2 DIT
import os
import sys

def create_empty_file_if_not_exists(file_path):
    """
    Cette fonction crée un fichier vide s'il n'existe pas
    """

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass

def create_directory_if_not_exists(path):
    """
    Cette fonction crée un répertoire s'il n'existe pas
    """

    if not os.path.exists(path):
        os.makedirs(path)

#Créer la fonction create_folder_tree().
def create_folder_tree(path):
    #Créer le répertoire s'il n'existe pas déjà.
    if not os.path.exists(path):
        os.makedirs(path) 
    
    # Créer les sous-répertoires suivants : data, docs, models, reports et src
    # s'il n'existe pas
    for folder in ["data", "docs", "models", "reports", "src"]:
        folder_path = os.path.join(path, folder)
        create_directory_if_not_exists(folder_path)
        
    # Créer les sous-répertoires suivants dans le répertoire data : cleaned, processed et raw
    # s'il n'existe pas
    for sub_folder in ["cleaned", "processed", "raw"]:
        sub_folder_path = os.path.join(path, "data", sub_folder)
        create_directory_if_not_exists(sub_folder_path)
        
    #Créer le sous-répertoire notebooks dans le répertoire models.
    create_directory_if_not_exists(
        os.path.join(path, "models", "notebooks")
    )
    
    # Créer les fichiers vides LICENSE, Makefile, README.md et requirements.txt_ à la racine
    create_empty_file_if_not_exists(os.path.join(path, "LICENSE"))
    create_empty_file_if_not_exists(os.path.join(path, "Makefile"))
    create_empty_file_if_not_exists(os.path.join(path, "README.md"))
    create_empty_file_if_not_exists(os.path.join(path, "requirements.txt_"))

    # Créer les fichiers vides utils.py, process.py et train.py dans le répertoire src
    create_empty_file_if_not_exists(os.path.join(path, "src", "utils.py"))
    create_empty_file_if_not_exists(os.path.join(path, "src", "process.py"))
    create_empty_file_if_not_exists(os.path.join(path, "src", "train.py"))


def main():
    # Récupérer le chemin du répertoire (argument de la commande)
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."

    #Appeller la fonction create_folder_tree() avec le chemin comme argument.
    #./Users/alwaysgoodapps/Documents/python-folder-tree-generator
    create_folder_tree(path)

if __name__ == "__main__":
    main()
