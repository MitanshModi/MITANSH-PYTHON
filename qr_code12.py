import qrcode
from PIL import Image

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,  # You can adjust the version for larger or more complex codes
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Use a lower error correction for more data
    box_size=10,  # Increase the box size for better scanning
    border=4,
)

# Add data to the QR code
qr.add_data("https://www.chittorgarh.com/ipo/ipo_dashboard.asp")
qr.make(fit=True)

# Create the image with higher contrast
img = qr.make_image(fill_color="black", back_color="white")  # Use black and white for better contrast

# Save the image to a file
img.save("ipo_web.png")

# Optionally, display the image
img.show()
