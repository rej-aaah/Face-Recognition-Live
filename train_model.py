import face_recognition
import os
import pickle

dataset_path = "dataset"

known_encodings = []
known_names = []

# Loop through each person folder
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_folder):
        continue

    print(f"Processing {person_name}...")

    # Loop through images
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        try:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(person_name)
            else:
                print(f"No face found in {image_name}")

        except Exception as e:
            print(f"Error processing {image_name}: {e}")

# Save encodings
data = {
    "encodings": known_encodings,
    "names": known_names
}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Training complete. Encodings saved.")