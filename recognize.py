from deepface import DeepFace
import os

result = DeepFace.find(
    img_path="test.jpg",
    db_path="dataset",
    enforce_detection=False
)

if len(result) > 0:
    match_path = result[0]['identity'][0]
    name = os.path.basename(match_path).split('.')[0]
    print("Recognized:", name)
else:
    print("No match found")