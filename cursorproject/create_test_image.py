from PIL import Image, ImageDraw, ImageFont
import os

# Create a simple certificate image
img = Image.new('RGB', (800, 600), color='white')
draw = ImageDraw.Draw(img)

# Try to use a default font, or fallback to a simple approach
try:
    # Try to use a default font
    font = ImageFont.load_default()
except:
    font = None

# Draw some certificate-like text
draw.text((100, 100), "CERTIFICATE OF COMPLETION", fill='black', font=font)
draw.text((100, 200), "This is to certify that", fill='black', font=font)
draw.text((100, 250), "John Doe", fill='black', font=font)
draw.text((100, 300), "has successfully completed the course", fill='black', font=font)
draw.text((100, 350), "Blockchain Technology Fundamentals", fill='black', font=font)
draw.text((100, 400), "Issued on: October 18, 2025", fill='black', font=font)
draw.text((100, 450), "Certificate ID: CERT-2025-001", fill='black', font=font)

# Save the image
img.save('test_certificate.png')
print("Test certificate created at test_certificate.png")