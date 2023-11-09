import cv2
import numpy as np
import os

# Function to detect digitally tampered regions in the image
def detect_tampered_regions(original_img, edited_img, save_directory):
    # Load images using OpenCV
    img_original = cv2.imread(original_img)
    img_edited = cv2.imread(edited_img)

    # Convert images to grayscale
    gray_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    gray_edited = cv2.cvtColor(img_edited, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference between the images
    diff_image = cv2.absdiff(gray_original, gray_edited)

    # Threshold the difference to identify changed areas
    _, threshold = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)

    # Find contours to identify altered regions
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the altered regions
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_original, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the regions that are potentially tampered
    # cv2.imshow('Potentially Tampered Regions', img_original)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    save_path = os.path.join(save_directory, "tampered_regions.jpg")
    cv2.imwrite(save_path, img_original)

    return save_path
    

# Paths to your original and edited images
# original_image_path = '/Users/tanmoysaha/Works/PythonWorks/fraud_analysis/media/originalImage.png'
# edited_image_path = '/Users/tanmoysaha/Works/PythonWorks/fraud_analysis/media/editedImage.png'

# Detect tampered regions in images
# detect_tampered_regions(original_image_path, edited_image_path, '/Users/tanmoysaha/Works/PythonWorks/fraud_analysis/media/')