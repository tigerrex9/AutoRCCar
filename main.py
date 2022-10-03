import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import sklearn

from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import optimizers

from keras import backend as K

#Image properties
height, width, depth = 320, 240, 3

#Template for image
image = np.zeros((height,width,depth))
normalized_image = np.divide(image, 255)
flattened_image = np.reshape(normalized_image, [-1,np.product(normalized_image.shape)])

print(image.shape)
print(normalized_image.shape)
print(flattened_image.shape)

def make_model(image_resolution, informational_neurons, outputs)
    image_data = keras.Input(shape=(image_resolution), name="image_data")
    information = keras.Input(shape=(informational_neurons), name="information")

    #input image_data into cnn

    #input information and flattened image_data layer into dense layer

    #get output
