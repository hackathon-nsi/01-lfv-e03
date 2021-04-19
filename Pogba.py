from PIL import Image
##from IPython.display import display
#import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open("pog.jpg")

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size
im_new = Image.new("RGB", (width, height), (255,255,255))
# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
def pogba():   
        for x in range(width):
            for y in range(0,height):

                pixel = im.getpixel((x, y))
                p_rouge = pixel[0]
                p_vert =  pixel[1]
                p_bleu =  pixel[2]
                im_new.putpixel((x,y),(p_rouge, p_vert, p_bleu))
    
        for x in range(0,height):
            for y in range(0,width):
                a= (x, y, x+width, y+height)
                b= im.crop(a)

# sauvegarder la nouvelle image et la montrer             
        im_new.save("outcome.png")
        im_new.show()

pogba()
