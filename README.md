# CodeAlpha Object Detection and Tracking

A real-time Object Detection and Tracking system developed using YOLOv8, OpenCV, and ByteTrack as part of the CodeAlpha Internship Program.

The application can process webcam input or video files, detect multiple objects in real time, assign tracking IDs, display confidence scores, count detected objects, and save the processed output video.

---

# Features

- Real-time webcam object detection
- Video file object detection
- Object tracking with unique IDs
- Bounding boxes with labels
- Confidence score display
- FPS (Frames Per Second) monitoring
- Live object counting
- Processed output video saving
- Professional command-line menu

---

# Technologies Used

- Python
- OpenCV
- YOLOv8
- Ultralytics
- ByteTrack

---

# Project Structure

```text
CodeAlpha_ObjectDetectionTracking/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── test_video.mp4
└── outputs/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_ObjectDetectionTracking.git
```

Navigate into the project folder:

```bash
cd CodeAlpha_ObjectDetectionTracking
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the application:

```bash
python main.py
```

You will see the following menu:

```text
1. Webcam detection
2. Video file detection
3. Exit
```

Choose:

- `1` for webcam detection
- `2` for video file detection

For video file detection, enter the video path:

```text
test_video.mp4
```

---

# Output

Processed videos are automatically saved inside the `outputs/` folder.

Example:

```text
outputs/webcam_output.mp4
outputs/video_output.mp4
```

---

# How the System Works

1. OpenCV captures frames from the webcam or video file.
2. YOLOv8 performs object detection on each frame.
3. ByteTrack assigns unique tracking IDs to detected objects.
4. OpenCV draws:
   - Bounding boxes
   - Object labels
   - Confidence scores
   - Tracking IDs
   - FPS counter
   - Object count panel
5. The processed frames are displayed live and saved as output videos.

---

# Internship Task Requirements Completed

This project satisfies the following CodeAlpha Task 4 requirements:

- Real-time video input using webcam or video file
- Pre-trained YOLO model for object detection
- Frame-by-frame object detection processing
- Bounding boxes and labels
- Object tracking implementation
- Real-time display with tracking IDs

---

# Example Applications

- Smart surveillance systems
- Autonomous vehicles
- Smart traffic monitoring
- Retail analytics
- Assistive systems for visually impaired users
- Human activity tracking

---

# Future Improvements

Possible future enhancements:

- Deep SORT integration
- Custom-trained YOLO models
- Heatmap generation
- Person re-identification
- Face recognition integration
- GPU optimization
- Web dashboard support

---

# Author

Lynn Sawtary

CodeAlpha Internship Project