import cv2
import time
from playsound import playsound  # Only import once

# Load Haar cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# Start webcam
cap = cv2.VideoCapture(0)

a = 0  # No-eyes counter
b = 0  # Eyes-detected counter
c = time.time()  # Timer for 15-second checks

def play_alert():
    try:
        playsound(r'C:\Users\Anuj mishra\Downloads\Project\Pictures\Desktop\sleep_detector\buzz.mp3')
    except Exception as e:
        print("Error playing sound:", e)

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        print("No face detected")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if (time.time() - c) >= 10:
            if (a + b) > 0 and (a / (a + b)) >= 0.2:
                play_alert()
                print("****ALERT*****", a, b, a / (a + b))
            else:
                print("Safe:", a / (a + b) if (a + b) > 0 else "N/A")
            c = time.time()
            a = 0
            b = 0

        if len(eyes) == 0:
            a += 1
            print("No eyes detected!")
        else:
            b += 1
            print("Eyes detected!")

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Sleep Detector', img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to stop
        print("No-eyes frames:", a)
        print("Total frames:", a + b)
        break

cap.release()
cv2.destroyAllWindows()
