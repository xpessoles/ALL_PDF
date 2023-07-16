# -*- coding: utf-8 -*-
"""
@author: xpessoles@lamartin.fr
"""

import os


# On fait la liste des .tex d'un dossier.
# On crée pour chaque .tex un dictionnaire :
# {fichier:str, time : os.path.getmtime
chemins = [#"PSI_Cy_08_SystemesSequentiels",
        "../../PSI_Cy_01_ModelisationSystemes",
        "../../PSI_Cy_02_PredictionPerfomances",
        "../../PSI_Cy_03_ConceptionCommande",
        "../../PSI_Cy_04_ModelisationDynamique",
        "../../PSI_Cy_05_Energetique",
        "../../PSI_Cy_06_ChaineSolides",
        #"PSI_Cy_07_ResolutionNumerique"
        ]
def make_tex_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier tex.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif}
    """
    tex_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".tex"):
                    if verif(root,file) :
                        fich = os.path.join(root, file)
                        modif = os.path.getmtime(fich)
                        dico = {'fichier':fich,'last_modif':modif}
                        tex_liste.append(dico)

    return tex_liste

def verif(root,file):
    test = ["old","QCM","Headings","QCM","OLD"]
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True

def compile_file(file):

