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
    "A5-05": "Décoder les spécifications géométriques par taille, par zone et par gabarit.",
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
    "B2-22":"Modéliser un convertisseur électromécanique.",
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
    "C1-06" : "Proposer une démarche permettant de déterminer des grandeurs électriques.",
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
    "C2-10" : "Déterminer les grandeurs relatives au comportement d'une poutre.",
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
    "F2-01" : "Modifier la commande pour faire évoluer le comportement du système.",
    "G2-01" : "Choisir et ordonnancer des procédés de fabrication du matériau à la pièce finie."
}

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
    dico["comp"]=comp
    #print(comp)
    #print(root)

    # Recherche de corrigé
    fid = open(fich,'r',encoding="utf8")
    data = fid.readlines()
    fid.close()
    cor = False
    for line in data :
        if "\correctiontrue" in line:
            cor = True
    #print(cor)
    dico['corrige'] = cor
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
        "500_Vierge",
        "1100_Pneumatique",
        "B2_13_04_RR",
        "B2_13_05_RT",
        "Exerc_test_Sujet",
        "test"
    ]
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True

def compile_file(dict):

    # Compilation du sujet
    # On copie la base
    dest = dict["fichier"] # fichier.tex
    dest = dict['comp']+"_"+dest[:-4]+"_Sujet.tex"
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
    dest = dict['comp']+"_"+dest[:-4]+"_Corrige.tex"
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
    nom_fichier = 'activites_tex_liste_'+machine+'.save'
    file = open(nom_fichier, 'wb')
    pickle.dump(data, file)
    file.close()

def load_liste_tex(machine) :
    # Charger la liste des fichiers tex
    nom_fichier = 'activites_tex_liste_'+machine+'.save'
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
        f_pdf_1 = d['comp']+"_"+d['fichier'][:-4]+'_Sujet.pdf'
        f_pdf_2 = d['comp']+"_"+d['fichier'][:-4]+'_Corrige.pdf'
        print(f_pdf_1,f_pdf_2)
        #return f_pdf,liste_pdf
        if (f_pdf_1 not in liste_pdf) and (f_pdf_2 not in liste_pdf) :
            #pass
            compile_file(d)



def make_nav(dico):
    # RENVOIE LA LISTE DES CHAPITRE
    # On crée la nav du site
    chap = []
    for d in dico :
        c = d['comp'].replace('_','-')
        if c not in chap :
            chap.append(c)

        # Vérif que les fichiers ont un chapitre
        if d['comp'] == '':
            print(d['fichier'])
            print(d['chapitre'])

    """
    Création du fichier du paragraphe de nav à ajouter dans mkdocs.yml
    """
    chap.sort()

    fid = open("nav_activites.yml","w",encoding = 'utf8')
    fid.write('- Activités SII: \n')
    fid.write('    - activites/index.md \n')

    for c in chap:
        fid.write('    - '+c+' : activites/'+c+'.md\n')
    fid.close()

    print("Modifier le fichier mkdocs.yml")
    return chap

def creation_fichiers_activites(chap_comp,liste_dico_act):
    """
    Création de fichiers correspondants aux activités
    """
    print("Creation d'un fichier md par compétence.")

    for comp in chap_comp :
        fid = open("C:\\GitHub\\xpessoles.github.io\\docs\\activites\\"+comp+".md","w",encoding = 'utf8')
        id_comp = comp

        titre_comp = dico_comp[comp]


        ## Titre de la page & Tags
        fid.write('---\n')
        fid.write('title: '+titre_comp+" \n")
        fid.write("tags:\n")
        fid.write('  - '+comp+"\n")
        fid.write('---\n')

        fid.write('[comment]: <> (Généré automatiquement par make_all_activitess.py, creation_fichiers_activites)\n\n')


        fid.write("##"+titre_comp +" \n")
        # On cherche toutes les activités
        liste_act = []
        for file in liste_dico_act :

            if file['comp'].replace("_","-") == id_comp :
                liste_act.append(file)


        fid.write("| Activités | Sujet | Corrigé | Sources  | \n")
        fid.write("| :-------------- | :---: | :-----: | :------: | \n")
        for act in liste_act :
            fid.write("| "+act['fichier'][:-4]+ " | ")
            fid.write("[:fontawesome-solid-file-pdf:](http://xpessoles-cpge.fr/pdf/"+act['comp']+"_"+act['fichier'][:-4]+"_Sujet.pdf) | ")
            if act['corrige'] :
                fid.write("[:fontawesome-solid-file-pdf:](http://xpessoles-cpge.fr/pdf/"+act['comp']+"_"+act['fichier'][:-4]+"_Corrige.pdf) |")
            else:
                fid.write("[:fontawesome-regular-file-pdf:](http://xpessoles-cpge.fr/pdf/"+act['comp']+"_"+act['fichier'][:-4]+"_Corrige.pdf) | ")


            fid.write("[:material-github:]("+act['chemin_git']+") |  \n")


        fid.write("\n")



        fid.close()







#make_all_pdf()

tex_liste = make_tex_list(chemins)
#save_liste_tex(tex_liste,PC)
#nav = make_nav(tex_liste)

#creation_fichiers_activites(nav,tex_liste)
def compte_activite(comp,tex_liste):
    cpt = 0
    for d in tex_liste :
        if d['comp'] == comp.replace('-','_') :
            cpt = cpt+1
    return cpt

for k,v in dico_comp.items():
    cc = compte_activite(k,tex_liste)
    print("| "+k+" | "+v+" | __"+str(cc)+"__ |")