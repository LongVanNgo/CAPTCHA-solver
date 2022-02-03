import numpy as np
from PIL import Image
import cv2
import os


IMG_DIR = r'C:\Users\Long\OneDrive - Danmarks Tekniske Universitet\02461 Introduction to intelligents systems\Exam project - Are you a robot\FinalFolder\dataset\segmented_test_data'
writedir = r'C:\Users\Long\OneDrive - Danmarks Tekniske Universitet\02461 Introduction to intelligents systems\Exam project - Are you a robot\FinalFolder\dataset\test_resize_test'
for img in os.listdir(IMG_DIR):
    img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)

    img_pil = Image.fromarray(img_array)
    img_28x28 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))
    #print(img_array)
    #img_array = (img_28x28.flatten())
    #print(img_array)
    #img_array  = img_array.reshape(-1,1).T
    ##img_array = np.array_split(img_array,27)
    #img_array = np.matrix(np.array_split(img_array, 27))
    im = Image.fromarray(img_28x28)
    im.save(writedir + '\\' + img)
    #print(np.size(img_array))
    #cv2.imwrite(writedir + '\\' + img,img_array)
    #print(img_array)

    #with open('train.csv', 'ab') as f:
#
    #    np.savetxt(f, img_array, delimiter=",")