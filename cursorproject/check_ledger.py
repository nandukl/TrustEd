import json
import os
import sys

# Fix encoding for Windows console
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

ledger_path = "backend/db/ledger.txt"

print("=" * 80)
print("BLOCKCHAIN LEDGER ANALYSIS")
print("=" * 80)

if not os.path.exists(ledger_path):
    print(f"\n[ERROR] Ledger file does not exist: {ledger_path}")
    exit(1)

print(f"\n[OK] Ledger file exists: {ledger_path}")
print(f"File size: {os.path.getsize(ledger_path)} bytes\n")

with open(ledger_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines in ledger: {len(lines)}\n")
print("=" * 80)
print("CERTIFICATE HASHES IN BLOCKCHAIN:")
print("=" * 80)

cert_count = 0
for i, line in enumerate(lines, 1):
    line = line.strip()
    if not line:
        continue
    
    try:
        block = json.loads(line)
        
        # Check if this is a certificate block (has certificate_data)
        if "certificate_data" in block:
            cert_count += 1
            cert_hash = block.get("certificate_file_hash", "N/A")
            cert_data = block.get("certificate_data", {})
            
            print(f"\n[CERT #{cert_count}] Line {i}:")
            print(f"   Student: {cert_data.get('student_name', 'N/A')}")
            print(f"   Institution: {cert_data.get('institution_name', 'N/A')}")
            print(f"   Year: {cert_data.get('year', 'N/A')}")
            print(f"   Certificate ID: {cert_data.get('certificate_id', 'N/A')}")
            print(f"   File Hash: {cert_hash}")
            print(f"   Uploaded by: {cert_data.get('uploaded_by', 'N/A')}")
            print(f"   Upload date: {cert_data.get('upload_date', 'N/A')}")
    except json.JSONDecodeError as e:
        print(f"\n[ERROR] Parsing line {i}: {e}")
        print(f"   Line content: {line[:100]}...")

print("\n" + "=" * 80)
print(f"SUMMARY: Found {cert_count} certificates in blockchain")
print("=" * 80)

# Now let's check what hash you're trying to verify
print("\n\nYOUR CERTIFICATE HASH FROM SCREENSHOT:")
print("6b9d79949909ff2d8ec1ff40b38c2e9308cd86dd4d10d1363f08405dd54ee9e")
print("\nSearching for this hash in the ledger...")

target_hash = "6b9d79949909ff2d8ec1ff40b38c2e9308cd86dd4d10d1363f08405dd54ee9e"
found = False

with open(ledger_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        
        try:
            block = json.loads(line)
            block_hash = block.get("certificate_file_hash", "")
            
            if block_hash == target_hash:
                print(f"\n[FOUND!] Hash exists on line {i}")
                print(f"Certificate data: {json.dumps(block.get('certificate_data', {}), indent=2)}")
                found = True
                break
        except:
            pass

if not found:
    print(f"\n[NOT FOUND!] This hash does not exist in the blockchain ledger.")
    print("\nPossible reasons:")
    print("1. The certificate was not uploaded successfully")
    print("2. The ledger file was cleared or reset")
    print("3. There's a mismatch in how the hash is being computed")
