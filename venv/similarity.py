
import  math
import cv2
import numpy as np
from PIL import Image as im
from convexhull import *


def similarity(img1, img2):
    orb = cv2.ORB_create(nfeatures=10000000, scoreType=cv2.ORB_FAST_SCORE)

    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)

    ### Plotting the detected features
    # for i in kp_a:
    #     point = tuple(np.array(i.pt).astype(int))
    #     img1 = cv2.circle(img1, point, color=(255, 0, 0), thickness=2, radius=1)
    # cv2.imshow("LEft", img1)
    # cv2.waitKey(0)

    #### Bruteforce matching
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    allMatches = bf.match(desc_a, desc_b)
    matches = []
    matched_points = []
    left_matches = []
    for match in allMatches:
        if abs(kp_a[match.queryIdx].pt[1] - kp_b[match.trainIdx].pt[1]) < 3:
            matches.append((match))            #Incase we output the image with similarities
            matched_points.append([kp_a[match.queryIdx].pt, kp_b[match.trainIdx].pt])
            left_matches.append(tuple(np.array(kp_a[match.queryIdx].pt).astype(int)))
            img1 = cv2.circle(img1, tuple(np.array(kp_a[match.queryIdx].pt).astype(int)), color=(255, 0, 0), thickness=2, radius=1)
    print("Match by bf: ", len(matched_points))

    # hull = convexHull(left_matches, len(left_matches))

    # for i in hull:
    #     cv2.circle(img1, i, radius= 5, color = (0, 0, 0), thickness= 4)


    # result = cv2.drawMatches(img1, kp_a, img2, kp_b, matches, None)
    # cv2.imshow("bf", result)
    # cv2.imshow("left", img1)
    # cv2.imshow("right", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return matched_points

    ### FLan based matcher

    # index_param = dict(algorithm = 0, trees = 5)
    # search_param = dict()
    # flann = cv2.FlannBasedMatcher(index_param, search_param)
    # allFlannMatches = flann.knnMatch(np.asarray(desc_a,np.float32),np.asarray(desc_b,np.float32), 2)
    # print(len(allFlannMatches))
    # good_points = []
    # matches = []
    # for m, n in allFlannMatches:
    #     if abs(kp_a[m.queryIdx].pt[1] - kp_b[n.trainIdx].pt[1]) < 3:
    #         print([kp_a[m.queryIdx].pt, kp_b[n.trainIdx].pt])
    #         matches.append((m))            #Incase we output the image with similarities
    #         good_points.append([kp_a[m.queryIdx].pt, kp_b[n.trainIdx].pt])
    # print("Match by flann: ", len(good_points))
    #
    # result = cv2.drawMatches(img1, kp_a, img2, kp_b, matches, None)
    # cv2.imshow("Lenn", result)

    # cv2.imshow("left", img1)
    # cv2.imshow("right", img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # return good_points

#
# def update(leftimg, right, width, height):
#
#     left = leftimg[0]
#     leftequivalent = leftimg[1]
#     confidence = leftimg[2]
#
#     for pad in range(1, 10):
#         for i in range(pad, height-pad, 2):
#             print(round(i / height * 100, 2), "% completed")
#             for j in range(pad, width-pad, 2):
#                 ft = right[i-pad: i+pad+1, j-pad:j+pad+1]
#                 small = math.inf
#                 index = -1
#
#                 for k in range(j, width- pad, 2):
#                     leftcut = left[i-pad: i+pad+1, k-pad:k+pad+1]
#                     difference = math.fabs((ft-leftcut).sum())
#                     if difference<small:
#                         small = difference
#                         index = k
#
#             if confidence[i][j]>small:
#                 leftequivalent[i][j] = index - j
#                 confidence[i][j] = small
#
#         img = im.fromarray(leftequivalent)
#         img.show()
#
#     op = np.array([left, leftequivalent, confidence])
#     return op
#
#
# def test(left, right):
#
#     width = np.shape(left)[1]
#     height = np.shape(left)[0]
#
#     leftequivalent = np.zeros([height, width])
#     confidence = np.zeros([height, width])
#
#     left = np.array([left, leftequivalent, confidence])
#     left = update(left, right, width, height)
#
#
# def convolute(left, right):
#     leftX = cv2.filter2D(left, -1, sobelX)
#     rightX = cv2.filter2D(right, -1, sobelX)
#
#     cv2.imshow("Left", leftX)
#     cv2.imshow("Right", rightX)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     test(leftX, rightX)
