# OpenCV Image I/O Basics

This repository contains my first computer vision exercises under **Zgt Studio**.  
The goal is to practice basic image input/output (I/O) operations with OpenCV:  
loading images, displaying them in a window, saving copies, and exploring image matrix properties.

---

## 1. Exercises

### 1.1 OpenCV Image Reading, Displaying and Saving

Folder: `OpenCV Image Reading, Displaying and Saving/`

This example works with the classic `cameraman.tif` image and focuses on simple image I/O.

**Script:**

- `main.py`
  - reads `cameraman.tif` in grayscale mode,
  - displays the image in a window titled `"Cameraman"`,
  - saves a copy as `new_black_white_image.png` in the same folder.

**Data:**

- `cameraman.tif` – classic test image used in many image processing examples.
- `new_black_white_image.png` – output image created by `main.py`.

---

### 1.2 OpenCV Image Properties: Shape, Type and Value Range

Folder: `OpenCV Image Properties Shape, Type and Value Range/`

This example works with a color bird image and focuses on the basic properties of the image matrix.

**Script:**

- `bird_image_properties.py`
  - reads `bird.jpg`,
  - checks if the file exists and raises an error if it cannot be loaded,
  - displays the image in a window titled `"Bird"`,
  - prints the following information to the terminal:
    - `shape`  → `(height, width, channels)`
    - `dtype`  → data type (for example `uint8`)
    - `min` / `max` pixel values in the image.

**Data:**

- `bird.jpg` – sample color image used to inspect image properties.

---

## 2. Project structure

```text
opencv-image-io-basics/
├─ OpenCV Image Reading, Displaying and Saving/
│  ├─ main.py
│  ├─ cameraman.tif
│  └─ new_black_white_image.png
├─ OpenCV Image Properties Shape, Type and Value Range/
│  ├─ bird_image_properties.py
│  └─ bird.jpg
└─ README.md
