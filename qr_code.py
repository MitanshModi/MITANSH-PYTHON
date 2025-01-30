import qrcode as qr

# URL to encode into the QR code
url = "https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl"

# Create the QR code with some adjustments
qr_code = qr.QRCode(
    version=1,  # Adjust version (larger numbers give larger, more complex codes)
    error_correction=qr.constants.ERROR_CORRECT_L,  # Lower error correction for more data capacity
    box_size=10,  # Increase size of each box (default is 10)
    border=4  # Border width (default is 4)
)

# Add the URL to the QR code
qr_code.add_data(url)
qr_code.make(fit=True)

# Create the image of the QR code
img = qr_code.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("wscube_youtube.png")

# Optionally, display the image
img.show()
