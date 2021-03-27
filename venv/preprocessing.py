import cv2
import numpy as np

def camera_sees():

    path1 = r"C:\Users\DELL\PycharmProjects\research\venv\1.jpg"
    path2 = r"C:\Users\DELL\PycharmProjects\research\venv\2.jpg"

    left = cv2.imread(path1)
    right = cv2.imread(path2)
    # right = cv2.flip(left, 1)

    left = cv2.resize(left, (0, 0), fx=0.2, fy=0.2)
    right = cv2.resize(right, (0, 0), fx=0.2, fy=0.2)

    left = cv2.blur(left, (3, 3))
    right = cv2.blur(right, (3, 3))


    left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

    kernel = np.array([[-1,-1,-1],
                       [-1,10,-1],
                       [-1,-1,-1]])
    left = cv2.filter2D(left, -1, kernel)
    right = cv2.filter2D(right, -1, kernel)

    return left, right
