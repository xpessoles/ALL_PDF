# -*- coding: utf-8 -*-
"""
@author: xpessoles@lamartin.fr
"""

import os
import shutil
import pickle


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
        "../../PSI_Cy_11_Statique_Revisions",
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
                        fich = fich.replace("\\","/")
                        root = root.replace("\\","/")
                        modif = os.path.getmtime(fich)
                        dico = {'full_chemin':fich,'last_modif':modif,"chemin":root,"fichier":file}
                        tex_liste.append(dico)


    return tex_liste

def verif(root,file):
    test = ["old","QCM","Headings","QCM","OLD",
    "Cours","cours","Old",
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
    "qr"
    ]
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True

def compile_file(dict):

    # Compilation du sujet
    # On copie la base
    dest = dict["fichier"] # fichier.tex
    dest = dest[:-4]+"_Sujet.tex"
    shutil.copy("base.tex",dest)
    print("==================================")
    print(dest)


    # On complete la base
    fid = open(dest,"a")
    fid.write("\\renewcommand{\\repExo}{"+dict["chemin"]+"} \n")
    fid.write("\\graphicspath{{\\repStyle/png}{\\repExo/images}}")
    fid.write("\\input{"+dict["full_chemin"]+"}\n \n")
    fid.write("\\end{document}")
    fid.close()

    # On compile
    os.system("pdflatex --shell-escape "+dest)
    os.system("pdflatex --shell-escape "+dest)

    src = dest[:-4]+".pdf"
    dest = "../PDF/"+src
    # On stocke
    shutil.copy(src,dest)
    # On efface tout les fichiers de compil
    src = src[:-4]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.startswith(src):

                try :
                    os.remove(file)
                except :
                    print(file)


    #################################
    # Compilation du corrigé
    # On copie la base
    dest = dict["fichier"] # fichier.tex
    dest = dest[:-4]+"_Corrige.tex"
    shutil.copy("base.tex",dest)
    print("==================================")
    print(dest)


    # On complete la base
    fid = open(dest,"a")
    fid.write("\\proftrue \n")
    fid.write("\\renewcommand{\\repExo}{"+dict["chemin"]+"} \n")
    fid.write("\\graphicspath{{\\repStyle/png}{\\repExo/images}}")
    fid.write("\\input{"+dict["full_chemin"]+"}\n \n")
    fid.write("\\end{document}")
    fid.close()

    # On compile
    os.system("pdflatex --shell-escape "+dest)
    os.system("pdflatex --shell-escape "+dest)

    src = dest[:-4]+".pdf"
    dest = "../PDF/"+src
    # On stocke
    shutil.copy(src,dest)
    # On efface tout les fichiers de compil
    src = src[:-4]
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.startswith(src):

                try :
                    os.remove(file)
                except :
                    print(file)



    return False


def save_liste_tex(data) :
    # Sauver la liste des fichiers tex
    file = open('tex_liste.save', 'wb')
    pickle.dump(data, file)
    file.close()

def load_liste_tex() :
    # Charger la liste des fichiers tex
    file = open('tex_liste.save', 'rb')
    data = pickle.load(file)
    return data


def go():
    # compilation des fichiers modifiés
    old_tex_file = load_liste_tex()
    new_tex_file = make_tex_list(chemins)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder
        if d_new not in old_tex_file :
            i=i+1

            compile_file(d_new)
    save_liste_tex(new_tex_file)

def diff_tex_file():
    # affichage des fichiers modifiés
    old_tex_file = load_liste_tex()
    new_tex_file = make_tex_list(chemins)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder
        if d_new not in old_tex_file :
            print(d_new)





def make_all_pdf():
    tex_liste = make_tex_list(chemins)
    liste_pdf = os.listdir("../PDF")

    for d in tex_liste :
        f_pdf_1 = d['fichier'][:-4]+'_Sujet.pdf'
        f_pdf_2 = d['fichier'][:-4]+'_Corrige.pdf'
        #print(f_pdf)
        #return f_pdf,liste_pdf
        if (f_pdf_1 not in liste_pdf) and (f_pdf_2 not in liste_pdf) :
            #pass

            compile_file(d)

#make_all_pdf()

diff_tex_file()
go()
#a = make_tex_list(chemins)
#save_liste_tex(a)
