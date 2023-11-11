from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.image import resize
from keras.models import load_model
import numpy as np
import skimage
import cv2
import os
import re
PATH_FOLDER_PROJECT = r'C:\Users\misha\Desktop\python'

def img_preproces(img, expand_dims = False, copy = False, preprocess_img = False):
    if expand_dims == True:
        img = np.expand_dims(img, axis=0)
    if copy == True:
        img = np.copy(img)
    if preprocess_img == True:
        img = preprocess_input(img).astype("float32") / 255
    return img

def si_rescale(img):
    for_rescale = list(img.shape)
    for_rescale.sort()
    scale_rating = 32 / for_rescale[1]
    img = skimage.transform.rescale(skimage.transform.resize(img, (for_rescale[1], for_rescale[1])), scale_rating, multichannel=True)
    img = img_preproces(img, expand_dims = True)
    return img

def image_classify(filename, processor, model):
    img = skimage.io.imread(filename)
    img = si_rescale(img)
        
    features = model.predict(img)
    top = []
    top_num = 10
    classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    
    for request in range(1):  # num of foto or objects on foto
        classes_request = classes
        features_request = features[0]
        rang = 1
        for i in range(top_num):
            pred = np.argmax(features_request)
            top.append([rang, classes_request[pred], round(features_request[np.argmax(features_request)], 4)])
            features_request = np.delete(features_request, np.argmax(features_request))
            classes_request.remove(classes_request[pred])
            rang +=1
    return top


def get_photo_path():
    dir_path = r'C:\Users\misha\Desktop\python\team_1\media\images'
    list_files = os.listdir(dir_path)
    list_files
    files  = ''
    for filename in list_files:
        files = (re.sub(r'\\', r'/', dir_path + "/" + filename))
    return files


def model_loader(model_path):
    model = load_model(model_path[0])
    model.load_weights(model_path[1])
    return model