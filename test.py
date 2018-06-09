#-*-coding:utf-8-*-
#Nutures
#2018/6/5

import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense , Dropout, Activation
from keras.optimizers import SGD
from keras.utils.vis_utils import plot_model

#read data
def read_data(X):
    data_list = []
    data_f = pd.read_csv(X, sep= ',')
    #data_list.append(data_f)
    #data = pd.read_csv(X, sep = ',')
    data = np.array(data_f)
    #zz = data.reshape(1,-1)[0]
    #print data , data.shape
    #print zz, len(zz), zz.shape
    return data

# input data format

#structure neural networks
def neural_networks(X):
    x_train = np.random.random((100,100))
    print x_train
    #print x_train.shape
    y_train = keras.utils.to_categorical(np.random.randint(1, size=(100, 1)), num_classes=1)
    y_train = keras.utils.to_categorical(y_train)
    print y_train
    #y_train = np.random.random((34, 1))
    #print y_train
    #y_train = [0.003]
    model = Sequential()
    print x_train.shape,y_train.shape
    model.add(Dense(34, activation='relu', input_dim=100))
    model.add(Dropout(0.5))
    model.add(Dense(20, activation='relu'))
    model.add(Dropout(0.8))
    model.add(Dense(2, activation='softmax'))
    plot_model(model, to_file='soft.png', show_shapes=True)
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])
    model.fit(x_train, y_train,
              epochs=5 , batch_size=128)


#read_data('/home/nutures/workspace/Ne-O2/structure/1/molematrix.csv')
neural_networks('/home/nutures/workspace/Ne-O2/structure/1/molematrix.csv')