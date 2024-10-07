# Hand-Controlled Cursor

A computer vision-based project that allows users to control all cursor operations using hand gestures without requiring additional hardware. This project utilizes **OpenCV** and **MediaPipe** for hand detection and gesture recognition to replace traditional mouse operations with simple hand movements.

## Features

- **Hand Tracking:** Detects hand landmarks and tracks movements in real time.
- **Cursor Control:** Move the cursor by simply moving your hand.
- **Clicking:** Perform left-clicks by creating specific gestures.
- **Dragging:** Control drag-and-drop operations by holding specific hand positions.
- **No Additional Hardware:** All operations are performed using your webcam, with no need for external devices.

## Technology Stack

- **OpenCV:** Used for real-time video capture and image processing.
- **MediaPipe:** Provides hand tracking and gesture recognition.
- **PyAutoGUI:** Simulates mouse control and actions based on hand gestures.

## How It Works

1. The webcam captures live video feed.
2. MediaPipe detects and tracks hand landmarks in the video.
3. Hand gestures are mapped to specific mouse operations such as cursor movement, clicks, and drags.
4. PyAutoGUI simulates the mouse actions corresponding to the detected gestures.

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/omshete96/hand-controlled-cursor.git
    cd hand-controlled-cursor
    ```

2. Install the required Python libraries:
    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

### Running the Application

1. Run the Python script:
    ```bash
    python hand_controlled_cursor.py
    ```

2. The webcam feed will open, and the system will start detecting hand movements. Use specific hand gestures to control the cursor.

### Closing the Application

- Press the `Esc` key to close the application gracefully.
- Alternatively, you can use `Ctrl + C` to forcefully terminate the program via the terminal.

## Usage

- **Move the cursor:** Move your hand in front of the camera.
- **Left-click:** Perform a specific gesture (e.g., pinching with your thumb and index finger).
- **Drag-and-drop:** Hold the click gesture and move your hand to drag objects.
- **Right-click and more:** Customize gestures as needed by modifying the code.

## Future Enhancements

- Add support for right-click and double-click gestures.
- Implement gesture-based scrolling.
- Improve hand gesture recognition for a smoother user experience.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue. Any contributions are welcome!

## License

This project is licensed under the MIT License.

