    # -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
# -- JEU DU PENDU --
import random 

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#VERSION CONSOLE

def initialisation():
    global mot_choisi,lettres_mot,mot_jeu
    fichier=open('dico.txt','r')     #ouverture du dico 
    liste=fichier.readlines()        #liste des mots
    fichier.close()  

    mot_choisi=random.choice(liste).strip()  #sélection du mot
    lettres_mot=list(mot_choisi)                    #liste des lettes du mot
    mot_jeu=[lettres_mot[0]] + ['_'] * (len(lettres_mot) - 1)          #liste de la progression du mot



def pendu():
    global mot_choisi,lettres_mot,mot_jeu,nb_erreurs
    chances=8
    nb_erreurs=0                                     #nombres de chances
    lettres_saisies=[]                  #liste des lettes saisies par le joueur
 
    print('le mot est',mot_choisi)     #PROVISOIRE 
    print (' '.join(mot_jeu))
  
    while chances!=0:
        lettre = raw_input('Entrez votre lettre: ')
 
        if lettre not in alphabet:
            print('Le caractère entré n\'est pas une lettre.')
        elif '_' not in mot_jeu:
            print('Vous avez déjà deviné toutes les lettres. Vous avez gagné!')
            break
        elif lettre in lettres_saisies:
            print('La lettre a déjà été choisie. Plus que', chances, 'chances restantes.')
            if lettres_saisies:
                print('Vous avez saisi les lettres:', ', '.join(lettres_saisies))
            else:
                print('Vous n\'avez saisi aucune lettre.')
        elif lettre in lettres_mot:
            lettres_saisies.append(lettre)
            for i in range(len(lettres_mot)):
                if lettres_mot[i] == lettre:
                    mot_jeu[i] = lettre
            print(' '.join(mot_jeu))
            if lettres_saisies:
                print('Vous avez saisi les lettres:', ', '.join(lettres_saisies))
            else:
                print('Vous n\'avez saisi aucune lettre.')
        else:
            chances -= 1
            nb_erreurs += 1
            lettres_saisies.append(lettre)
            print('La lettre n\'est pas dans le mot. Plus que', chances, 'chances restantes.')
            if lettres_saisies:
                print('Vous avez saisi les lettres:', ', '.join(lettres_saisies))
            else:
                print('Vous n\'avez saisi aucune lettre.')

    if chances == 0:
        print('Perdu :/')


initialisation()
pendu()
