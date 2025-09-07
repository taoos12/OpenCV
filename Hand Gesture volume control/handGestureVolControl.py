import cv2 as cv
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0
capture = cv.VideoCapture(0)
drawing_utils = mp.solutions.drawing_utils

my_hands = mp.solutions.hands.Hands()
while True:
    isTrue, frame = capture.read()
    
    frame_height, frame_width, _= frame.shape
    
    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    output = my_hands.process(rgb_img)
    
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            
            landmarks = hand.landmark
            
            for id, landmark in enumerate(landmarks):
                # 8 == forefinger   
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv.circle(img= frame, center= (x, y), radius= 8, color= (0, 0, 255), thickness= 3)
                    x1 = x
                    y1 = y

                # thumb
                if id == 4:
                    cv.circle(img= frame, center= (x, y), radius= 8, color= (0, 255, 0), thickness= 3)
                    x2 = x
                    y2 = y
        dist = (((x2 - x1) ** 2 )+ ((y2 - y1) ** 2))**(0.5) // 4
        cv.line(frame, (x1, y1), (x2, y2), (100, 250, 255), 5)

        if dist > 25:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    if not isTrue:
        break
    frame =cv.flip(frame, 1)
    cv.imshow("Camera", frame)
    
    key = cv.waitKey(20)
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()