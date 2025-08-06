import cv2 as cv

#Insert the correct image path to be analyzed by the face detection filters.
#@testing...
picture = "Image/PATH"

img = cv.imread(picture)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
filter = cv.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')
result = filter.detectMultiScale(img_gray, minNeighbors=5, minSize =(20,20))

for (x, y, w, h) in result:
    print(f'Picture: {picture} x: {x} y: {y} Width: {w} Height: {h}')
    cv.rectangle(img, (x, y),(x + w, y + h),(0, 255, 0), 5)

cv.imshow('img', img)
cv.waitKey()