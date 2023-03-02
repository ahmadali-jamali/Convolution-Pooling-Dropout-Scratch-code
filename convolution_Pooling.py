#...............inrto..................#

'''
           image processing project
              convolution_pooling_dropOut
                Ahmadali Jamali
                 02.15.2022
                  Teheran
                                    '''

#..............libraries...............#

import numpy as np
import math 
from skimage import io, img_as_float
import cv2
import random

#.............Functions................#

#pooling function:
def pooling(image):

    l = len(image)
    le = len(image[0])
    
    if l/2 != 0:
       l = l-1
       
    if le/2 != 0:
       le = le-1
       
    pool = []
    for i in range(0,l,2):
        pool1 = []
        
        for j in range(0,le,2):
            p1 = []
            p1.append(image[i][j])
            p1.append(image[i+1][j+1])
            p1.append(image[i][j+1])
            p1.append(image[i+1][j])
            pm = max(p1)
            pool1.append(pm)
        pool.append(pool1)    
        
    return np.array(pool)

def drop_out(image):
    
    l = len(image)
    le = len(image[0])
    
    if l/2 != 0:
       l = l-1
       
    if le/2 != 0:
       le = le-1
       
    pool = []
    for i in range(0,l,2):
        pool1 = []
        
        for j in range(0,le,2):
            p1 = []
            p1.append(image[i][j])
            p1.append(image[i+1][j+1])
            p1.append(image[i][j+1])
            p1.append(image[i+1][j])
            drop = []
            for _ in range(2):
                a = random.randint(0,3)
                drop.append(p1[a])
                
            pm = max(drop)
            pool1.append(pm)
        pool.append(pool1)    
        
    return np.array(pool)
    

#...............input..................#

#main function:
def main():

    #load image / gray and float 
    img = img_as_float(io.imread('wo.jpg',as_gray = True))

    #kernel
    kernel = np.ones((5,5),np.float32)/25
    gaussian_kernel = np.array([[1/16, 1/4, 1/16],
                                [1/8, 1/4,  1/8],
                                [1/16, 1/8, 1/16]])



    # design your own Convolution pooling road map:
    
    #like: Convolution --->Pooling ---> Convolution ---> pooling ---> convolution ---> Unpooling
    
    #convolution
    conv_using_cv2 = cv2.filter2D(img, -1, gaussian_kernel, borderType = cv2.BORDER_CONSTANT)

    #output/show
    #orginal image:
    cv2.imshow('org',img)
   
    #convolution
    cv2.imshow('conv',conv_using_cv2)

    #pooling image
    p = pooling(img)
    cv2.imshow('pooling',p)
    cv2.imshow('conv',conv_using_cv2)

    conv = cv2.filter2D(p, -1, gaussian_kernel, borderType = cv2.BORDER_CONSTANT)
    cv2.imshow('convolution 2',conv)
    #drop out:
    
    d = pooling(conv)
    cv2.imshow('doup out pooling',d)

    conv3 = cv2.filter2D(d, -1, gaussian_kernel, borderType = cv2.BORDER_CONSTANT)
    cv2.imshow('convolution 2',conv3)
    
    dd = drop_out(conv3)
    cv2.imshow('droup ',conv3)
    #output/showing
    cv2.waitkey()
    cv2.destruAllwindow()
    
#...............output.................#

#output/main function:    
if __name__ == "__main__":
    
    main()
                          
input()                            
