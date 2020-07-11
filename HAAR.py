import os
import random
import sys, subprocess
import cv2
import shutil
import numpy as np

pic_num = 1

while pic_num<3001:
    path2="/home/olsze16/PycharmProjects/HAARclasifier/venv/101_ObjectCategories"
    paths=os.listdir(path2)
    path=random.choice(paths)
    files=os.listdir("/home/olsze16/PycharmProjects/HAARclasifier/venv/101_ObjectCategories/" + str(path))
    d=random.choice(files)
    os. chdir("/home/olsze16/PycharmProjects/HAARclasifier/venv/101_ObjectCategories/BACKGROUND_Google")
    image=cv2.imread(d,cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("issue with image")
    else:
        height, width = image.shape
        if height<1300:
            resized_image = cv2.resize(image, (150, 150))
            cv2.imshow('kondzik',resized_image)
            os. chdir("/home/olsze16/PycharmProjects/HAARclasifier/venv/negative")
            cv2.imwrite("image" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1
            cv2.waitKey(1)
        else:
            print("issue")
print("proces zakonczony")

