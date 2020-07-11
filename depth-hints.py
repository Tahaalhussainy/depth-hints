import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

def opencv2matplot(src):
    """
          Convert opencv color channels to matplot color channels
    """
    b, g, r = cv2.split(src)
    return cv2.merge([r, g, b])
format_image=".png"
url=input("Enter image 1 and 2 image select number=")

im1 = cv2.imread(r"assets/"+ url +format_image)
convert_image=int(url)
url_image1="datasets"
url_image2="assest"
img1=""
if convert_image==1:
    img1=cv2.imread(r""+url_image1+"/"+url_image2+"/"+"3"+format_image)
if convert_image==2:
    img1=cv2.imread(r""+url_image1+"/"+url_image2+"/"+"4"+format_image)    
url_image3="datasets"

images = [im1,img1]
img_title = ['1 image','2 image']
for i, img in enumerate(images):
    plt.subplot(1, 2, i+1)
    plt.imshow(opencv2matplot(img))
    plt.title(img_title[i])

plt.show()
 
cv2.waitKey(0)  
cv2.destroyAllWindows()  
