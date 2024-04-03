# Import OpenCV
import cv2
import matplotlib.pyplot as plt

# Create detector
face_detector = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# Video capture
video_capture = cv2.VideoCapture(0)
''' 0 denotes own webcam, 1 indicates some other webcam'''


# Capture frame-by-frame
while True:
    ret, frame = video_capture.read()
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = face_detector.detectMultiScale(image_gray)

    # Draw rectangle around the faces
    for (x, y, w, h) in detections:
        print(w,h)
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done release the capture
video_capture.release()
cv2.destroyAllWindows()