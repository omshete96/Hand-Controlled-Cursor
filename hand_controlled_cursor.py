import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,  # Track one hand
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Variables for smoothing cursor movement
prev_x, prev_y = 0, 0
smoothing_factor = 7  # Adjust for smoother or more responsive cursor

# Variables for click and drag
click_threshold = 0.02  # Distance threshold for click
dragging = False

# Frame rate calculation
p_time = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    # Flip the image horizontally for a mirror view
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract landmark positions
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((lm.x, lm.y))

            if lm_list:
                # Index finger tip (landmark 8)
                ix, iy = lm_list[8]
                # Thumb tip (landmark 4)
                tx, ty = lm_list[4]

                # Convert normalized coordinates to screen coordinates
                # Screen width and height are used to map the coordinates
                x = int(ix * screen_width)
                y = int(iy * screen_height)

                # Smoothing the cursor movement
                smoothed_x = prev_x + (x - prev_x) / smoothing_factor
                smoothed_y = prev_y + (y - prev_y) / smoothing_factor
                pyautogui.moveTo(screen_width - smoothed_x, smoothed_y)  # Mirror the cursor movement
                prev_x, prev_y = smoothed_x, smoothed_y

                # Calculate distance between index finger and thumb
                distance = math.hypot(tx - ix, ty - iy)

                # Click Action
                if distance < click_threshold:
                    if not dragging:
                        pyautogui.mouseDown()
                        dragging = True
                        cv2.circle(img, (int(ix * 640), int(iy * 480)), 15, (0, 255, 0), cv2.FILLED)
                else:
                    if dragging:
                        pyautogui.mouseUp()
                        dragging = False
                        cv2.circle(img, (int(ix * 640), int(iy * 480)), 15, (0, 0, 255), cv2.FILLED)

    # Calculate and display Frames Per Second (FPS)
    c_time = time.time()
    fps = 1 / (c_time - p_time) if (c_time - p_time) != 0 else 0
    p_time = c_time
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Hand Controlled Cursor", img)

    # Exit on pressing 'Esc' key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
