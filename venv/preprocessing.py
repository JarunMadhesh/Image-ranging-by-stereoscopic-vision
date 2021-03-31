import cv2
import numpy as np

def camera_sees():

    path1 = r"C:\Users\DELL\PycharmProjects\research\venv\assets\3_left.jpg"
    path2 = r"C:\Users\DELL\PycharmProjects\research\venv\assets\3_right.jpg"

    # path = r"C:\Users\DELL\PycharmProjects\research\venv\img.jpeg"
    #
    # left = cv2.imread(path)
    # right = left[0: np.shape(left)[0], int(np.shape(left)[1] * 0.5) : int(np.shape(left)[1])]
    # left = left[0: np.shape(left)[0], 0 : int(np.shape(left)[1] * 0.5)]
    right = cv2.imread(path2)
    left= cv2.imread(path1)
    # right = cv2.flip(left, 1)

    change = 350/ np.shape(left)[0]
    left = cv2.resize(left, (0, 0), fx=change, fy=change)
    right = cv2.resize(right, (0, 0), fx=change, fy=change)

    left = cv2.blur(left, (2, 2))
    right = cv2.blur(right, (2, 2))

    left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

    left[0:np.shape(left)[0], 0: int(np.shape(left)[1] * 0.1)] = 0
    right[0:np.shape(right)[0], int(np.shape(right)[1] * 0.9): np.shape(right)[1]] = 0

    kernel = np.array([[-1,-1,-1],
                       [-1, 9.5,-1],
                       [-1,-1,-1]])
    left = cv2.filter2D(left, -1, kernel)
    right = cv2.filter2D(right, -1, kernel)


    return left, right
