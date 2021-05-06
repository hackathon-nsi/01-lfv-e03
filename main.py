from PIL import Image

#yanik fait le menu qui demande quel image l'on voudrait ouvrir

from fonction_zaha import*


from fonction_ronaldo import*


from fonction_pogba import*



x = input("Si vous voulez voir une image de Zaha tapez: zaha; si vous voulez voir une image de ronaldo tapez: cr7; et si vous voulez voir une image de pogba tapez:pogba") )

if x == "zaha":
    zaha()

elif x == "cr7":
    cr7()
    
elif x=="pogba":
    pogba()
