from PIL import Image

#yanik fait le menu qui demande quel image l'on voudrait ouvrir

from fonction_zaha import*


from fonction_ronaldo import*



x = input("Si vous voulez voir une image de Zaha tapez: zaha; si vous voulez voir un image de ronaldo tapez: cr7")

if x == "zaha":
    zaha()

elif x == "cr7":
    cr7()
