import paho.mqtt.client as mqtt
import json
import os
import time

# Load configuration from JSON file
CONFIG_FILE = "/home/big_h/Desktop/steganographic_key_mgmt_project/config.json"

if not os.path.exists(CONFIG_FILE):
    print("[❌] Error: config.json not found!")
    exit(1)

with open(CONFIG_FILE, "r") as config_file:
    config = json.load(config_file)

# Extract configuration values
BROKER = config.get("broker", "localhost")
PORT = config.get("port", 1883)
TOPIC = config.get("topic", "iot/secure_channel")
IMAGE_PATH = config.get("image_path", "/home/big_h/Desktop/steganographic_key_mgmt_project/stego_image.jpg")

def send_image():
    # Ensure the image exists before sending
    if not os.path.exists(IMAGE_PATH):
        print(f"[❌] Error: Image file '{IMAGE_PATH}' not found!")
        return

    try:
        with open(IMAGE_PATH, "rb") as file:
            image_data = file.read()

        # Use updated MQTT API
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

        def on_connect(client, userdata, flags, rc, properties=None):
            if rc == 0:
                print(f"[✅] Successfully connected to MQTT Broker at {BROKER}:{PORT}")
            else:
                print(f"[⚠] Connection failed with code {rc}")

        client.on_connect = on_connect

        print(f"[🔄] Connecting to MQTT Broker at {BROKER}:{PORT}...")
        client.connect(BROKER, PORT, 60)

        print(f"[📤] Publishing image to topic '{TOPIC}'...")
        client.publish(TOPIC, image_data)

        # Ensure message is sent before disconnecting
        time.sleep(10)

        client.disconnect()
        print("[✅] Image sent successfully to Node-RED!")

    except Exception as e:
        print(f"[❌] Error: {e}")

if __name__ == "__main__":
    send_image()

