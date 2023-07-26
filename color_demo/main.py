import cv2
import numpy as np

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW) #webcamdan görüntü okumak

while True:
    ret, frame = cap.read()  #görüntüyü okur doğru frame için ret, true döndürür
    frame = cv2.flip(frame, 1) #görüntünün y eksenine göre yansıması (ayna)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #hsv renk uzayı

    #green için
    lower_green = np.array([45, 100, 50]) #green üst ton hsv formatında
    upper_green = np.array([75, 255, 255]) #green alt ton hsv formatında
    green_mask= cv2.inRange(hsv_frame, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)

    #blue için
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

    #frameleri görmek için;
    cv2.imshow("Webcam", frame)
    cv2.imshow("Green", green)
    cv2.imshow("Blue", blue)
    if cv2.waitKey(1) & 0xFF == ord("q"):  #her frame 1ms kalır ve q ya basınca çıkar
        break

cap.release()
cv2.destroyAllWindows()