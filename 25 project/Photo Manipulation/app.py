import cv2
import numpy as np
from PIL import Image, ImageEnhance

# 🖼️ Load Image
image_path = "sample.jpg"  # Apna image path yahan dalna
image = Image.open(image_path)

# ✅ Function to Adjust Brightness
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# ✅ Function to Adjust Contrast
def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# ✅ Function to Apply Blur
def apply_blur(image, blur_strength):
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    blurred = cv2.GaussianBlur(image_cv, (blur_strength, blur_strength), 0)
    return Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))

# 🎨 Apply Filters
bright_image = adjust_brightness(image, 1.5)  # 1.5 = 50% brighter
contrast_image = adjust_contrast(image, 2.0)  # 2.0 = Higher contrast
blurred_image = apply_blur(image, 15)  # Blur intensity

# 💾 Save Filtered Images
bright_image.save("brightened_image.jpg")
contrast_image.save("contrast_image.jpg")
blurred_image.save("blurred_image.jpg")

print("✅ Image Processing Done! Check the output images.")
