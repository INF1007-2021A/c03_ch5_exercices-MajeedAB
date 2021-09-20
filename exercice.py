#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math


def convert_to_absolute(number: float) -> float:
    if number>=0:
        return number
    else:
        return -number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    prenoms = []
    for pre in prefixes:
        prenoms.append(pre+suffixe)
    return prenoms


def prime_integer_summation() -> int:
    somme = 0
    liste_premiers = []
    nb_test = 2
    for i in range(100):
        est_premier=False
        while(est_premier==False): #boucle tant qu'on a pas trouvé de nbr premier
            est_premier = True
            #testez s'il est premier
            racine = math.sqrt(nb_test)
            for facteur in liste_premiers: #on teste tous les facteurs premiers precedents sur notre nb_test
                if(facteur<=racine):
                    if(nb_test%facteur==0):
                        est_premier = False
                        nb_test+=1
                        break   #nbr pas premier
                else:
                    break #nbr premier
        liste_premiers.append(nb_test)
        somme+=nb_test
        nb_test+=1
        #on a trouve un premier
    return somme


def factorial(number: int) -> int:
    resultat = 1
    for i in range(2,number+1):
        resultat*=i
    return resultat


def use_continue() -> None:
    for i in range(1,11):
        if(i==5):
            continue
        else:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    liste_de_verification = []
    for groupe in groups:
        if(len(groupe)>10 or len(groupe)<=3):
            liste_de_verification.append(False)
            continue
        else: #critere de taille respecté
            critere_age_fini = False
            for age in groupe:
                if(age==25):    #condition prioritaire
                    liste_de_verification.append(True)
                    critere_age_fini = True
                    break
            if(critere_age_fini):
                continue
            un_plus_que_70 = False
            un_50 = False
            for age in groupe: #il n'y a pas de 25 ans
                if(age<18):
                    liste_de_verification.append(False)
                    critere_age_fini = True
                    break
                if(age==50):
                    un_50 = True
                if(age>70):
                    un_plus_que_70 = True
            if(un_50 and un_plus_que_70):
                liste_de_verification.append(False)
            elif(critere_age_fini==False):
                liste_de_verification.append(True)

    return liste_de_verification


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
