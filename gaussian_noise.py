import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load image from absolute path
image_path = r"E:\Academic 7th Sem\Image_Processing\Assignment_2\Computer_Vision\Images\IMG.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Add Gaussian noise
mean = 0
std_dev = 10
noise = np.random.normal(mean, std_dev, image.shape)
noisy_image = image + noise
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

# Save noisy image to 'result' folder
result_dir = r"E:\Academic 7th Sem\Image_Processing\Assignment_2\Computer_Vision\Result"
os.makedirs(result_dir, exist_ok=True)  # create folder if it doesn't exist
output_path = os.path.join(result_dir, "Gaussian noise image.jpeg")
cv2.imwrite(output_path, noisy_image)

# Display original and noisy image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Gaussian Noise Image")
plt.imshow(noisy_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
