#YOVO, KOSSI MARTINO, MASTER 2 DIT
import os
import sys

def create_empty_file(file_path):
    """
    Cette fonction crée un fichier vide 
    dont le chemin est file_path
    """

    with open(file_path, "w") as f:
        pass


#Créer la fonction create_folder_tree().
def create_folder_tree(path):
    
    #Vérifier si le répertoire existe déjà. Si c'est le cas, la fonction create_folder_tree() renvoie sans rien faire.
    if not os.path.exists(path):
        os.makedirs(path) 

    
    # #Créer le répertoire s'il n'existe pas déjà.
    # os.makedirs(path) 
    
    #Créer les sous-répertoires suivants : data, docs, models, reports et src.
    for folder in ["data", "docs", "models", "reports", "src"]:
        os.makedirs(os.path.join(path, folder))
        
    #Créer les sous-répertoires suivants dans le répertoire data : cleaned, processed et raw.    
    for sub_folder in ["cleaned", "processed", "raw"]:
        os.makedirs(os.path.join(path, "data", sub_folder))
        
    #Créer le sous-répertoire notebooks dans le répertoire models.
    os.makedirs(os.path.join(path, "models", "notebooks"))
    
    #Créer les fichiers vides LICENSE, Makefile, README.md et requirements.txt_ à la racine
    create_empty_file(os.path.join(path, "LICENSE"))
    create_empty_file(os.path.join(path, "Makefile"))
    create_empty_file(os.path.join(path, "README.md"))
    create_empty_file(os.path.join(path, "requirements.txt_"))

    #Créer les fichiers vides utils.py, process.py et train.py dans le répertoire src
    create_empty_file(os.path.join(path, "src", "utils.py"))
    create_empty_file(os.path.join(path, "src", "process.py"))
    create_empty_file(os.path.join(path, "src", "train.py"))


def main():
    # Récupérer le chemin (argument de la commande)
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."

    #Appeller la fonction create_folder_tree() avec le chemin comme argument.
    #./Users/alwaysgoodapps/Documents/python-folder-tree-generator
    create_folder_tree(path)

if __name__ == "__main__":
    main()
