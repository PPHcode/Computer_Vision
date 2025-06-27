# Computer_Vision

This project contains implementations of the following image processing tasks using Python and OpenCV


## Task 1: Gaussian Noise + Otsu’s Thresholding

### Description:
- Load an image containing two objects and a background (3 distinct pixel values).
- Add Gaussian noise to the image.
- Apply Otsu’s thresholding to segment the objects automatically.

### Files:
- `add_gaussian_noise.py`: Adds Gaussian noise and saves the noisy image.
- `otsu_threshold.py`: Applies Otsu’s thresholding.


### Output:
- `Gaussian noise image.jpeg`
- `Otsu Threshold Image.jpeg`
---

## Task 2: Region Growing Segmentation

### Description:
- Implemented region growing based on a manually chosen seed point.
- Recursively adds neighboring pixels if their intensity is within a threshold of the seed pixel.

### Files:
- `region_growing.py`: Implements and saves region-growing segmentation.
- Accepts seed point and intensity threshold for customization.

### Output:
- `Region Growing Result.jpeg`

---

## 🔧 Requirements

Install dependencies using pip (within virtual environment):

```bash
pip install opencv-python numpy matplotlib
