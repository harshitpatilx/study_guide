import cv2
import pygame
import numpy as np
from datetime import datetime

# Initialize pygame
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("alert.wav")

# Motion detection function
def detect_motion():
    cap = cv2.VideoCapture(0)

    # Set the size of the frame to speed up the process
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Resize width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Resize height

    # Get current timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
    filename = f"motion_recording_{timestamp}.avi"  # Video filename with timestamp

    # Video Writer setup to save video in 240p resolution (320x240)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi files
    out = cv2.VideoWriter(filename, fourcc, 20.0, (320, 240))  # Save at 20 FPS in 240p

    # Read the first frame and convert to grayscale
    ret, frame1 = cap.read()
    if not ret:
        print("Failed to grab frame")
        return

    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

    frame_count = 0  # To skip frames
    motion_counter = 0  # To track duration of motion

    while True:
        ret, frame2 = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame_count += 1

        # Skip some frames to optimize processing
        if frame_count % 3 != 0:
            continue

        frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

        # Find the absolute difference between frames
        frame_diff = cv2.absdiff(frame1_gray, frame2_gray)
        _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) > 1500:  # Threshold for excessive motion
                motion_detected = True
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if motion_detected:
            motion_counter += 1
            # Trigger alert only if the motion is significant and persists
            if motion_counter > 4:  # Motion persistence threshold (number of frames)
                # print("Excessive motion detected!")
                alert_sound.play()  # Play alert sound
                motion_counter = 0  # Reset counter after alert
        else:
            # Reset counter if no motion is detected
            motion_counter = 0

        # Resize the frame to 240p resolution
        frame_resized = cv2.resize(frame2, (320, 240))

        # Write the resized frame to the video file
        out.write(frame_resized)

        # Update the previous frame for the next iteration
        frame1_gray = frame2_gray

        # Display the processed frame
        cv2.imshow("Webcam Feed", frame_resized)

        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()  # Release the video writer
    cv2.destroyAllWindows()

# Run the function
detect_motion()
