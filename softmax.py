#-*-coding:utf-8-*-
#Nutures
#2018/5/29
#softmax
import tensorflow
import keras
from keras.models import Sequential
from keras.utils.vis_utils import plot_model
from keras.layers import Dense , Dropout, Activation
from keras.optimizers import SGD
# 生成数据
#Generate dummy data
import numpy as np
#x_train = np.random.random((1000, 20))
#print x_train.shape
#y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000,1)), num_classes=40)
#y_train = np.random.random((50, 20))
#print len(y_train)
#print y_train

#y_test = keras.utils.to_categorical(np.random.randint(10, size=(100,1)), num_classes=40)
data = np.loadtxt('../structure/1/fock.dat')
x_train = np.random.random((100, 10))
print x_train
y_train = data[0:1000].reshape(-1, 10)
x_test = np.random.random((10, 10))
y_test = data[1000:1100].reshape(-1, 10)
print y_train.shape, x_train.shape, y_test.shape, x_test.shape

#print len(k)
model = Sequential()

model.add(Dense(64, activation='relu', input_dim=10))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
model.compile(loss = 'categorical_crossentropy',
              optimizer = sgd ,
              metrics = ['accuracy'])
model.fit(x_train, y_train,
          epochs = 20,
          batch_size= 128)
plot_model(model, to_file = 'model.png', show_shapes = True)
#Image('model.png')
score = model.evaluate(x_test, y_test, batch_size= 128)
print score