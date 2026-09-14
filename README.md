# Study Guide

A simple Python-based webcam motion detection project that detects significant movement, triggers an audio alert, and records the webcam feed.

> **Note:** The repository is currently named `study_guide`, while the code implements a webcam motion detection system.

## Features

* 📷 Captures live video from the default webcam
* 🔍 Detects motion by comparing consecutive video frames
* 🖼️ Highlights areas where significant motion is detected
* 🔊 Plays an alert sound when persistent motion is detected
* 🎥 Records the webcam feed as an `.avi` video
* 🕒 Automatically adds timestamps to recorded filenames
* ⚡ Processes frames at a reduced resolution for better performance
* ⌨️ Press `Q` to stop the program

## Tech Stack

* **Python**
* **OpenCV** — webcam capture, image processing, motion detection, and video recording
* **Pygame** — audio alert
* **NumPy** — numerical/image-processing dependency used by OpenCV

## How It Works

The program follows a simple motion-detection pipeline:

1. Opens the default webcam.
2. Captures the first frame and converts it to grayscale.
3. Applies Gaussian blur to reduce image noise.
4. Captures subsequent frames.
5. Calculates the difference between the previous and current frames.
6. Applies a threshold to identify significant changes.
7. Finds contours in the thresholded image.
8. If a contour exceeds the configured area threshold, motion is detected.
9. Persistent motion triggers an audio alert.
10. The processed video is saved to a timestamped `.avi` file.

The current implementation uses a `320 × 240` frame size and skips some frames to reduce processing requirements.

## Requirements

* Python 3.x
* A working webcam
* A system capable of playing audio

## Installation

Clone the repository:

```bash
git clone https://github.com/harshitpatilx/study_guide.git
cd study_guide
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Setup

Place the required alert sound file in the same directory as the Python script:

```text
study_guide/
├── main.py
├── alert.wav
├── requirements.txt
├── README.md
└── .gitignore
```

The program currently expects the file to be named:

```text
alert.wav
```

## Running the Project

Run:

```bash
python main.py
```

The webcam feed will open in a window.

Press:

```text
Q
```

to stop the program.

## Output

When the program runs, recorded video files are created using timestamps, for example:

```text
motion_recording_2026-09-15_00-42-10.avi
```

## Configuration

Some motion-detection parameters can be adjusted directly in `main.py`.

### Resolution

The current webcam resolution is:

```text
320 × 240
```

### Motion Threshold

The pixel-difference threshold is currently set to:

```text
25
```

### Contour Area

Motion is considered significant when a detected contour has an area greater than:

```text
1500
```

### Motion Persistence

The alert is triggered after motion persists for more than:

```text
4
```

processed motion frames.

These values can be tuned depending on the environment and desired sensitivity.

## Project Structure

```text
study_guide/
│
├── main.py
├── alert.wav
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

Possible improvements for future versions:

* Add a configurable camera selection
* Add a graphical user interface
* Allow users to configure motion sensitivity
* Add recording start/stop controls
* Automatically stop recording after a period of inactivity
* Store recordings in a dedicated directory
* Add configurable alert sounds
* Improve motion detection against lighting changes
* Add support for multiple cameras
* Add logging and error handling
* Add configuration through a `.json` or `.env` file

## License

This project is intended for personal and educational use.

## Author

**Harshit Patil**

GitHub: [github.com/harshitpatilx](https://github.com/harshitpatilx)
