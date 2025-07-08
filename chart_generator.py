import random
import string
import numpy as np
import cv2
import time

def generate_random_word(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def generate_chart_image(word, index):
    # Increase image size for better quality
    img = np.zeros((720, 1280, 3), dtype=np.uint8)  # Larger canvas (720p)
    
    # Increase base font scale and reduce scaling between lines
    font_scale = 6.0 - (index * 0.4)  # Start larger, decrease less per line
    font_scale = max(2.5, font_scale)  # Set minimum font size larger
    
    # Get text size and position
    text_size = cv2.getTextSize(word, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 8)[0]
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = (img.shape[0] + text_size[1]) // 2
    
    # Draw text with thicker border for better visibility
    cv2.putText(img, word, (text_x, text_y), 
               cv2.FONT_HERSHEY_SIMPLEX, font_scale, 
               (255, 255, 255), 12, cv2.LINE_AA)  # Increased thickness to 12
    return img

CHART_WORDS = [generate_random_word(i + 1) for i in range(7)]
CHART_IMAGES = [generate_chart_image(word, idx) for idx, word in enumerate(CHART_WORDS)]

# Your run_test() function goes below this and assumes CHART_WORDS and CHART_IMAGES are defined
