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

if __name__ == "__main__" :
    distance_btw_eyes = 2 #cms
    angle_of_view = [80, 40]
    start = time.time()

    left, right = camera_sees()
    matched_points = similarity(left, right)
    pix_with_dist, dist_image = findDistance(matched_points, np.shape(left), distance_btw_eyes, angle_of_view)
    print(time.time() - start)
    Window(left, dist_image)
    # plotDist(pix_with_dist)


