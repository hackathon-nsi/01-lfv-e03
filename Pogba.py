from __future__ import division
from PIL import Image 
import math
import os

img = Image.open("pog.jpg")

width, height = img.size
new_img= Image.new("RGB",(height,width),(255,255,255))

def long_slice(image_path, out_name, outdir, slice_size):
    """slice an image into parts slice_size tall"""
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))

    count = 1
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  

        bbox = (left, upper, width, lower)
        new_img = img.crop(bbox)
        upper += slice_size
        #save the slice
        new_img.save(os.path.join(outdir,out_name + "_" + str(count)+".png"))
        count +=1
        img1= Image.open("pogba_1.png")
        img2= Image.open("pogba_2.png")
        img3= Image.open("pogba_3.png")
        img4= Image.open("pogba_4.png")
        new_img= Image.new('RGB', (img1.width, img1.height + img2.height + img3.height + img4.height),(255,255,255))
        new_img.paste(img1, (0, 0))
        new_img.paste(img2, (0, 100))
        new_img.paste(img3, (0, 210))
        new_img.paste(img4, (0, 320))
        new_img.save("zzz.jpg")
        new_img.show()
        time.show(1)
       
        
        
if __name__ == '__main__':
    long_slice("pog.jpg","pogba", os.getcwd(), 90)


