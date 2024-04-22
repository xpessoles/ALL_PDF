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
        "../../ExercicesCompetences",
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

def make_pdf_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier tex.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif:....}
    """
    pdf_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf"):
                    if verif(root,file) :
                        #print(file)
                        #dico = make_dico_from_tex_file(root, file)
                        #dico = {}
                        #dico["chemin"]=root
                        #dico["fichier"]=file
                        #dico["last_modif"] = os.path.getmtime(os.path.join(root, file))
                        pdf_liste.append(file)
    return pdf_liste

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

    dico = {
    'full_chemin':fich,
    'last_modif':modif,
    "chemin":root,
    "fichier":file,
    "type":['exo_comp'],
    "depot":'ExercicesCompetences',
    'chemin_git':'https://github.com/xpessoles/ExercicesCompetences/tree/main/'+root[27:]
    }

    comp = root.split("/")[-2][:5]
    comp.replace("_","-")
    #print(comp)
    #print(root)

    #fid = open(fich,'r', encoding="utf8")
    #line = fid.readline()
    #fid.close()

    return dico

def verif(root,file):
    """
    Exclusion de fichiers
    """
    test = ["STOCK",
        "../../ExercicesCompetences/Outils",
        "GPS_PPM_Colle_",
        "ALL_EXOS",
        "500_Vierge_Sujet",
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


def go(machine):
    # compilation UNIQUEMENT des fichiers modifiés
    old_tex_file = load_liste_tex(machine)
    new_tex_file = make_tex_list(chemins,machine)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder

        if d_new not in old_tex_file :

            compile_file(d_new)
        ### AREVOIR SAUVEGARDE A CHAQUE ITeRATION CI DESSOUS CA MARCHE PAS

        #On sauve la liste à chaque itération ### TEST ####
        save_liste_tex(new_tex_file[:i])
        old_tex_file = load_liste_tex()
        i=i+1

def diff_tex_file(machine):
    # affichage des fichiers modifiés
    old_tex_file = load_liste_tex(machine)
    new_tex_file = make_tex_list(chemins)
    i=0
    for d_new in new_tex_file :
        # On cherche si le fichier existe dans le fichier_sauvegarder
        if d_new not in old_tex_file :
            print(d_new)





def make_all_pdf():
    # Création de tous les PDF
    tex_liste = make_tex_list(chemins)


    for d in tex_liste :
        liste_pdf = make_pdf_list(['../PDF'])
        f_pdf_1 = d['fichier'][:-4]+'_Sujet.pdf'
        f_pdf_2 = d['fichier'][:-4]+'_Corrige.pdf'
        print(f_pdf_1,f_pdf_2)
        #return f_pdf,liste_pdf
        if (f_pdf_1 not in liste_pdf) and (f_pdf_2 not in liste_pdf) :
            #pass
            compile_file(d)


make_all_pdf()


#tex_liste = make_tex_list(chemins)
