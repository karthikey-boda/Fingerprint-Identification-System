import cv2
import os

PROCESSED_FOLDER = "processed"
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def preprocess_image(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize
    resized = cv2.resize(gray, (300, 300))

    # Histogram Equalization
    equalized = cv2.equalizeHist(resized)

    # Gaussian Blur
    blurred = cv2.GaussianBlur(equalized, (5, 5), 0)

    # Binary Threshold
    _, binary = cv2.threshold(
        blurred,
        127,
        255,
        cv2.THRESH_BINARY
    )

    filename = os.path.basename(image_path)
    output_path = os.path.join(PROCESSED_FOLDER, filename)

    cv2.imwrite(output_path, binary)

    return output_path