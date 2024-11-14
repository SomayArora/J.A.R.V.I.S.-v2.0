import cv2
from deepface import DeepFace
import os


# Function to recognize the face
def recognize_face(image_path, reference_image_path="face.jpg"):
    if not os.path.exists(reference_image_path):
        raise FileNotFoundError(f"Reference image '{reference_image_path}' not found.")

    result = DeepFace.verify(img1_path=image_path, img2_path=reference_image_path)

    if result['verified']:
        print("Welcome back!")
        return True
    else:
        print("Face not recognized")
        return False


# Open the webcam and start detecting faces
def detect_and_recognize():
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    recognized = False
    while not recognized:
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            # If a face is detected, save the image and attempt recognition
            img_path = 'captured_face.jpg'
            cv2.imwrite(img_path, frame)
            print(f"Face detected and saved as {img_path}")

            # Try to recognize the face
            recognized = recognize_face(img_path)

            if recognized:
                break  # Exit the loop if the face is recognized

        # Display the frame (optional, can be removed if not needed)
        cv2.imshow('Detecting face...', frame)

        # Exit if 'q' is pressed (optional)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Start the face detection and recognition process
detect_and_recognize()
