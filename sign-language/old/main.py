from cv2 import cv2
import numpy as np
import tensorflow as tf
import os
import pyttsx3

# engine = pyttsx3.init()


# load saved model from PC
model = tf.keras.models.load_model(
    r'/smnist.h5')
model.summary()
data_dir = '../dataset'
# getting the labels form data directory
labels = sorted(os.listdir(data_dir))
labels[-1] = 'Nothing'
print(labels)

# initiating the video source, 0 for internal camera
cap = cv2.VideoCapture(0)
while (True):

    _, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5)
    # region of intrest
    roi = frame[100:300, 100:300]
    img = cv2.resize(roi, (28, 28))
    cv2.imshow('roi', roi)
    img = img / 255
    # img.reshape(1, 50, 50, 3)
    # make predication about the current frame
    prediction = model.predict(img.reshape(1, 28, 28, 1))
    char_index = np.argmax(prediction)
    print(char_index,prediction[0,char_index]*100)

    confidence = round(prediction[0, char_index] * 100, 1)
    predicted_char = labels[char_index]
    print(predicted_char)
    # Initialize the engine
    # engine = pyttsx3.init()
    # engine.say(predicted_char)
    # engine.runAndWait()

    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    color = (0, 255, 255)
    thickness = 2

    # writing the predicted char and its confidence percentage to the frame
    msg = predicted_char + ', Conf: ' + str(confidence) + ' %'
    cv2.putText(frame, msg, (80, 80), font, fontScale, color, thickness)

    cv2.imshow('frame', frame)

    # close the camera when press 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

# import cv2
#
# # define a video capture object
# vid = cv2.VideoCapture(0)
#
# while (True):
#
#     # Capture the video frame
#     # by frame
#     _, frame = vid.read()
#     cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5)
#         # region of intrest
#     roi = frame[100:300, 100:300]
#     img = cv2.resize(roi, (50, 50))
#     cv2.imshow('roi', roi)
#
#     img = img / 255
#
#
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#
#     img.reshape(1, 50, 50, 3)
#
#     font = cv2.FONT_HERSHEY_TRIPLEX
#     fontScale = 1
#     color = (0, 255, 255)
#     thickness = 2
#
#     # writing the predicted char and its confidence percentage to the frame
#     msg = 'Y' + ', Conf: ' + str(90) + ' %'
#     cv2.putText(frame, msg, (80, 80), font, fontScale, color, thickness)
#
#     cv2.imshow('frame', frame)
#
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()