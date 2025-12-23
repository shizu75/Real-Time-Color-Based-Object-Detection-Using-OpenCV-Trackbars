# Real-Time Color-Based Object Detection Using OpenCV Trackbars

## Project Overview
This project demonstrates a **real-time object detection system** based on **color segmentation** using **OpenCV**. It allows users to dynamically tune HSV color thresholds through interactive trackbars to isolate and detect objects of specific colors from a live webcam feed.

The project is highly educational and practical, showcasing how classical computer vision techniques can be used for object detection without deep learning.

---

## Objectives
- Perform real-time object detection using color segmentation
- Understand HSV color space for robust detection
- Use OpenCV trackbars for live threshold tuning
- Detect object contours from segmented masks
- Visualize multiple processing stages simultaneously

---

## Technologies Used
- Python 3
- OpenCV (cv2)
- NumPy

---

## Core Concepts Used
- HSV Color Space
- Image Thresholding
- Masking and Bitwise Operations
- Contour Detection
- Real-Time Video Processing
- Interactive Trackbars

---

## How the System Works

### 1. Video Capture
- Webcam feed is captured using OpenCV
- Frames are flipped horizontally for natural interaction
- Frames resized to optimize performance

---

### 2. Trackbar-Based Control
The following interactive trackbars are provided:

#### Threshold Control
- **th** – Binary threshold value for mask refinement

#### Lower HSV Bounds
- **lb** – Lower Hue
- **lg** – Lower Saturation
- **lr** – Lower Value

#### Upper HSV Bounds
- **ub** – Upper Hue
- **ug** – Upper Saturation
- **ur** – Upper Value

These sliders allow real-time adjustment of color ranges for object isolation.

---

### 3. Color Segmentation
- Frame is converted from BGR to HSV color space
- User-defined HSV range is applied using `cv2.inRange`
- A binary mask is created isolating the target color

---

### 4. Mask Refinement
- Thresholding applied to clean the binary mask
- Bitwise operations extract the detected object
- Inverted results generated for visualization

---

### 5. Contour Detection
- Contours are detected from the thresholded mask
- All detected contours are drawn on the original frame
- Helps identify object boundaries clearly

---

### 6. Visualization Layout
The final display combines multiple views:
- Original Image with Contours
- Binary Mask (stacked as 3-channel)
- Resulting Color-Segmented Image
- HSV Converted Frame

All views are stacked horizontally and vertically for easy comparison.

---

## Output
- Live webcam feed
- Adjustable real-time color detection
- Highlighted object contours
- Multi-panel visualization window
- Binary threshold preview window

---

## How to Run the Project

### Prerequisites
Ensure the following libraries are installed:
- opencv-python
- numpy

---

### Execution Steps
1. Connect a webcam
2. Run the Python script
3. Use trackbars to adjust HSV values
4. Observe real-time object detection
5. Press **'p'** to exit the application

---

## Learning Outcomes
- Strong understanding of HSV-based segmentation
- Practical experience with OpenCV trackbars
- Real-time contour detection skills
- Knowledge of image masking and thresholding
- Foundation for more advanced object detection systems

---

## Limitations
- Sensitive to lighting conditions
- Detects color-based objects only
- No object classification
- Manual threshold tuning required

---

## Future Enhancements
- Add automatic color calibration
- Integrate morphological operations for noise removal
- Implement object tracking (e.g., CamShift or Kalman Filter)
- Add bounding boxes and object labels
- Extend to multi-color detection

---

## Use Cases
- Learning computer vision fundamentals
- Color-based object tracking
- Robotics and automation prototypes
- Educational demonstrations
- Real-time vision experimentation

---

## Author
Developed as a hands-on computer vision project to demonstrate real-time color-based object detection using OpenCV and interactive trackbars.
