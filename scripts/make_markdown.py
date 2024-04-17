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


dico_comp={
    "A" : "Analyser.",
    "A1" : "Analyser le besoin et les exigences.",
    "A1-01" : "Décrire le besoin et les exigences.",
    "A1-02" : "Traduire un besoin fonctionnel en exigences.",
    "A1-03" : "Définir les domaines d’application et les critères technico-économiques et environnementaux.",
    "A1-04" : "Qualifier et quantifier les exigences.",
    "A1-05" : "Évaluer l’impact environnemental et sociétal.",
    "A2" : "Définir les frontières de l'analyse.",
    "A2-01" : "Isoler un système et justifier l’isolement.",
    "A2-02" : "Définir les éléments influents du milieu extérieur.",
    "A2-03" : "Identifier la nature des flux échangés traversant la frontière d’étude.",
    "A3" : "Analyser l'organisation fonctionnelle et structurelle.",
    "A3-01" : "Associer les fonctions aux constituants.",
    "A3-02" : "Justifier le choix des constituants dédiés aux fonctions d’un système.",
    "A3-03" : "Identifier et décrire les chaînes fonctionnelles du système.",
    "A3-04" : "Identifier et décrire les liens entre les chaînes fonctionnelles.",
    "A3-05" : "Caractériser un constituant de la chaîne de puissance.",
    "A3-06" : "Caractériser un constituant de la chaîne d’information.",
    "A3-07" : "Analyser un algorithme.",
    "A3-08" : "Analyser les principes d'intelligence artificielle.",
    "A3-09" : "Interpréter tout ou partie de l’évolution temporelle d’un système séquentiel.",
    "A3-10" : "Identifier la structure d'un système asservi.",
    "A4" : "Analyser les performances et les écarts.",
    "A4-01" : "Extraire un indicateur de performance pertinent à partir du cahier des charges ou de résultats issus de l'expérimentation ou de la simulation.",
    "A4-02" : "Caractériser les écarts entre les performances.",
    "A4-03" : "Interpréter et vérifier la cohérence des résultats obtenus expérimentalement, analytiquement ou numériquement. ",
    "A4-04" : "Rechercher et proposer des causes aux écarts constatés.",
    "B" : "Modéliser.",
    "B1" : "Choisir les grandeurs physiques et les caractériser.",
    "B1-01" : "Identifier les performances à prévoir ou à évaluer.",
    "B1-02" : "Identifier les grandeurs d'entrée et de sortie d’un modèle.",
    "B1-03" : "Identifier les paramètres d’un modèle.",
    "B1-04" : "Identifier et justifier les hypothèses nécessaires à la modélisation.",
    "B2" : "Proposer un modèle de connaissance et de comportement.",
    "B2-01" : "Choisir un modèle adapté aux performances à prévoir ou à évaluer.",
    "B2-02" : "Compléter un modèle multiphysique.",
    "B2-03" : "Associer un modèle aux composants des chaînes fonctionnelles.",
    "B2-04" : "Établir un modèle de connaissance par des fonctions de transfert.",
    "B2-05" : "Modéliser le signal d'entrée.",
    "B2-06" : "Établir un modèle de comportement à partir d'une réponse temporelle ou fréquentielle.",
    "B2-07" : "Modéliser un système par schéma-blocs.",
    "B2-08" : "Simplifier un modèle.",
    "B2-09" : "Modéliser un correcteur numérique.",
    "B2-10" : "Déterminer les caractéristiques d'un solide ou d'un ensemble de solides indéformables.",
    "B2-11" : "Proposer une modélisation des liaisons avec leurs caractéristiques géométriques.",
    "B2-12" : "Proposer un modèle cinématique à partir d'un système réel ou d'une maquette numérique.",
    "B2-13" : "Modéliser la cinématique d'un ensemble de solides.",
    "B2-14" : "Modéliser une action mécanique.",
    "B2-15" : "Simplifier un modèle de mécanisme.",
    "B2-16" : "Modifier un modèle pour le rendre isostatique.",
    "B2-17" : "Décrire le comportement d'un système séquentiel.",
    "B3" : "Valider un modèle.",
    "B3-01" : "Vérifier la cohérence du modèle choisi en confrontant les résultats analytiques et/ou numériques aux résultats expérimentaux.",
    "B3-02" : "Préciser les limites de validité d'un modèle.",
    "B3-03" : "Modifier les paramètres et enrichir le modèle pour minimiser l’écart entre les résultats analytiques et/ou numériques et les résultats expérimentaux.",
    "C" : "Résoudre.",
    "C1" : "Proposer une démarche de résolution.",
    "C1-01" : "Proposer une démarche permettant d'évaluer les performances des systèmes asservis.",
    "C1-02" : "Proposer une démarche de réglage d'un correcteur.",
    "C1-03" : "Choisir une démarche de résolution d’un problème d'ingénierie numérique ou d'intelligence artificielle.",
    "C1-04" : "Proposer une démarche permettant d'obtenir une loi entrée-sortie géométrique.",
    "C1-05" : "Proposer une démarche permettant la détermination d’une action mécanique inconnue ou d'une loi de mouvement.",
    "C2" : "Mettre en œuvre une démarche de résolution analytique.",
    "C2-01" : "Déterminer la réponse temporelle.",
    "C2-02" : "Déterminer la réponse fréquentielle.",
    "C2-03" : "Déterminer les performances d'un système asservi.",
    "C2-04" : "Mettre en œuvre une démarche de réglage d’un correcteur.",
    "C2-05" : "Caractériser le mouvement d’un repère par rapport à un autre repère.",
    "C2-06" : "Déterminer les relations entre les grandeurs géométriques ou cinématiques.",
    "C2-07" : "Déterminer les actions mécaniques en statique.",
    "C2-08" : "Déterminer les actions mécaniques en dynamique dans le cas où le mouvement est imposé.",
    "C2-09" : "Déterminer la loi de mouvement dans le cas où les efforts extérieurs sont connus.",
    "C3" : "Mettre en œuvre une démarche de résolution numérique.",
    "C3-01" : "Mener une simulation numérique.",
    "C3-02" : "Résoudre numériquement une équation ou un système d'équations.",
    "C3-03" : "Résoudre un problème en utilisant une solution d'intelligence artificielle.",
    "D" : "Expérimenter.",
    "D1" : "Mettre en œuvre un système.",
    "D1-01" : "Mettre en œuvre un système en suivant un protocole.",
    "D1-02" : "Repérer les constituants réalisant les principales fonctions des chaînes fonctionnelles.",
    "D1-03" : "Identifier les grandeurs physiques d’effort et de flux.",
    "D2" : "Proposer et justifier un protocole expérimental.",
    "D2-01" : "Choisir le protocole en fonction de l'objectif visé.",
    "D2-02" : "Choisir les configurations matérielles et logicielles du système en fonction de l'objectif visé par l'expérimentation.",
    "D2-03" : "Choisir les réglages du système en fonction de l'objectif visé par l'expérimentation.",
    "D2-04" : "Choisir la grandeur physique à mesurer ou justifier son choix.",
    "D2-05" : "Choisir les entrées à imposer et les sorties pour identifier un modèle de comportement.",
    "D2-06" : "Justifier le choix d’un capteur ou d’un appareil de mesure vis-à-vis de la grandeur physique à mesurer.",
    "D3" : "Mettre en œuvre un protocole expérimental.",
    "D3-01" : "Régler les paramètres de fonctionnement d'un système.",
    "D3-02" : "Mettre en œuvre un appareil de mesure adapté à la caractéristique de la grandeur à mesurer.",
    "D3-03" : "Effectuer des traitements à partir de données.",
    "D3-04" : "Identifier les erreurs de mesure.",
    "D3-05" : "Identifier les erreurs de méthode.",
    "E" : "Communiquer.",
    "E1" : "Rechercher et traiter des informations.",
    "E1-01" : "Rechercher des informations.",
    "E1-02" : "Distinguer les différents types de documents et de données en fonction de leurs usages.",
    "E1-03" : "Vérifier la pertinence des informations (obtention, véracité, fiabilité et précision de l'information).",
    "E1-04" : "Extraire les informations utiles d’un dossier technique.",
    "E1-05" : "Lire et décoder un document technique.",
    "E1-06" : "Trier les informations selon des critères.",
    "E1-07" : "Effectuer une synthèse des informations disponibles dans un dossier technique.",
    "E2" : "Produire et échanger de l'information.",
    "E2-01" : "Choisir un outil de communication adapté à l’interlocuteur.",
    "E2-02" : "Faire preuve d’écoute et confronter des points de vue.",
    "E2-03" : "Présenter les étapes de son travail.",
    "E2-04" : "Présenter de manière argumentée une synthèse des résultats.",
    "E2-05" : "Produire des documents techniques adaptés à l'objectif de la communication.",
    "E2-06" : "Utiliser un vocabulaire technique, des symboles et des unités adéquats.",
    "F" : "Concevoir",
    "F1" : "Concevoir l'architecture d'un système innovant",
    "F1-01" : "Proposer une architecture fonctionnelle et organique.",
    "F2" : "Proposer et choisir des solutions techniques",
    "F2-01" : "Modifier la commande pour faire évoluer le comportement du système."}


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


    if chap_rep == 'cin' or chap_rep == 'stat':
        fid = open("C:/GitHub/xpessoles.github.io/docs/Revisions/"+chap_rep+"/"+chap_file+".md",'w',encoding='utf8')
    else :
        fid = open("C:/GitHub/xpessoles.github.io/docs/PSI/"+chap_rep+"/"+chap_file+".md",'w',encoding='utf8')



    ## Titre de la page
    fid.write('---\n')
    fid.write('title: '+dico_titre_chapitre[chapitre]+" \n")
    fid.write('---\n\n')

    write_comp(liste_dico_file,fid,chapitre)

    ## Le cours
    write_activite('cours',liste_dico_file,fid,chapitre)

    ## Les applications
    write_activite('application',liste_dico_file,fid,chapitre)

    ## Les TD
    write_activite('td',liste_dico_file,fid,chapitre)

    ## Les colles
    write_activite('colle',liste_dico_file,fid,chapitre)

    fid.write("\n")
    fid.close()


def write_activite(activite,liste_dico_file,fid,chapitre) :
    # on écrit pour une activite td, application o colle

    titre_activite = ""
    if activite == "td" :
        titre_activite = "Travaux Dirigés"
    elif activite == "application" :
        titre_activite = "Applications"
    elif activite == "cours" :
        titre_activite = "Cours"
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

def write_comp(liste_dico_file,fid,chapitre):
    #Recupère la liste des compétences d'un chapitre
    liste_comp_chap = []
    for file in liste_dico_file :
        if file['chapitre'] == chapitre :
            print(">>"+file['fichier'])
            tuple_comp = file['comp']
            for c in tuple_comp :
                liste_comp_chap.append(c)
    print(liste_comp_chap)
    return None



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

#make_page_chapitre(liste_dico_file,dico_titre_chapitre,"slci_laplace")

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
