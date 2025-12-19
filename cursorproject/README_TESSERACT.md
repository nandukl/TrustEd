# Tesseract OCR Installation Guide

This guide will help you install Tesseract OCR to enable automatic certificate data extraction in the TrustEd system.

## What is Tesseract OCR?

Tesseract is an open-source Optical Character Recognition (OCR) engine that can extract text from images. In the TrustEd system, it's used to automatically extract student names, institutions, certificate IDs, and other information from certificate images.

## Installation Instructions

### Windows

#### Option 1: Automatic Installation (Recommended)
1. Run the installation script:
   ```bash
   python install_tesseract.py
   ```

#### Option 2: Manual Installation
1. Download the Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer and follow the installation wizard
3. Make sure to check the option to add Tesseract to your PATH environment variable
4. Restart your command prompt or IDE after installation

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install tesseract-ocr
```

### Linux (CentOS/RHEL)
```bash
sudo yum install tesseract
```

### macOS
```bash
# Install Homebrew if you haven't already
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Tesseract
brew install tesseract
```

## Verifying Installation

After installation, verify that Tesseract is properly installed by running:
```bash
tesseract --version
```

You should see output similar to:
```
tesseract v5.0.0-alpha.20210506
leptonica-1.78.0
```

## Language Support

By default, Tesseract includes English language support. To install additional language packs:

### Windows
During installation, select the languages you want to support.

### Linux/macOS
```bash
# For additional languages (e.g., Spanish)
sudo apt install tesseract-ocr-spa

# List all available language packs
apt-cache search tesseract-ocr
```

## Configuration

The TrustEd system automatically detects Tesseract installation. If Tesseract is installed in a non-standard location, you can set the `TESSERACT_PATH` environment variable:

### Windows
```cmd
set TESSERACT_PATH=C:\path\to\tesseract.exe
```

### Linux/macOS
```bash
export TESSERACT_PATH=/path/to/tesseract
```

## Troubleshooting

### Tesseract not found
If you get an error that Tesseract is not found:
1. Make sure Tesseract is installed
2. Restart your terminal or IDE
3. Check that Tesseract is in your PATH environment variable
4. Set the `TESSERACT_PATH` environment variable manually if needed

### Poor OCR accuracy
If the extracted data is inaccurate:
1. Ensure the certificate images are clear and high-resolution
2. Try improving image quality (contrast, brightness)
3. Install language packs for the language used in certificates
4. The system uses multiple OCR passes with different preprocessing - this should handle most image quality issues

## Fallback Mechanism

If Tesseract is not available or fails to extract data, the system will:
1. Attempt to extract information from the filename
2. Use default placeholder values ("John Doe", "Example University", etc.)
3. Still generate a blockchain hash for the certificate

This ensures the system remains functional even without OCR capabilities.