from PIL import Image
##from IPython.display import display
#import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open("zaha.jpg")
im_palace = Image.open("palace-resize.jpg")
im_ic = Image.open("ivory-coast-resize.jpg")
im_pl = Image.open("pl-resize.jpg")
width, height = im_palace.size

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size
im_new = Image.new("RGB", (width, height), (255, 255, 255))
def zaha():

# créer des variables, pour rendre la modification plus simple
    a = 200
    b = 300
    c = 760
    d = 860

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
    for x in range(width):
        for y in range(0,height):

            pixel = im.getpixel((x, y))
            p_rouge = pixel[0]
            p_vert =  pixel[1]
            p_bleu =  pixel[2]
            im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))



# Construire le numéro 11 avec les logos et le drapeau

#Le premier 1 du 11

    for x in range(70,170):
        for y in range(100,163):

                pixel = im_palace.getpixel((x-70, y-100))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(a,b):
        for y in range(100,163):

                pixel = im_ic.getpixel((x-a, y-100))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(a,b): 
        for y in range(200,263):

                pixel = im_pl.getpixel((x-a, y-200))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(a,b):
        for y in range(b,363):

                pixel = im_palace.getpixel((x-a, y-b))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(a,b):
        for y in range(400,463):

                pixel = im_ic.getpixel((x-a, y-400))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(a,b):
        for y in range(500,563):

                pixel = im_pl.getpixel((x-a, y-500))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))


# Le deuxième 1 du 11



    for x in range(630,730):
        for y in range(100,163):

                pixel = im_palace.getpixel((x-630, y-100))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))


    for x in range(c,d):
        for y in range(100,163):

                pixel = im_palace.getpixel((x-c, y-100))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(c,d):
        for y in range(100,163):

                pixel = im_ic.getpixel((x-c, y-100))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(c,d):
        for y in range(a,263):

                pixel = im_pl.getpixel((x-c, y-a))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(c,d):
        for y in range(b,363):

                pixel = im_palace.getpixel((x-c, y-b))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(c,d):
        for y in range(400,463):

                pixel = im_ic.getpixel((x-c, y-400))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))

    for x in range(c,d):
        for y in range(500,563):

                pixel = im_pl.getpixel((x-c, y-500))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))



#sauvegarder et montrer l'image manipulé
                
    im_new.save("sortie.png")
    im_new.show()

zaha()








