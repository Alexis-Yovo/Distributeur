print ("1.Café(4.0 $ );2.Chocolat(5.0 $), 3.Thé(6.0 $) ou 4.Annuler?")
argent = (float)(input("Insérez des pièces: "))
cafe = 4,0 
chocolat =5,0 
the = 6,0 
ok = False
choix = (input("Faites votre choix : "))
if (choix=="Annuler")and argent<4 :
    ok!=True

if (choix=="Café") and argent >=4:
    print ("Prenez votre boisson(Café)")
    ok = True
    if argent > 4:
        print("Voici votre monnaie:", argent - 4)

if (choix=="Chocolat") and argent >=5:
    print ("Prenez votre boisson(Chocolat)")
    ok = True
    if argent > 5:
        print ("Voici votre monnaie:",argent - 5)

if (choix=="Thé") and argent >=6:
    print ("Prenez votre boisson(Thé)")
    ok = True
    if argent > 6:
         print("Voici votre monnaie:", argent - 6)

if ok != True :
    print("Vous n'avez pas assez d'argent. Veuillez réesayer")
          
    

          
