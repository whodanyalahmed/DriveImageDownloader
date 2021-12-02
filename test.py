from PIL import Image
import os
# image1 = Image.open(r'C:\Users\Ron\Desktop\Test\image1.png')
# image2 = Image.open(r'C:\Users\Ron\Desktop\Test\image2.png')
# image3 = Image.open(r'C:\Users\Ron\Desktop\Test\image3.png')
# image4 = Image.open(r'C:\Users\Ron\Desktop\Test\image4.png')
 
# im1 = image1.convert('RGB')
# im2 = image2.convert('RGB')
# im3 = image3.convert('RGB')
# im4 = image4.convert('RGB')




# imagelist = [im2,im3,im4]

# im1.save(r'C:\Users\Ron\Desktop\Test\myImages.pdf',save_all=True, append_images=imagelist)

path = os.getcwd()+'\\test'
# get all the files in the path
files = os.listdir(path)
print(files)
imgList = []
for file in files:
    print(file)
    image = Image.open(path+'\\'+file)
    image.convert('RGB')
    imgList.append(image)
image.save(path+'\\'+'All.pdf',save_all=True, append_images=imgList)