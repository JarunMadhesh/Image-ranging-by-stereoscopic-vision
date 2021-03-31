import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plotDist(pix_with_dist):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    for i in pix_with_dist:
        ax.scatter(i[0], i[1], i[2], c = "r", marker = "o")
    plt.show()

def findDistofPix(x, y, dist_image):
    i = 1
    dist_image = dist_image.astype(int)
    while True:
        if np.count_nonzero(dist_image[x-i:x+i,y-i:y+i]) > 5:
            break
        i+=1
        if i>min(np.shape(dist_image)[0], np.shape(dist_image)[1]):
            break
    lt = []
    pt = dist_image[x - i:x + i, y - i:y + i]
    for p in pt:
        for j in p:
            if(j!=0):
                lt.append(j)
    print("lt = ", lt)
    if len(lt)>3:
        lt.pop(lt.index(max(lt)))
        lt.pop((lt.index(min(lt))))
    if len(lt)>0:
        distance = np.mean(lt)
    else:
        distance = -1
    return distance


def findDistance(matched_points, imgShape, base, view):
    pixPerDeg = calculate_degPerPix(view=view, imageSize=imgShape)

    imgCenter = tuple(np.divide(imgShape, 2).astype(int))

    pix_with_dist = []
    dist_img = np.zeros(imgShape)

    for point in matched_points:
        leftObj = point[0]
        rightObj = point[1]
        # print(calculate_degrees(leftObj, imgCenter, degPerPix), )
        distance = find_distance(90-calculate_degrees(leftObj, imgCenter, pixPerDeg)[0], 90-calculate_degrees(rightObj, imgCenter, pixPerDeg)[0], base)
        pix_with_dist.append([leftObj[0], leftObj[1], distance])
        dist_img[int(leftObj[1])][int(leftObj[0])] = int(distance)

    # img = im.fromarray(dist_img, 'RGB')
    # img.show()
    return pix_with_dist, dist_img

def find_distance(deg1, deg2, base):
    deg1 = math.radians(deg1)
    deg2 = math.radians(deg2)

    if(deg1<deg2):
        temp = deg2
        deg2 = deg1
        deg1 = temp
    # Let deg1 always have higher degree so degree 2 will
    # be that of the camera farther
    dist = 0
    temp = (math.tan(deg1) - math.tan(deg2))
    if(temp>0):
        dist = (base * math.tan(deg1) * math.tan(deg2)) / temp

    return dist

def calculate_degPerPix(view, imageSize):
    imageSize = imageSize[::-1]
    return tuple((imageSize[0]/view[0], imageSize[1]/view[1]))

def calculate_degrees(point, center, pixPerDeg):
    # print(center, image, degPerPix)
    degrees =  (point[0]-center[0]) / pixPerDeg[0], (point[1]- center[1]) / pixPerDeg[1]
    return degrees

