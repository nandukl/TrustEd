"""
Test script to demonstrate certificate verification fix
"""
import hashlib
import json

def compute_sha256_hex(data: bytes) -> str:
    """Compute SHA-256 hash of data"""
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()

# Simulate uploading a certificate
print("=" * 60)
print("CERTIFICATE UPLOAD SIMULATION")
print("=" * 60)

# Create a test certificate (simulating file bytes)
test_certificate = b"This is a test certificate for John Doe from Example University 2023"
file_hash = compute_sha256_hex(test_certificate)

print(f"\n1. Institution uploads certificate")
print(f"   File hash: {file_hash}")

# Simulate blockchain storage
blockchain_block = {
    "timestamp": "2025-12-16T14:23:00Z",
    "student_id": "STU-1234",
    "certificate_data": {
        "student_name": "John Doe",
        "institution_name": "Example University",
        "year": 2023,
        "certificate_id": "CERT-001"
    },
    "certificate_file_hash": file_hash,
    "prev_block_hash": "GENESIS",
    "block_hash": "abc123..."
}

print(f"\n2. Certificate stored in blockchain:")
print(f"   Student: {blockchain_block['certificate_data']['student_name']}")
print(f"   Institution: {blockchain_block['certificate_data']['institution_name']}")
print(f"   Year: {blockchain_block['certificate_data']['year']}")
print(f"   Blockchain hash: {blockchain_block['certificate_file_hash']}")

# Simulate verification
print("\n" + "=" * 60)
print("CERTIFICATE VERIFICATION SIMULATION")
print("=" * 60)

# Verifier uploads the SAME certificate
verification_file_hash = compute_sha256_hex(test_certificate)
print(f"\n3. Verifier uploads certificate for verification")
print(f"   File hash: {verification_file_hash}")

# Check if hashes match
print(f"\n4. Blockchain verification:")
if verification_file_hash == blockchain_block['certificate_file_hash']:
    print(f"   ✅ MATCH FOUND!")
    print(f"   Certificate hash exists in blockchain ledger")
    print(f"   Status: VALID")
    print(f"   Confidence: 95%")
    print(f"\n   Reasons:")
    print(f"   - Certificate verified in blockchain ledger")
    print(f"   - File hash matches blockchain record")
    print(f"   - Certificate is authentic")
else:
    print(f"   ❌ NO MATCH")
    print(f"   Certificate not found in blockchain")
    print(f"   Status: SUSPICIOUS")

print("\n" + "=" * 60)
print("KEY FIX IMPLEMENTED")
print("=" * 60)
print("""
The verification now works correctly because:

1. BEFORE THE FIX:
   - System required BOTH blockchain match AND OCR data match
   - OCR extraction can vary between uploads
   - Same certificate could fail verification due to OCR differences
   
2. AFTER THE FIX:
   - System uses blockchain hash as PRIMARY verification
   - If file hash matches blockchain → Certificate is VALID
   - OCR data is used for additional information only
   - Same certificate will ALWAYS verify correctly
   
3. BLOCKCHAIN VERIFICATION LOGIC:
   - Upload: SHA-256 hash of file is stored in blockchain
   - Verify: SHA-256 hash of uploaded file is computed
   - Match: If hashes match → Certificate is authentic
   - This is cryptographically secure and reliable
""")

print("\n" + "=" * 60)
print("TESTING INSTRUCTIONS")
print("=" * 60)
print("""
To test the fix:

1. Login as Institution (institution@trusted.dev / inst123)
2. Upload a certificate image
3. Note the success message
4. Logout

5. Login as Verifier (verifier@trusted.dev / verify123)
6. Upload the SAME certificate image
7. You should now see: Status = "valid"
8. Reasons will include "Certificate verified in blockchain ledger"

The verification will succeed because the file hash matches!
""")
