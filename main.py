import os


#Créer la fonction create_folder_tree().
def create_folder_tree(path):
    
    #Vérifier si le répertoire existe déjà. Si c'est le cas, la fonction create_folder_tree() renvoie sans rien faire.
    if os.path.exists(path):
        return
    
    #Créer le répertoire s'il n'existe pas déjà.
    os.makedirs(path) 

