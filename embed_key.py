import os

# Define file paths
IMAGE = "/home/big_h/Desktop/steganographic_key_mgmt_project/cover-image.jpg"
HIDDEN_TEXT = "/home/big_h/Desktop/steganographic_key_mgmt_project/super.txt"
OUTPUT_IMAGE = "/home/big_h/Desktop/steganographic_key_mgmt_project/stego_image.jpg"
PASSPHRASE = "1234"

def embed_data():
    """Embeds hidden text into an image using steghide."""
    
    # Check if required files exist before embedding
    if not os.path.exists(IMAGE):
        print(f"[❌] Error: Cover image '{IMAGE}' not found!")
        return
    
    if not os.path.exists(HIDDEN_TEXT):
        print(f"[❌] Error: Hidden text file '{HIDDEN_TEXT}' not found!")
        return
    
    print("[🔄] Embedding data into image...")
    
    # Run steghide embed command
    result = os.system(f"steghide embed -cf {IMAGE} -ef {HIDDEN_TEXT} -sf {OUTPUT_IMAGE} -p {PASSPHRASE} -f")
    
    # Check if embedding was successful
    if result == 0 and os.path.exists(OUTPUT_IMAGE):
        print(f"[✅] Data successfully embedded into '{OUTPUT_IMAGE}'")
    else:
        print("[❌] Embedding failed! Check your steghide setup.")

if __name__ == "__main__":
    embed_data()

