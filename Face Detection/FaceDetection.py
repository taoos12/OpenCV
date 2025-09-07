import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    
    
    # Conversion of frames from BGR to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    
    # All the faces will get stored in the faces object
    faces = face_cascade.detectMultiScale(gray, 1.1, minNeighbors= 4)
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    frame = cv.flip(frame, 1)
    
    cv.imshow("Video", frame)

    # Storing the 20ms key press time in the key 
    key = cv.waitKey(20)
    
    # 27 = esc key
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()