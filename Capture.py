import cv2
import numpy as np
import os

name = input("Enter name: ")
def capture_image(save_folder):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Captured Image', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):

            filename = os.path.join(save_folder, name+".jpg")
            cv2.imwrite(filename, frame)

            # Break out of the loop
            break

        # Display the current frame
    cv2.imshow('Captured Image', frame)

    # Close the webcam
    cap.release()
    cv2.destroyAllWindows()
capture_image("ImagesAttendance")
