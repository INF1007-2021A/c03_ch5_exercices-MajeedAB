import math

def prime_integer_summation_MAX(count) -> int:
    liste_premiers = []
    nombre_teste = 2
    while len(liste_premiers) < count:
        prime = True
        racine = math.sqrt(nombre_teste)
        for premier in liste_premiers:
            if nombre_teste%premier == 0:
                prime = False
                break
            if premier >= racine:
                break
        if prime:
            liste_premiers.append(nombre_teste)
        nombre_teste += 1
    return(sum(liste_premiers))



def prime_integer_summation_MAJ(count) -> int:
    somme = 0
    liste_premiers = []
    nb_test = 2
    for i in range(count):
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
        # print(nb_test)
        nb_test+=1
        #on a trouve un premier
    return somme

print("MAJ")
prime_integer_summation_MAJ(300000)

print("MAX")
prime_integer_summation_MAX(300000)
