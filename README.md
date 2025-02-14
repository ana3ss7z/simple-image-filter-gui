# Simple Image Processor and Filtering with PIL and Tkinter 🖼️✨


This project is focused on applying various image filtering techniques to enhance and manipulate images. The project is implemented in Python and utilizes popular libraries such as OpenCV and NumPy.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [Troubleshooting](#troubleshooting)



## Introduction 🛠️

Image filtering is a technique used to process and enhance images by applying various algorithms. This project demonstrates different filtering methods such as Gaussian blur, median filter, and edge detection.

## Features

- 💫 Load and display images
- 📊 Apply various filters (Gaussian, Median, Min, Max)
- 🎨 Adjust brightness, contrast, color, and sharpness
- 📈 Generate histograms
- 💾 Save the modified images

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/image-filtering-tool.git
    cd image-filtering-tool
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```


## Usage 🖱️

1. **Launch the App:**  
   Run the script using:
   ```bash
   python main.py
   ```
2. **Load an Image:**  
   - Click the "Browse" button and select an image file.  
   - The original image appears on the left, and the working copy on the right.

3. **Apply Filters:**  
   - Select a filter from the dropdown (GaussianBlur, MedianFilter, MaxFilter, MinFilter).  
   - Enter the filter (radius for GaussianBlur and size for MedianFilter, MaxFilter, MinFilter) in the input box.  
   - Press "Enter" to apply the filter.  
   - Save the result using the green save icon.

4. **Enhance Image:**  
   - Choose an enhancement type (Colors, Contrast, Brightness, Sharpness).  
   - Enter a value (e.g., between 0.1 to 3 for adjustments).  
   - Press "Enter" to apply.  
   - Save using the green save icon.

5. **Invert Colors:**  
   - Click the "Invert" button to apply color inversion.  
   - Save using the green save icon.

6. **Generate Histogram:**  
   - Click the "Histogram" button to display color channel histograms for the image.

7. **Reset:**  
   - Click "Reset" to revert all modifications to the original image.

8. **Exit:**  
   - Click "Quit" to close the application.



## Notes 📝
- **File Formats:** The app supports `.png`, `.jpg`, and `.jpeg`.
- **Save Location:** Files are saved with descriptive names based on the modifications applied.

## Troubleshooting 🛎️
- 🛑 **Error: Invalid matrix expression** – Check the filter size input.
- ⚠️ **No image displayed?** Ensure the image path is correct.