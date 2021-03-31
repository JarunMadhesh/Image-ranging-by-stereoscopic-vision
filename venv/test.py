import math
import cv2
import os
import numpy as np
import time
import math
import matplotlib.pyplot as plt
from PIL import Image as im
from PIL import  ImageTk
from tkinter import *

from filters import *
from finddistance import *
from similarity import *
from preprocessing import *
from gui import *

def chumma(imgs):

    for img in imgs:
        img = cv2.pyrDown(img)

        ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)
        contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            # find bounding box coordinates
            x,y,w,h = cv2.boundingRect(c)
            hull = cv2.convexHull(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("contours", img)
            cv2.waitKey(0)

        # find minimum area
        rect = cv2.minAreaRect(c)
        # calculate coordinates of the minimum area rectangle
        box = cv2.boxPoints(rect)
        # normalize coordinates to integers
        box = np.int0(box)
        # draw contours
        cv2.drawContours(img, [box], 0, (0,0, 255), 3)
        # calculate center and radius of minimum enclosing circle
        (x,y),radius = cv2.minEnclosingCircle(c)
        # cast to integers
        center = (int(x),int(y))
        radius = int(radius)
        # draw the circle
        img = cv2.circle(img,center,radius,(0,255,0),2)

        cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
        cv2.imshow(str(img), img)
    cv2.waitKey(0)


if __name__ == "__main__" :
    distance_btw_eyes = 2 #cms
    angle_of_view = [80, 40]
    start = time.time()

    left, right = camera_sees()
    # chumma([left, right])
    matched_points = similarity(left, right)
    pix_with_dist, dist_image = findDistance(matched_points, np.shape(left), distance_btw_eyes, angle_of_view)

    print(time.time() - start)
    Window(left, dist_image)
    # plotDist(pix_with_dist)