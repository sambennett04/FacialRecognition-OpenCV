# FacialRecognition-OpenCV

## Overview

- This is a piece of software where you can take a picture of your self and recognize yourself based on a name.
- This software is made up of 2 files that act in tandom.
- The first file, faceRecog.py, captures a photo of a face and labels it.
- The second file, faceCompare.py, compares a video stream from your computer camera to any stored facial images contained in the Faces folder and attempts to label the faces found on the video stream.

Adapted from: https://python.plainenglish.io/make-a-basic-face-detection-algorithm-in-python-using-opencv-and-haar-cascades-9571b3600383

## Requirements

1. numpy

```

pip install numpy

```

2. cv2

```

pip install opencv-python

```

3. os (built-in)

4. platform (built-in)

## Step 1 - Take a Screenshot of Your Face

Run the file ```faceRecog.py``` using the command below. Once you see the window dispaying a green box around your face press the ```p``` key to capture the face in the green box. Take multiple pictures of your face to train the software to recognize your face at different angles. All picture names must be unique, so if you took a picture and named it "Bob" the next picture of the same subject should be "Bob0", "Bob1", "Bob2", etc... The Name display code removes all numbers from the name of the face image when it is displayed on the screen. 

```py

python3 faceRecog.py

```

## Step 2 - Recognize your face

Run the file ```faceCompare.py``` using the command below. A video feed should appear showing the output of your computers camera. A green box should appear around your face and your name should appear above that green box. 

```py

python3 faceCompare.py

```

