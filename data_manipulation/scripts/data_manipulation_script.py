from PIL import Image
import imagehash

# Function to detect changes in images using hashing
def detect_image_changes(original_img, edited_img):
    # Load images using PIL
    img_original = Image.open(original_img)
    img_edited = Image.open(edited_img)

    # Compute hashes for the images
    hash_original = imagehash.average_hash(img_original)
    hash_edited = imagehash.average_hash(img_edited)

    # Compare the hashes
    if hash_original == hash_edited:
        return "Images are identical."
    else:
        return "Changes detected in the images."

# Paths to your original and edited images
# original_image_path = 'original_image.png'  # Replace with the path to your original image
# edited_image_path = 'edited_image.png'  # Replace with the path to your edited image

# Detect changes in images
# detect_image_changes(original_image_path, edited_image_path)