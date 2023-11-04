# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow as tf
# import os
#
# from keras import Sequential
# from keras.layers import Conv2D, BatchNormalization, MaxPool2D, Dropout, Flatten, Dense
# # from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# import cv2
# import pydot
#
#
# # load_dataset function to load the data and resize the images to 50x50
# def load_dataset(directory):
#     images = []
#     labels = []
#     for idx, label in enumerate(uniq_labels):
#         for file in os.listdir(directory + '/' + label):
#             filepath = directory + '/' + label + "/" + file
#             img = cv2.resize(cv2.imread(filepath), (50, 50))
#             images.append(img)
#             labels.append(idx)
#     images = np.asarray(images)
#     labels = np.asarray(labels)
#     return images, labels
#
#
# # display_images function to show examples
# def display_images(x_data, y_data, title, display_label=True):
#     x, y = x_data, y_data
#     fig, axes = plt.subplots(5, 8, figsize=(18, 5))
#     fig.subplots_adjust(hspace=0.5, wspace=0.5)
#     fig.suptitle(title, fontsize=18)
#     for i, ax in enumerate(axes.flat):
#         ax.imshow(cv2.cvtColor(x[i], cv2.COLOR_BGR2RGB))
#         if display_label:
#             ax.set_xlabel(uniq_labels[y[i]])
#         ax.set_xticks([])
#         ax.set_yticks([])
#     plt.show()
#
#
# # loading_dataset into X_pre and Y_pre
# data_dir = r'/Users/george/PycharmProjects/sign-language/dataset'
# uniq_labels = sorted(os.listdir(data_dir))
# X_pre, Y_pre = load_dataset(data_dir)
# print(X_pre.shape, Y_pre.shape)
#
# # spliting dataset into 80% train, 10% validation and 10% test data
# X_train, X_test, Y_train, Y_test = train_test_split(X_pre, Y_pre, test_size=0.8)
# X_test, X_eval, Y_test, Y_eval = train_test_split(X_test, Y_test, test_size=0.5)
#
# print("Train images shape", X_train.shape, Y_train.shape)
# print("Test images shape", X_test.shape, Y_test.shape)
# print("Evaluate image shape", X_eval.shape, Y_eval.shape)
# print("Printing the labels", uniq_labels, len(uniq_labels))
#
# # converting Y_tes and Y_train to One hot vectors using to_categorical
# # example of one hot => '1' is represented as [0. 1. 0. . . . . 0.]
# Y_train = to_categorical(Y_train)
# Y_test = to_categorical(Y_test)
# Y_eval = to_categorical(Y_eval)
# X_train = X_train / 255.
# X_test = X_test / 255.
# X_eval = X_eval / 255.
#
# # building our model
#
# # model = tf.keras.Sequential([
# #     tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(50, 50, 3)),
# #     tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
# #     tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
# #     tf.keras.layers.MaxPool2D((2, 2)),
# #     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
# #     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
# #     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
# #     tf.keras.layers.MaxPool2D((2, 2)),
# #     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
# #     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
# #     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
# #     tf.keras.layers.Flatten(),
# #     tf.keras.layers.Dense(128, activation='relu'),
# #     tf.keras.layers.Dense(25, activation='softmax')
# # ])
#
# model = Sequential()
# model.add(BatchNormalization())
# model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
# model.add(Conv2D(50 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
# model.add(Dropout(0.2))
# model.add(BatchNormalization())
# model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
# model.add(Conv2D(25 , (3,3) , strides = 1 , padding = 'same' , activation = 'relu'))
# model.add(BatchNormalization())
# model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))
# model.add(Flatten())
# model.add(Dense(units = 512 , activation = 'relu'))
# model.add(Dropout(0.3))
# model.add(Dense(units = 24 , activation = 'softmax'))
#
# model.summary()
#
# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'], )
#
# history = model.fit(X_train, Y_train, epochs=20, verbose=1,
#                     validation_data=(X_eval, Y_eval))
#
# model.evaluate(X_test, Y_test)
#
# model.save(r'/Users/george/PycharmProjects/sign-language/new_model_40ep.h5')
#
# train_loss = history.history['loss']
# train_acc = history.history['accuracy']
# val_loss = history.history['val_loss']
# val_accuracy = history.history['val_accuracy']
#
# epochs = list(range(1, 41))
# plt.plot(epochs, train_loss, label="training loss")
# plt.plot(epochs, val_loss, label="validation  loss")
# plt.legend()
# plt.show()
#
# plt.plot(epochs, train_acc, label="training accuracy")
# plt.plot(epochs, val_accuracy, label="validation  accuracy")
# plt.legend()
# plt.show()
