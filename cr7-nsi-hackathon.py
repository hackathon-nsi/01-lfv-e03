from PIL import Image

#je donne les 2 images au programme 
juv = Image.open('juv.jpg')

rma = Image.open('cr7rma-resize.jpg')

#taille
juv = juv.resize((1200,693))

juv_size = juv.size

rma_size = rma.size

#j'ouvre une image blanche et je colle mes 2 images dessus
blanc = Image.new('RGB',(2*juv_size[0], juv_size[1]), (250,250,250))

blanc.paste(juv,(0,0))

blanc.paste(rma,(juv_size[0],0))

#je montre et je sauvegarde la nouvelle image, contenant les 2 images collé dessus
blanc.save("merged.jpg")

blanc.show()
