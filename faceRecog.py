import cv2
import platform

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
    
    if screen is None:
        raise Exception("screen was not initialized")

    face_rects = face_cascade.detectMultiScale(screen, scaleFactor=1.1, minNeighbors=5)
    # list of rects that correspond to the face

    baseFaces = []
    for x, y, w, h in face_rects:
        frame = cv2.rectangle(screen, (x, y), (x+w, y+h), (0, 255, 0), 3)   # make rectangle
        face = cv2.resize(screen[y:y + h, x:x + w], (100, 100))  # create face img
        baseFaces.append(face)  # save to list

    if key == ord('p'):
        for i in range(len(baseFaces)):  # for every face
            print("photo taken")
            cv2.imshow(str(i), baseFaces[i])
            cv2.imwrite('% s/% s.png' % (path, input("Whose face is this? ")), baseFaces[i])  # save to Faces folder
            print("\nselect the python launcher and press P to take another photo or Q to quit.")

    cv2.imshow('Sam\'s and Hudson\'s super cool Face Detector', screen)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video.release()
quit()