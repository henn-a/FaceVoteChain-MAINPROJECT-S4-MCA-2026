import cv2
import numpy as np
import random
from datetime import datetime
def generate_image(fn):
    # Define the dimensions of the image
    width = 400
    height = 300

    # Create a white background image
    background = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Generate a random number
    random_number = random.randint(1000, 9999)

    # Choose font, scale, and color
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 2
    color = (0, 0, 0)  # Black color

    # Determine text size to center it on the image
    text_size = cv2.getTextSize(str(random_number), font, scale, 2)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    # Put the random number on the white background image
    cv2.putText(background, str(random_number), (text_x, text_y), font, scale, color, 2, cv2.LINE_AA)

    cv2.imwrite(r"E:\e_voting\media\img/"+fn,background)

    image = background

    # Split the image into its channels (BGR)
    b, g, r = cv2.split(image)

    # Extract the first 4 bits (upper nibble) and last 4 bits (lower nibble)
    upper_nibble_b = (b & 15)<<4
    lower_nibble_b = (b & 240)

    upper_nibble_g = (g & 15)<<4
    lower_nibble_g = g & 240

    upper_nibble_r = (r & 15)<<4
    lower_nibble_r = r & 240

    # Combine the upper and lower nibbles into shares
    upper_share = cv2.merge([upper_nibble_b, upper_nibble_g, upper_nibble_r])
    lower_share = cv2.merge([lower_nibble_b, lower_nibble_g, lower_nibble_r])

    cb=upper_nibble_b>>4|lower_nibble_b
    cg=upper_nibble_g>>4|lower_nibble_g
    cr=upper_nibble_r>>4|lower_nibble_r

    cimg=cv2.merge([cb, cg, cr])

    # Display the shares
    cv2.imshow('Upper Share', upper_share)
    cv2.imwrite(r"E:\e_voting\media\share1/" + fn, upper_share)

    cv2.imshow('Lower Share', lower_share)
    cv2.imwrite(r"E:\e_voting\media\share2/" + fn, lower_share)
    cv2.imwrite("c"+ fn, lower_share)


generate_image("2.png")