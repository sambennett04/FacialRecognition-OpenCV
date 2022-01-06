#from skimage.metrics import structural_similarity as ssim;
#import matplotlib.pyplot as plt;
#import numpy as np
#import FaceConfiguration
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

#this is going to be the screen shot section

#def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    #err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    #err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    #return err

#def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	#m = mse(imageA, imageB)
	#s = ssim(imageA, imageB)
	# setup the figure
	#fig = plt.figure(title)
	#plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	#ax = fig.add_subplot(1, 2, 1)
	#plt.imshow(imageA, cmap = plt.cm.gray)
	#plt.axis("off")
	# show the second image
	#ax = fig.add_subplot(1, 2, 2)
	#plt.imshow(imageB, cmap = plt.cm.gray)
	#plt.axis("off")
	# show the images
	#plt.show()

