import os
import sys
import platform
import subprocess
import urllib.request
import tempfile
import zipfile

def install_tesseract_windows():
    """Install Tesseract OCR on Windows"""
    print("Installing Tesseract OCR for Windows...")
    
    # URL for Tesseract installer (updated to latest version)
    tesseract_url = "https://github.com/UB-Mannheim/tesseract/releases/download/v5.5.0.20241111/tesseract-ocr-w64-setup-5.5.0.20241111.exe"
    
    # Download the installer to a temporary file
    print("Downloading Tesseract OCR installer...")
    temp_dir = tempfile.gettempdir()
    installer_path = os.path.join(temp_dir, "tesseract_installer.exe")
    
    try:
        urllib.request.urlretrieve(tesseract_url, installer_path)
        print("Download complete!")
        
        # Run the installer with silent mode
        print("Installing Tesseract OCR...")
        subprocess.run([installer_path, "/S"], check=True)
        print("Tesseract OCR installed successfully!")
        
        # Clean up the installer
        os.remove(installer_path)
        
        # Add Tesseract to PATH
        tess_path = r"C:\Program Files\Tesseract-OCR"
        if os.path.exists(tess_path):
            # Add to system PATH
            current_path = os.environ.get("PATH", "")
            if tess_path not in current_path:
                new_path = current_path + ";" + tess_path
                # Note: This only affects the current session
                os.environ["PATH"] = new_path
                print(f"Added {tess_path} to PATH")
            
            print("Tesseract OCR installation completed!")
            print("Please restart your command prompt or IDE for PATH changes to take effect.")
            return True
        else:
            print("Installation path not found!")
            return False
            
    except Exception as e:
        print(f"Error installing Tesseract OCR: {e}")
        return False

def install_tesseract_linux():
    """Install Tesseract OCR on Linux"""
    print("Installing Tesseract OCR for Linux...")
    try:
        # Try apt (Debian/Ubuntu)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "tesseract-ocr"], check=True)
        print("Tesseract OCR installed successfully!")
        return True
    except:
        try:
            # Try yum (CentOS/RHEL)
            subprocess.run(["sudo", "yum", "install", "-y", "tesseract"], check=True)
            print("Tesseract OCR installed successfully!")
            return True
        except:
            try:
                # Try dnf (Fedora)
                subprocess.run(["sudo", "dnf", "install", "-y", "tesseract"], check=True)
                print("Tesseract OCR installed successfully!")
                return True
            except Exception as e:
                print(f"Error installing Tesseract OCR: {e}")
                return False

def install_tesseract_mac():
    """Install Tesseract OCR on macOS"""
    print("Installing Tesseract OCR for macOS...")
    try:
        # Try Homebrew
        subprocess.run(["brew", "install", "tesseract"], check=True)
        print("Tesseract OCR installed successfully!")
        return True
    except Exception as e:
        print(f"Error installing Tesseract OCR: {e}")
        return False

def main():
    """Main installation function"""
    print("Tesseract OCR Installation Script")
    print("=" * 35)
    
    system = platform.system().lower()
    
    if system == "windows":
        success = install_tesseract_windows()
    elif system == "linux":
        success = install_tesseract_linux()
    elif system == "darwin":  # macOS
        success = install_tesseract_mac()
    else:
        print(f"Unsupported operating system: {system}")
        return False
    
    if success:
        print("\nInstallation completed successfully!")
        print("You may need to restart your terminal or IDE for the changes to take effect.")
        return True
    else:
        print("\nInstallation failed!")
        return False

if __name__ == "__main__":
    main()