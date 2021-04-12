from PIL import Image
##from IPython.display import display
#import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open("zaha.jpg")
im_palace = Image.open("palace-resize.jpg")

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size
im_new = Image.new("RGB", (width, height), (255, 255, 255))
def zaha():
# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
    for x in range(width):
        for y in range(0,height,1):

            pixel = im.getpixel((x, y))
            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]
            im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(100,200):
        for y in range(200,263):

            pixel = im_palace.getpixel((x-100, y-200))
            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]
            im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))



    # valeurs des couleurs rouge, vert, bleu
##            p_rouge = pixel[0]
##            p_vert =  pixel[1]
##            p_bleu =  pixel[2]
##
##    # modification du pixel de coordonnées x, y
##            p_bleu = 0
##
##            im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    # affichage de l'image
    im_new.save("sortie.png")
    im_new.show()

zaha()
