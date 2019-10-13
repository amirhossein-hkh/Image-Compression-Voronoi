from PIL import Image
import random
import math
import numpy as np
import cv2

#reading image
I = cv2.imread("pixel1.jpg")

#reading image for edges
IG = cv2.imread("pixel1.jpg", cv2.IMREAD_GRAYSCALE)

#using the edge detction algorithm
sigma = 3

lth = 80   # low threshold
hth = 120  # high threshold
Ib = cv2.GaussianBlur(IG, (sigma,sigma), 0); # blur the image
Ec = cv2.Canny(Ib,lth, hth)

#clac prob with respecto to distance from edges
p = np.zeros(Ec.shape)
for i in range(Ec.shape[0]):
    for j in range(Ec.shape[1]):
        print(i,j,'1')
        if Ec[i][j]==255 :
            p[i][j] = 0
        else:
            c = 0
            s = 0
            k = 7
            for m in range(-k//2,k//2+1):
                for n in (-k//2,k//2+1):
                    if 0 <= i+m < Ec.shape[0] and 0 <= j+n < Ec.shape[1]:
                        c += 1
                        s += int(Ec[i+m][j+n]==255)
            p[i][j] = s/c

p = p/p.sum()

unique, counts = np.unique(p, return_counts=True)
#choosing voronoi sites with given probs

x = np.random.choice(Ec.shape[0]*Ec.shape[1],10000,replace=False,p=np.ravel(p))
points = [(f%Ec.shape[1],f//Ec.shape[1]) for f in x]


def generate_voronoi_diagram(width, height, points):
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for point in points:
        nx.append(point[0])
        ny.append(point[1])
        nr.append(I[point[1],point[0],2])
        ng.append(I[point[1],point[0],1])
        nb.append(I[point[1],point[0],0])
    for y in range(imgy):
        for x in range(imgx):
            print(y,x)
            dmin = math.hypot(imgx-1, imgy-1)
            j = -1
            for i in range(len(points)):
                d = math.hypot(nx[i]-x, ny[i]-y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("VoronoiImage.png", "PNG")
    image.show()
 
generate_voronoi_diagram(I.shape[1], I.shape[0], points)