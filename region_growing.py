import cv2
import numpy as np
import matplotlib.pyplot as plt

def region_growing(image, seed_point, threshold=10):
   
    height, width = image.shape
    segmented = np.zeros((height, width), dtype=np.uint8)
    visited = np.zeros((height, width), dtype=bool)

    seed_value = image[seed_point]
    stack = [seed_point]

    while stack:
        x, y = stack.pop()
        if visited[x, y]:
            continue

        visited[x, y] = True
        if abs(int(image[x, y]) - int(seed_value)) <= threshold:
            segmented[x, y] = 255

            # Add 8-connected neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < height and 0 <= ny < width and not visited[nx, ny]:
                        stack.append((nx, ny))

    return segmented



image_path = r"E:\Academic 7th Sem\Image_Processing\Assignment_2\Computer_Vision\Images\IMG.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Set seed point 
seed = (30, 30)  
threshold = 15   

# Apply region growing
segmented_image = region_growing(image, seed, threshold)

# Save result
output_path = r"E:\Academic 7th Sem\Image_Processing\Assignment_2\Computer_Vision\Result\Region Growing Result.jpeg"
cv2.imwrite(output_path, segmented_image)

# Display result
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Region Growing Result")
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
