#YOVO, KOSSI MARTINO, MASTER 2 DIT
import os


#Créer la fonction create_folder_tree().
def create_folder_tree(path):
    
    #Vérifier si le répertoire existe déjà. Si c'est le cas, la fonction create_folder_tree() renvoie sans rien faire.
    if os.path.exists(path):
        return
    
    #Créer le répertoire s'il n'existe pas déjà.
    os.makedirs(path) 
    
    #Créer les sous-répertoires suivants : data, docs, models, reports et src.
    for folder in ["data", "docs", "models", "reports", "src"]:
        os.makedirs(os.path.join(path, folder))
        
    #Créer les sous-répertoires suivants dans le répertoire data : cleaned, processed et raw.    
    for sub_folder in ["cleaned", "processed", "raw"]:
        os.makedirs(os.path.join(path, "data", sub_folder))
        
    #Créer le sous-répertoire notebooks dans le répertoire models.
    os.makedirs(os.path.join(path, "models", "notebooks"))
    
    #Ouvrir le fichier LICENSE, Makefile, README.md, requirements.txt_, en écriture et y écrit une ligne vide.
    with open(os.path.join(path, "LICENSE"), "w") as f:
        f.write("")
    with open(os.path.join(path, "Makefile"), "w") as f:
        f.write("")
    with open(os.path.join(path, "README.md"), "w") as f:
        f.write("")
    with open(os.path.join(path, "requirements.txt_"), "w") as f:
        f.write("")
        
    #Ouvrir le fichier utils.py, process.py, train.py en écriture et y écrit une ligne vide.
    with open(os.path.join(path, "src", "utils.py"), "w") as f:
        f.write("")
    with open(os.path.join(path, "src", "process.py"), "w") as f:
        f.write("")
    with open(os.path.join(path, "src", "train.py"), "w") as f:
        f.write("")
        
#Appeller la fonction create_folder_tree() avec le chemin actuel comme argument.
#./Users/alwaysgoodapps/Documents/python-folder-tree-generator
current_path = input("Entrer le chemin vers lequel vous voulez créer l'arborescence: ")
create_folder_tree(current_path)

