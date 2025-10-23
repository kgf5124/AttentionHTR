import os
import csv

# Path to the Greek dataset folder
DATA_DIR = "datasets/Query"
OUTPUT_FILE = "datasets/greek_gcdb_labels.txt"

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    for label_folder in os.listdir(DATA_DIR):
        label_path = os.path.join(DATA_DIR, label_folder)
        if not os.path.isdir(label_path):
            continue
        for img_file in os.listdir(label_path):
            if img_file.endswith((".png", ".jpg", ".jpeg")):
                img_path = os.path.join(label_path, img_file)
                writer.writerow([img_path, label_folder])

print(f"Labels file created at {OUTPUT_FILE}")

