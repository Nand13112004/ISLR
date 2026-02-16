import os
import cv2
import numpy as np
from keras.models import load_model
from sklearn.metrics import confusion_matrix, classification_report

# ---------------- SETTINGS ----------------
MODEL_PATH = 'cnn8grps_rad1_model.h5'
DATASET_PATH = 'AtoZ_3.1'
IMG_SIZE = 400
# ------------------------------------------

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print("Loading model...")
model = load_model(MODEL_PATH)
print("Model loaded successfully.\n")

group_dict = {
    'A': 0, 'E': 0, 'M': 0, 'N': 0, 'S': 0, 'T': 0,
    'B': 1, 'F': 1, 'D': 1, 'I': 1, 'U': 1, 'V': 1, 'W': 1, 'K': 1, 'R': 1,
    'C': 2, 'O': 2,
    'G': 3, 'H': 3,
    'L': 4,
    'P': 5, 'Q': 5, 'Z': 5,
    'X': 6,
    'Y': 7, 'J': 7
}

total = 0
correct = 0

y_true = []
y_pred = []

print("Evaluating test dataset...\n")

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    folder = os.path.join(DATASET_PATH, letter)
    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):
        if file.endswith('.jpg'):
            img_path = os.path.join(folder, file)
            img = cv2.imread(img_path)

            if img is None:
                continue

            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img.astype(np.float32) / 255.0
            img = img.reshape(1, IMG_SIZE, IMG_SIZE, 3)

            prediction = model.predict(img, verbose=0)
            pred_group = np.argmax(prediction)

            true_group = group_dict[letter]

            if pred_group == true_group:
                correct += 1

            y_true.append(true_group)
            y_pred.append(pred_group)
            total += 1

            if total % 500 == 0:
                print(f"Processed {total} images...")

accuracy = (correct / total) * 100

print("\n================ FINAL RESULTS ================")
print(f"Test Accuracy: {accuracy:.2f}%")
print(f"Total Test Samples: {total}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))

print("\nClassification Report:")
print(classification_report(y_true, y_pred))
print("==============================================")
