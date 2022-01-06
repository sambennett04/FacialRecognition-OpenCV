import cv2
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
        faces.append(face)  # save to list

    if key == ord('p'):
        for i in range(len(faces)):  # for every face
            print("photo taken")
            cv2.imwrite('% s/% s.png' % (path, i), faces[i])    # save to Faces folder

    cv2.imshow('Sam\'s and Hudson\'s super cool Face Detector', screen)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video.release()