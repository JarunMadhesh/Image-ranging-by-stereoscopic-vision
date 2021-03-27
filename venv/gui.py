from PIL import Image as im
from PIL import  ImageTk
from tkinter import *
import numpy as np
import  cv2

from test import *

temp_dist = 0


class Window():

    def __init__(self, img, dist_image):
        self.root = Tk()
        self.shape = np.shape(img)
        self.text = StringVar()
        self.text.set("0")
        self.dist_image = dist_image

        self.l = Label(self.root, textvariable=self.text, font=("Courier", 22))
        self.l.grid(row=1, column=1)

        self.w2 = Scale(self.root, from_=0, to=self.shape[1], orient=HORIZONTAL, length=self.shape[1])
        self.w2.grid(row=1, column=0)

        self.w1 = Scale(self.root, from_=0, to=self.shape[0], length=self.shape[0])
        self.w1.grid(row=0, column=1)

        self.img = img
        self.editedimg = cv2.circle(self.img, (self.w1.get(), self.w2.get()), radius=2, color=(255, 0, 0), thickness=2)
        self.photo = ImageTk.PhotoImage(im.fromarray(self.editedimg))
        self.canvas = Canvas(self.root, width=self.shape[1], height=self.shape[0])
        self.canvas.grid(row=0, column=0)
        self.canvas.create_image(20, 20, anchor=NW, image=self.photo)

        Button(self.root, text='Find', command=self.update_dist).grid(row=2, column=1)

        self.root.mainloop()

    def update_dist(self):
        temp_dist = findDistofPix(self.w1.get(), self.w2.get(), self.dist_image)
        print(temp_dist)

        self.editedimg = cv2.circle(self.img, (self.w2.get(), self.w1.get()), radius=2, color=(255, 0, 0), thickness=2)
        self.photo = ImageTk.PhotoImage(im.fromarray(self.editedimg))
        self.canvas.create_image(20, 20, anchor=NW, image=self.photo)
        self.root.update()
        # print(temp_dist)