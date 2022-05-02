import cv2 as cv
from cv2 import CascadeClassifier
import numpy
import os
from os import listdir

rootdir = "."
for subdir, dirs, files in os.walk(rootdir):

        for images in files:

        #define image
                if (images.endswith(".jpg")):
                        img = cv.imread(os.path.join(subdir,images))
                
                #grayscale for detection
                        grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                
                #trained data - https://github.com/opencv/opencv/tree/master/data/haarcascades
                        plateSetting = cv.CascadeClassifier('Trained_plate2.xml')
                
                #find license plates
                        plates = plateSetting.detectMultiScale(grayscale_img)
                
                #mark license plates
                        for(x,y,w,h) in plates:

                                cv.rectangle(img,(x,y),(x+w,y+h),[0,255,0],2)
                        #save marked images
                        cv.imwrite("marked_"+ images,img)


        



#cv.imshow('test',img)



#cv.waitKey()
