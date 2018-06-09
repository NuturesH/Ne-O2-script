#-*-coding:UTF-8-*-
#Nutures
#2018/5/29

import tensorflow
import numpy as np
import keras
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation

#model = Sequential([Dense(32, units=784),
                    #Activation('relu'), Dense(10), Activation('softmax'),])
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax', units= 10))

# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
date = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))
# wg = model.
# print wg
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)


def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

