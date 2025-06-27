import cv2
import os
import matplotlib.pyplot as plt

# Path to the noisy image
noisy_image_path = r"E:\Academic 7th Sem\Image_Processing\Assignment_2\Computer_Vision\result\Gaussian noise image.jpeg"
noisy_image = cv2.imread(noisy_image_path, cv2.IMREAD_GRAYSCALE)

if noisy_image is None:
    raise FileNotFoundError(f"Image not found at {noisy_image_path}")

# Apply Otsu's thresholding
_, otsu_result = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Save the result to the result folder
output_dir = r"E:\Academic 7th Sem\Image_Processing\Assignment_2\Computer_Vision\Result"
os.makedirs(output_dir, exist_ok=True)
otsu_output_path = os.path.join(output_dir, "Otsu Threshold Image.jpeg")
cv2.imwrite(otsu_output_path, otsu_result)

# Display the result
plt.figure(figsize=(8, 4))
plt.imshow(otsu_result, cmap='gray')
plt.title("Otsu Thresholding Result")
plt.axis('off')
plt.tight_layout()
plt.show()
