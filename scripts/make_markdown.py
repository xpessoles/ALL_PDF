# -*- coding: utf-8 -*-
"""
@author: xpessoles@lamartin.fr
"""

import os
import shutil
import pickle

## TODO :
 # Sauvegarder l'historique de compilation a chaque fin de compil
 # Modifier les noms des PDF pour pouvoir les parser
 # Préciser le PC surlquel ont été compilés les fichiers ?
##

PC = "perso"
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
        #"../../PSI_Cy_07_ResolutionNumerique",
        "../../PSI_Cy_11_Statique_Revisions",
        "../../PSI_Cy_12_Cinematique_Revisions",
        ]
def make_tex_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier tex.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif:....}
    """
    tex_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".tex"):
                    if verif(root,file) :
                        dico = make_dico_from_tex_file(root, file)
                        tex_liste.append(dico)


    return tex_liste

def make_dico_from_tex_file(root, file):
    """
    Réalise un dictionnaire à partir d'un fichier tex

    Clés du dico :
     - full_chemin : chemin relatif + nom de fichier.tex par rapport au dossier de ce script
     - last_modif : dernière modification
     - chmein : chemin relatif du dossier
     - fichier : fichier.tex
     % "{'classe':('PSI'),'chapitre':'cin_','type':('td'),'titre':'', 'source':'','comp':(''),'corrige':True}"
    """
    fich = os.path.join(root, file)
    fich = fich.replace("\\","/")
    root = root.replace("\\","/")
    modif = os.path.getmtime(fich)

    dico = {'full_chemin':fich,'last_modif':modif,"chemin":root,"fichier":file}

    fid = open(fich,'r', encoding="utf8")
    line = fid.readline()
    fid.close()
    # On vérifie si le fichier a les tags sur la première ligne.

    if not 'type' in line :
        print(file)
        print(line)


    if 'type' in line :
        # Creation du dico a partir de la premiere ligne du fichier
        line = line.rstrip()[1:]
        d = eval(line)
        #print(file)
        d = eval(d)
        for k,v in d.items():
            dico[k]=v

    return dico

def verif(root,file):
    """
    Exclusion de fichiers
    """
    test = ["old","QCM","Headings",
    "QCM","OLD","xx","TODO","macros",
    "Cours",
    "cours","Old",
    "Cy_01_Ch_01_Application",
    "Cy_01_Ch_02_05_App_01",
    "Schema_1_entree_2F_R",
    "Schema2Entrees_2F_R",
    "Schema_1_entree_F_R",
    "new_pagegarde",
    "macros_SII",
    "new_style",
    "SchemaBlocs",
    "DS_01__Sujet",
    "DS_01_Sujet",
    "DS_01_",
    "Fiche",
    "Cy_02_01_Application_01",
    "Cy_02_Ch_01_Application_01",
    "TD_03_/",
    "Cy_02_01_TD_02_Calage",
    "Cy_02_03_Activation",
    "Cy_02_Ch_03_TD_02_SegwayVuibert",
    "Cy_02_Ch_03_TD_01_FauteuilDynamique",
    "Cy_03_01_Colle_05",
    "Colle_06_PompeTurboMolecullaire",
    "qr",
    ]
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True


def save_liste_tex(data,machine) :
    # Sauver la liste des fichiers tex
    nom_fichier = 'tex_liste'+machine+'.save'
    file = open(nom_fichier, 'wb')
    pickle.dump(data, file)
    file.close()

def load_liste_tex(machine) :
    # Charger la liste des fichiers tex
    nom_fichier = 'tex_liste'+machine+'.save'
    file = open(nom_fichier, 'rb')
    data = pickle.load(file)
    return data




def diff_tex_file(machine):
    # affichage des fichiers modifiés
    old_tex_file = load_liste_tex(machine)
    new_tex_file = make_tex_list(chemins)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder
        if d_new not in old_tex_file :
            print(d_new)


def make_nav(dico):
    # On crée la nav du site
    chap = []
    for d in dico :
        c = d['chapitre']
        if c not in chap :
            chap.append(c)

        # Vérif que les fichiers ont un chapitre
        if d['chapitre'] == '':
            print(d['fichier'])
            print(d['chapitre'])
    return chap


# Strucutre du site :
a = make_tex_list(chemins)
chap = make_nav(a)
for c in chap :
    if "" in c :
        print(c)
for d in a :
    if "pdf" in d['chapitre']:
        print(print(d['fichier']))