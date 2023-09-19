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

