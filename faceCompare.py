import numpy as np
import cv2
import os

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

path = 'Faces'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)     # 0 for built-in, 1 for external

while True:
    key = cv2.waitKey(1)    # getting the key press
    check, screen = video.read()    # creating the screen (reading it from the webcam)
    face_rects = face_cascade.detectMultiScale(screen, scaleFactor=1.1, minNeighbors=5)
    # list of rects that correspond to the face

    faces = []
    for x, y, w, h in face_rects:
        frame = cv2.rectangle(screen, (x, y), (x+w, y+h), (0, 255, 0), 3)   # make rectangle
        face = screen[y:y + h, x:x + w]  # create face img
        faces.append(cv2.cvtColor(face, cv2.COLOR_BGR2GRAY))  # save to list

    if key == ord('p'):
        list = os.listdir('Faces')
        for i in range(len(faces)):  # for every face]
            print("photo taken")
            for k in range(len(list)):
                cv2.imshow("yoo", cv2.imread(list[k],0))
                if mse(faces[i],cv2.imread(list[k])) <= 500:
                    print(list[k])



    cv2.imshow('Sam\'s and Hudson\'s super cool Face Detector', screen)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video.release()


