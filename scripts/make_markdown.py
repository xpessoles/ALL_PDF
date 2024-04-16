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

liste_chapitres = ['chs_', 'chs_hs', 'chs_leq', 'cin_geo', 'cin_point', 'cin_va', 'dyn_', 'dyn_1d', 'dyn_cin', 'dyn_inertie', 'dyn_pfd', 'dyn_pfd_cf', 'dyn_pfd_co', 'dyn_pfd_vehicule', 'slci_ap', 'slci_blocs', 'slci_bode', 'slci_commande', 'slci_correcteur', 'slci_correcteurs', 'slci_laplace', 'slci_multiphy', 'slci_p', 'slci_pi', 'slci_precision', 'slci_rapidite', 'slci_revisions', 'slci_rp', 'slci_stabilite', 'slci_synthese', 'stat_frot', 'stat_mam', 'stat_pfs_2d', 'stat_pfs_3d', 'tec_', 'tec_1d', 'tec_3d', 'tec_jeq', 'tec_vehicule']
dico_titre_chapitre = {ch:"" for ch in liste_chapitres}
dico_titre_chapitre = {
    'chs_': 'Théorie des mécanismes',
    'chs_hs': 'Théorie des mécanismes',
    'chs_leq': 'Liaisons équivalentes',
    'cin_geo': 'Géométrie',
    'cin_point': 'Cinématique du point',
    'cin_va': 'Résolution cinématique',
    'dyn_': 'Dynamique',
    'dyn_1d': 'Résolution du PFD dans des systèmes 1D',
    'dyn_cin': 'Détemination du torseur dynamique',
    'dyn_inertie': 'Caractéristiques inertielles',
    'dyn_pfd': 'Résolution du PFD',
    'dyn_pfd_cf': 'PFD - Chaînes fermées',
    'dyn_pfd_co': 'PFD - Chaînes ouvertes',
    'dyn_pfd_vehicule': 'PFD - Véhicules',
    'slci_ap': 'Correcteur à avance de phase',
    'slci_blocs': 'Modélisation par schéma-blocs',
    'slci_bode': 'Analyse fréquentielle des SLCI',
    'slci_commande': 'Commande des SLCI',
    'slci_correcteur': 'Correcteurs des SLCI',
    'slci_correcteurs': 'Correcteurs des SLCI',
    'slci_laplace': 'Transformée de Laplace',
    'slci_multiphy': 'Modélisation polyphysique',
    'slci_ordre12': "Systèmes d'ordre 1 et 2",
    'slci_p': 'Correcteur proportionnel',
    'slci_pi': 'Correcteur proportionnel intégral',
    'slci_precision': 'Précision des systèmes',
    'slci_rapidite': 'Rapidité des systèmes',
    'slci_revisions': 'SLCI Révisions',
    'slci_rp': 'Correcteur à retard de phase',
    'slci_stabilite': 'Stablité des systèmes',
    'slci_synthese': 'SLCI Synthèse',
    'stat_frot': 'Frottement sec',
    'stat_mam': 'Modélisation des AM',
    'stat_pfs_2d': 'Résolution du PFS 2D',
    'stat_pfs_3d': 'Résolution du PFS 3D',
    'tec_': 'Energétique',
    'tec_1d': 'TEC Mouvements simples',
    'tec_3d': 'TEC Mouvements complexes',
    'tec_jeq': 'Inertie équivalente',
    'tec_vehicule': 'TEC Véhicules'}
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



def make_page_chapitre(liste_dico_file,dico_titre_chapitre,chapitre):
    # Créer la page d'un chapitre considéré.
    chap_file = chapitre.replace("_","-")
    chap_rep = chap_file.split("-")[0]
    fid = open("C:/GitHub/xpessoles.github.io/docs/PSI/"+chap_rep+"/"+chap_file+".md",'w',encoding='utf8')
    ## Titre de la page
    fid.write('---\n')
    fid.write('title: '+dico_titre_chapitre[chapitre]+" \n")
    fid.write('---\n\n')



    ## Le cours


    ## Les applications
    write_activite('application',liste_dico_file,fid)

    ## Les TD
    write_activite('td',liste_dico_file,fid)

    ## Les colles
    write_activite('colle',liste_dico_file,fid)

    fid.write("\n")
    fid.close()


def write_activite(activite,liste_dico_file,fid) :
    # on écrit pour une activite td, application o colle

    titre_activite = ""
    if activite == "td" :
        titre_activite = "Travaux Dirigés"
    elif activite == "application" :
        titre_activite = "Applications"
    if activite == "colle" :
        titre_activite = "Colles"

    # On cherche toutes les TD
    liste_td = []
    for file in liste_dico_file :
        if file['chapitre'] == chapitre and (activite in file['type']):
            liste_td.append(file)
    # S'il y a des TD
    if liste_td != [] :
        fid.write("### "+titre_activite+" \n \n")
        fid.write("| "+titre_activite+" | Sujet | Corrigé | Sources  | \n")
        fid.write("| :-------------- | :---: | :-----: | :------: | \n")
        for td in liste_td :
            fid.write("| "+td['titre']+ " | ")
            fid.write("[:fontawesome-solid-file-pdf:](http://xpessoles-cpge.fr/pdf/"+td['fichier'][:-4]+"_Sujet.pdf) | ")
            if td['corrige'] :
                fid.write("[:fontawesome-solid-file-pdf:](http://xpessoles-cpge.fr/pdf/"+td['fichier'][:-4]+"_Corrige.pdf) | \n")
            else:
                fid.write("[:fontawesome-regular-file-pdf:](http://xpessoles-cpge.fr/pdf/"+td['fichier'][:-4]+"_Corrige.pdf) | \n")

    fid.write("\n")



def make_nav(dico):
    # RENVOIE LA LISTE DES CHAPITRE
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
liste_dico_file = make_tex_list(chemins)

make_page_chapitre(liste_dico_file,dico_titre_chapitre,"slci_laplace")

for chapitre in liste_chapitres :
    make_page_chapitre(liste_dico_file,dico_titre_chapitre,chapitre)


"""chap = make_nav(a)
for c in chap :
    if "" in c :
        print(c)
"""
"""
for d in a :
    if "stat_pds_2d" in d['chapitre']:
        print(print(d['fichier']))
"""
