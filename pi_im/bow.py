import argparse as ap
import cv2

import os

from sklearn.externals import joblib
from sklearn import preprocessing
from scipy.cluster.vq import *

import math
import numpy as np

from pylab import *
from PIL import Image

# App imports
from pi_im.models import ReferenceImg, ResourceAnalyse, AnalyseResults
from image_srv import settings

def indexing():
    # Get the training classes names and store them in a list
    train_path = settings.PI_IM_RESOURCES_DIR

    training_names = os.listdir(train_path)

    numWords = 1000

    # Get all the path to the images and save them in a list
    # image_paths and the corresponding label in image_paths
    image_paths = []
    for training_name in training_names:
        image_path = os.path.join(train_path, training_name)
        image_paths += [image_path]

    # Create feature extraction and keypoint detector objects
    # fea_det = cv2.FeatureDetector_create("SIFT")
    # des_ext = cv2.DescriptorExtractor_create("SIFT")

    # List where all the descriptors are stored
    des_list = []
    sift = cv2.xfeatures2d.SIFT_create()

    for i, image_path in enumerate(image_paths):
        im = cv2.imread(image_path)
        print("Extract SIFT of %s image, %d of %d images" % (training_names[i], i, len(image_paths)))
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        kp, des = sift.detectAndCompute(gray, None)
        des_list.append((image_path, des))

    # Stack all the descriptors vertically in a numpy array
    # downsampling = 1
    # descriptors = des_list[0][1][::downsampling,:]
    # for image_path, descriptor in des_list[1:]:
    #    descriptors = np.vstack((descriptors, descriptor[::downsampling,:]))

    # Stack all the descriptors vertically in a numpy array
    descriptors = des_list[0][1]
    for image_path, descriptor in des_list[1:]:
        descriptors = np.vstack((descriptors, descriptor))

    # Perform k-means clustering
    print("Start k-means: %d words, %d key points" % (numWords, descriptors.shape[0]))
    voc, variance = kmeans(descriptors, numWords, 1)

    # Calculate the histogram of features
    im_features = np.zeros((len(image_paths), numWords), "float32")
    for i in range(len(image_paths)):
        words, distance = vq(des_list[i][1], voc)
        for w in words:
            im_features[i][w] += 1

    # Perform Tf-Idf vectorization
    nbr_occurences = np.sum((im_features > 0) * 1, axis=0)
    idf = np.array(np.log((1.0 * len(image_paths) + 1) / (1.0 * nbr_occurences + 1)), 'float32')

    # Perform L2 normalization
    im_features = im_features * idf
    im_features = preprocessing.normalize(im_features, norm='l2')

    joblib.dump((im_features, image_paths, training_names, idf, numWords, voc), "bof_retr.pkl", compress=3)

    return "Indexed: k-means: %d words, %d key points" % (numWords, descriptors.shape[0])


def research(image_path, nb_results):
    print(image_path)

    # Load the classifier, class names, scaler, number of clusters and vocabulary
    im_features, image_paths, image_names, idf, numWords, voc = joblib.load("bof_retr.pkl")

    # Create feature extraction and keypoint detector objects
    # List where all the descriptors are stored
    des_list = []
    sift = cv2.xfeatures2d.SIFT_create()


    im = cv2.imread(image_path)

    old_size = im.shape[:2]  # old_size is in (height, width) format

    ratio = float(800) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])
    # new_size should be in (width, height) format
    im = cv2.resize(im, (new_size[1], new_size[0]))

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(im, None)

    des_list.append((image_path, des))

    # Stack all the descriptors vertically in a numpy array
    descriptors = des_list[0][1]

    #
    test_features = np.zeros((1, numWords), "float32")
    words, distance = vq(descriptors, voc)
    for w in words:
        test_features[0][w] += 1

    # Perform Tf-Idf vectorization and L2 normalization
    test_features = test_features * idf
    test_features = preprocessing.normalize(test_features, norm='l2')

    score = np.dot(test_features, im_features.T)
    rank_ID = np.argsort(-score)

    resource = ResourceAnalyse()
    resource.save()

    for i, ID in enumerate(rank_ID[0][0:nb_results]):
        img = ReferenceImg.objects.filter(img_name=image_names[ID])[0]
        result = AnalyseResults(image=img, score=score[0][ID])
        result.save()
        resource.results.add(result)
        resource.save()

    return resource.id

