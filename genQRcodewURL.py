import pyqrcode
from pyqrcode import QRCode
import re
import os

# Function to sanitize the URL for use as a filename
def sanitize_filename(url):
    # Remove any characters that are not alphanumeric, underscore, or hyphen
    sanitized = re.sub(r'[^\w\s-]', '', url)
    # Replace spaces and multiple hyphens with a single hyphen
    sanitized = re.sub(r'[-\s]+', '-', sanitized)
    return sanitized

# Prompt the user to enter a URL
url = input("Enter the URL to be converted to QR code: ")

# Sanitize the URL to create a valid filename
filename = sanitize_filename(url) + ".png"

# Generate QR code
qr = pyqrcode.create(url)

# Create and save the png file with the sanitized URL as the filename
qr.png(filename, scale=8)

print(f"QR code has been generated and saved as '{filename}'")
