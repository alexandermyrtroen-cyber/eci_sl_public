import os
import time
import json
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

INCOMING_DIR = "/home/alexander/ECI_NEXUS/incoming_payloads"
PROCESSED_DIR = "/home/alexander/ECI_NEXUS/processed_payloads"
ERROR_DIR = "/home/alexander/ECI_NEXUS/error_payloads"
OUTPUT_DIR = "/home/alexander/ECI_NEXUS/projects/eci_sl_public"

os.makedirs(INCOMING_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(ERROR_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

REQUIRED_FIELDS = ["certificate_id", "issuer", "beneficiary", "amount", "currency"]

def validate_payload(data):
    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, "Valid"

def generate_certificate(data):
    payload_str = json.dumps(data, sort_keys=True)
    sha256_hash = hashlib.sha256(payload_str.encode('utf-8')).hexdigest()
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>ECI Sovereign Certificate - {data.get('certificate_id')}</title>
    <style>
        body {{ font-family: monospace; background: #0f172a; color: #f8fafc; padding: 40px; }}
        .card {{ background: #1e293b; border: 1px solid #334155; padding: 30px; border-radius: 8px; max-width: 800px; margin: auto; }}
        h1 {{ color: #38bdf8; font-size: 24px; border-bottom: 1px solid #334155; padding-bottom: 10px; }}
        .meta {{ margin: 15px 0; font-size: 14px; color: #94a3b8; }}
        .hash {{ background: #0f172a; padding: 10px; border: 1px solid #475569; word-break: break-all; font-size: 12px; color: #34d399; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>ECI Sovereign Trade Finance Certificate</h1>
        <div class="meta">
            <p><strong>Certificate ID:</strong> {data.get('certificate_id')}</p>
            <p><strong>Issuer:</strong> {data.get('issuer')}</p>
            <p><strong>Beneficiary:</strong> {data.get('beneficiary')}</p>
            <p><strong>Amount:</strong> {data.get('amount')} {data.get('currency')}</p>
        </div>
        <p><strong>Cryptographic Verification Hash (SHA-256):</strong></p>
        <div class="hash">{sha256_hash}</div>
    </div>
</body>
</html>"""
    
    filename = f"cert_{data.get('certificate_id')}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w") as f:
        f.write(html_content)
    return filepath, sha256_hash

def process_payloads():
    print("ECI Watch Daemon active. Monitoring incoming payloads...", flush=True)
    while True:
        try:
            files = os.listdir(INCOMING_DIR)
            for filename in files:
                if filename.endswith(".json"):
                    file_path = os.path.join(INCOMING_DIR, filename)
                    time.sleep(0.1)
                    
                    with open(file_path, "r") as f:
                        try:
                            data = json.load(f)
                        except json.JSONDecodeError as e:
                            print(f"Error parsing JSON in {filename}: {e}", flush=True)
                            os.rename(file_path, os.path.join(ERROR_DIR, filename))
                            continue
                            
                    is_valid, msg = validate_payload(data)
                    if not is_valid:
                        print(f"Validation failed for {filename}: {msg}", flush=True)
                        os.rename(file_path, os.path.join(ERROR_DIR, filename))
                        continue
                        
                    cert_path, hash_val = generate_certificate(data)
                    print(f"Generated certificate for {filename} | Hash: {hash_val[:16]}...", flush=True)
                    
                    os.rename(file_path, os.path.join(PROCESSED_DIR, filename))
        except Exception as e:
            print(f"Daemon execution error: {e}", flush=True)
        time.sleep(2)

if __name__ == "__main__":
    process_payloads()
