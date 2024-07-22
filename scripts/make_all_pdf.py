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
     % "{'classe':(''),'chapitre':'','type':(''),'titre':'', 'source':' ','comp':(None),'corrige':True}"
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
        d = eval(d)
        for k,v in d.items():
            dico[k]=v

    dico['sujet'] = dico['fichier'][:-4]+'_Sujet.pdf'
    dico['corrige'] = dico['fichier'][:-4]+'_Corrige.pdf'


    if ('type' in line) and (dico["type"] == 'cours') :
        dico['sujet'] = d["chapitre"]+"_"+dico['fichier'][:-4]+'.pdf'
        dico['corrige'] = d["chapitre"]+"_"+dico['fichier'][:-4]+'.pdf'

    dico['lien_sujet']="https://xpessoles-cpge.fr/pdf/"+dico['sujet']
    dico['lien_corrige']="https://xpessoles-cpge.fr/pdf/"+dico['corrige']

    return dico

def verif(root,file):
    """
    Exclusion de fichiers
    """
    test = ["old","QCM","Headings",
    "QCM","OLD","xx","TODO","macros",
    #"Cours",
     #"cours",
    "Old",
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

def compile_file(dict):

    # Compilation du sujet
    # On copie la base
    dest = dict["sujet"] # fichier.tex
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
    # Donne la liste des dictionnaire des fichiers à recompiler
    old_tex_file = load_liste_tex(machine)
    new_tex_file = make_tex_list(chemins)
    print("SAV : ",len(old_tex_file)," NOW :",len(old_tex_file))
    i=0
    diff_tex = []
    for d_new in new_tex_file :
        # On cherche le ditionnaire correspondant en regardant le full_chemin.
        for d_old in old_tex_file :
            if d_old['full_chemin'] == d_new['full_chemin'] :
                # Si les timestamp sont différents, on stocke
                if d_old['last_modif'] != d_new['last_modif']:
                    diff_tex.append(d_new)

    print(diff_tex)
    return (diff_tex)



def make_all_pdf(PC):
    # Création de TOUS les PDF et Reecriture du point de sauvegarde

    tex_liste = make_tex_list(chemins)
    #liste_pdf = os.listdir("../PDF")

    for d in tex_liste :
        print(d['fichier'])
        f_pdf_1 = d['fichier'][:-4]+'_Sujet.pdf'
        f_pdf_2 = d['fichier'][:-4]+'_Corrige.pdf'
        #print(f_pdf_1,f_pdf_2)
        #return f_pdf,liste_pdf
        #if (f_pdf_1 not in liste_pdf) and (f_pdf_2 not in liste_pdf) :
            #pass
        compile_file(d)
    save_liste_tex(tex_liste,PC)


def go(machine):
    # compilation UNIQUEMENT des fichiers modifiés
    diff_tex = diff_tex_file(machine)
    while diff_tex :
        for d in diff_tex :
            print(d['fichier'])
            f_pdf_1 = d['fichier'][:-4]+'_Sujet.pdf'
            f_pdf_2 = d['fichier'][:-4]+'_Corrige.pdf'

            compile_file(d)

        new_tex_file = make_tex_list(chemins)
        save_liste_tex(new_tex_file,machine)
        diff_tex = diff_tex_file(machine)


def get_chapitre_liste(tex_liste):
    # Création de la liste des chapitres
    dico_chap = {}
    for d in tex_liste :
        if d['chapitre'] not in dico_chap :
           dico_chap[d["chapitre"]]=1
        else :
            dico_chap[d["chapitre"]]+=1
    return list(dico_chap.keys())






PC = "perso"
#go(PC)
#make_all_pdf(PC)

# SAUVEGARDE DES FICHIERS TEX
#tex_liste = make_tex_list(chemins)
#save_liste_tex(tex_liste,PC)

tex_liste = make_tex_list(chemins)
cours_liste = []
for d in tex_liste :
    if "Cours" in d["fichier"] or "cours" in d["fichier"]:
        cours_liste.append(d)

for d in cours_liste :
    print(d['sujet'])
    compile_file(d)
#diff_tex_file(PC)
# go()
# a = make_tex_list(chemins)
# save_liste_tex(a)
