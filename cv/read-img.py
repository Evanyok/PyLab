import cv2
import numpy
import os.path as path


BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

if path.exists(path.join(BASE_DIR, 'cv/resources/sample000.jpeg')):
    img = cv2.imread(path.join(BASE_DIR, 'cv/resources/sample000.jpeg'), 1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('File not found: %s' % path.join(BASE_DIR, 'cv/resources/sample000.jpeg'))