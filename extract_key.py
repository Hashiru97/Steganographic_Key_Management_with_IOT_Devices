import os
import json

# Load configuration
CONFIG_FILE = "/home/big_h/Desktop/steganographic_key_mgmt_project/config.json"

try:
    with open(CONFIG_FILE, "r") as config_file:
        config = json.load(config_file)
        PASSPHRASE = config.get("1234", "1234")  # Default to "1234" if not found
except Exception as e:
    print(f"[⚠] Warning: Could not load config.json ({e}), using default passphrase.")
    PASSPHRASE = "1234"

STEGO_IMAGE = "/home/big_h/Desktop/steganographic_key_mgmt_project/received_image.jpg"
OUTPUT_TEXT = "/home/big_h/Desktop/steganographic_key_mgmt_project/extracted.txt"

def extract_data():
    """Extracts hidden data from a steganographic image using steghide."""
    
    # Ensure the stego image exists before attempting extraction
    if not os.path.exists(STEGO_IMAGE):
        print(f"[❌] Error: Stego image '{STEGO_IMAGE}' not found!")
        return
    
    print("[🔄] Extracting hidden data...")
    
    # Run steghide extract command
    result = os.system(f"steghide extract -sf {STEGO_IMAGE} -xf {OUTPUT_TEXT} -p {PASSPHRASE} -f")
    
    # Check if extraction was successful
    if result == 0 and os.path.exists(OUTPUT_TEXT):
        print(f"[✅] Data extracted successfully! Check '{OUTPUT_TEXT}'")
        
        # Display the extracted message
        with open(OUTPUT_TEXT, "r") as file:
            hidden_message = file.read().strip()
            print(f"[📜] Extracted Message: {hidden_message}")
    else:
        print("[❌] Extraction failed! Wrong passphrase or no hidden data.")

if __name__ == "__main__":
    extract_data()

