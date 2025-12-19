import os
import base64
import json
import hashlib
import logging
from typing import Dict, Any, Optional
import random
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Import OCR module
try:
    import ocr
    extract_text_from_file = ocr.extract_text_from_file
    extract_structured_data = ocr.extract_structured_data
    OCR_AVAILABLE = True
except Exception as e:
    logging.error(f"Error importing OCR module: {str(e)}")
    extract_text_from_file = None
    extract_structured_data = None
    OCR_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AES encryption key (32 bytes for AES-256)
# In production, this should be securely stored and not hardcoded
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "trustededucationcertificatesecuritykey").encode()[:32]
IV = b"trustededucation"[:16]  # 16 bytes initialization vector

def encrypt_data(data: str) -> str:
    """Encrypt data using AES-256 encryption"""
    try:
        # Convert data to bytes
        data_bytes = data.encode()
        
        # Add padding
        padder = padding.PKCS7(128).padder()  # AES block size is 128 bits
        padded_data = padder.update(data_bytes) + padder.finalize()
        
        # Create cipher
        cipher = Cipher(
            algorithms.AES(ENCRYPTION_KEY),
            modes.CBC(IV),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        
        # Encrypt data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Return base64 encoded string
        return base64.b64encode(encrypted_data).decode()
    except Exception as e:
        logger.error(f"Encryption error: {str(e)}")
        return ""

def decrypt_data(encrypted_data: str) -> str:
    """Decrypt data using AES-256 encryption"""
    try:
        # Decode base64 string
        encrypted_bytes = base64.b64decode(encrypted_data)
        
        # Create cipher
        cipher = Cipher(
            algorithms.AES(ENCRYPTION_KEY),
            modes.CBC(IV),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        
        # Decrypt data
        decrypted_padded = decryptor.update(encrypted_bytes) + decryptor.finalize()
        
        # Remove padding
        unpadder = padding.PKCS7(128).unpadder()  # AES block size is 128 bits
        decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
        
        # Return decoded string
        return decrypted_data.decode()
    except Exception as e:
        logger.error(f"Decryption error: {str(e)}")
        return ""

def generate_hash(data: Dict[str, Any]) -> str:
    """Generate SHA-256 hash from certificate data"""
    try:
        # Convert dictionary to sorted JSON string to ensure consistent hashing
        data_str = json.dumps(data, sort_keys=True)
        # Generate hash
        hash_obj = hashlib.sha256(data_str.encode())
        return hash_obj.hexdigest()
    except Exception as e:
        logger.error(f"Hash generation error: {str(e)}")
        return ""

def extract_certificate_data(image_bytes: bytes, filename: str = "certificate.jpg") -> Dict[str, Any]:
    """
    Extract certificate data using Tesseract OCR instead of Google's Gemini API
    """
    try:
        # Check if OCR is available
        if not OCR_AVAILABLE or extract_text_from_file is None or extract_structured_data is None:
            logger.warning("OCR not available, using fallback values")
            return _get_fallback_data()
        
        # Extract text from image using OCR
        ocr_text = extract_text_from_file(filename, image_bytes)
        logger.info(f"OCR text extracted: {ocr_text[:200]}...")  # Log first 200 characters
        
        # Extract structured data from OCR text
        structured_data = extract_structured_data(ocr_text)
        logger.info(f"Structured data extracted: {structured_data}")
        
        # Format the extracted data to match the expected structure
        extracted_data = {
            "student_name": structured_data.get("name", "Unknown Name"),
            "institution_name": structured_data.get("institution", "Unknown Institution"),
            "certificate_id": structured_data.get("certificate_id", f"AUTO-{random.randint(10000, 99999)}"),
            "issue_date": datetime.now().strftime("%Y-%m-%d"),
            "year": structured_data.get("year", datetime.now().year)
        }
        
        # Encrypt sensitive data using AES-256
        encrypted_data = {
            "student_name": encrypt_data(extracted_data["student_name"]),
            "certificate_id": encrypt_data(extracted_data["certificate_id"]),
            "issue_date": encrypt_data(extracted_data["issue_date"]),
            "institution_name": encrypt_data(extracted_data["institution_name"])
        }
        
        # Add encrypted data to the result
        extracted_data["encrypted_data"] = encrypted_data
        
        # Generate hash for the certificate data
        file_hash = generate_hash(extracted_data)
        extracted_data["file_hash"] = file_hash
        
        logger.info(f"Final extracted data: {extracted_data}")
        return extracted_data
        
    except Exception as e:
        logger.error(f"OCR extraction error: {e}")
        return _get_fallback_data()

def _get_fallback_data() -> Dict[str, Any]:
    """Generate fallback data when OCR extraction fails"""
    default_data = {
        "student_name": "Unknown Name",
        "institution_name": "Unknown Institution",
        "certificate_id": f"AUTO-{random.randint(10000, 99999)}",
        "issue_date": datetime.now().strftime("%Y-%m-%d"),
        "year": datetime.now().year
    }
    
    # Encrypt default data
    encrypted_default = {
        "student_name": encrypt_data(default_data["student_name"]),
        "certificate_id": encrypt_data(default_data["certificate_id"]),
        "issue_date": encrypt_data(default_data["issue_date"]),
        "institution_name": encrypt_data(default_data["institution_name"])
    }
    
    default_data["encrypted_data"] = encrypted_default
    default_data["file_hash"] = generate_hash(default_data)
    
    return default_data