import numpy as np
import cv2
import os
import platform

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('imgA', cv2.resize(imageA, (250, 250)))
    #cv2.imshow('imgB', cv2.resize(imageB, (250, 250)))
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

path = 'Faces'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# On more recent MacOS devices the camera is external
# On windows the camera is considered to be built-in
# 0 for built-in, 1 for external
DEVICE_SETTING = 0 if platform.platform().lower().startswith("windows") else 1
video = cv2.VideoCapture(DEVICE_SETTING)

while True:
    key = cv2.waitKey(1)    # getting the key press
    check, screen = video.read()    # creating the screen (reading it from the webcam)
    face_rects = face_cascade.detectMultiScale(screen, scaleFactor=1.1, minNeighbors=5)
    # list of rects that correspond to the face

    faces = []
    for x, y, w, h in face_rects:
        frame = cv2.rectangle(screen, (x, y), (x+w, y+h), (0, 255, 0), 3)   # make rectangle
        face = cv2.resize(screen[y:y + h, x:x + w], (100, 100))  # create face img
        faces.append(face)  # save to list


    baseFaces = os.listdir('Faces')
    for i in range(len(faces)):
        lowestMSE = 200000
        testMSE = 0
        closest_index = 0
        for k in range(len(baseFaces)):
            testMSE = mse(faces[i], cv2.imread(os.path.join(path, baseFaces[k])))
            #print(baseFaces[k], testMSE)
            if testMSE < lowestMSE:
                lowestMSE = testMSE
                closest_index = k

        matchName = baseFaces[closest_index]
        matchName = matchName.removesuffix(".png")
        matchName = ''.join([c for c in matchName if not c.isdigit()])

        cv2.putText(screen, matchName, (face_rects[i][0], face_rects[i][1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 10, (255, 255, 255))

    cv2.imshow('Sam\'s and Hudson\'s super cool Face Detector', screen)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video.release()