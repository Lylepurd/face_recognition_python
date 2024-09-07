# import cv2
# import face_recognition
# import os

# # Ensure the "images" folder exists
# if not os.path.exists('images'):
#     os.makedirs('images')

# # Load known face encodings and names
# known_face_encodings = []
# known_face_names = []

# # Function to load faces from the "images" folder
# def load_known_faces():
#     for filename in os.listdir('images'):
#         if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
#             image_path = os.path.join('images', filename)
#             image = face_recognition.load_image_file(image_path)
#             encoding = face_recognition.face_encodings(image)[0]
#             known_face_encodings.append(encoding)
#             known_face_names.append(os.path.splitext(filename)[0])  # Use the filename without extension as the name

# # Load faces initially
# load_known_faces()

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# # Frame counter for saved images
# image_counter = 1

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     if not ret:
#         print("Failed to grab frame")
#         break

#     # Find all face locations in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Loop through each face found in the frame
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Check if the face matches any known faces
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = 'Unknown'

#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#         # Draw a box around the face and label with the name
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

#     # Display the resulting frame
#     cv2.imshow('video', frame)

#     # Save photo when 'c' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('c'):
#         # Save the image to the "images" folder
#         image_path = f"images/person_{image_counter}.jpeg"
#         cv2.imwrite(image_path, frame)
#         print(f"Captured and saved {image_path}")

#         # After saving, reload the faces to include the new one
#         load_known_faces()

#         # Increment the image counter
#         image_counter += 1

#     # Break the loop when the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close OpenCV windows
# video_capture.release()
# cv2.destroyAllWindows()



import cv2
import face_recognition
import os

# Ensure the "images" folder exists
if not os.path.exists('images'):
    os.makedirs('images')

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Function to load faces from the "images" folder
def load_known_faces():
    global known_face_encodings, known_face_names
    known_face_encodings = []
    known_face_names = []
    for filename in os.listdir('images'):
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join('images', filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])  # Use the filename without extension as the name

# Load faces initially
load_known_faces()

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Frame counter for saved images
image_counter = 1

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = 'Unknown'

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('video', frame)

    # Save photo when 'c' is pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Prompt for the name of the person
        name = input("Enter the name of the person: ").strip()
        if not name:
            name = f"person_{image_counter}"

        # Save the image to the "images" folder
        image_path = f"images/{name}.jpeg"
        cv2.imwrite(image_path, frame)
        print(f"Captured and saved {image_path}")

        # After saving, reload the faces to include the new one
        load_known_faces()

        # Increment the image counter
        image_counter += 1

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
