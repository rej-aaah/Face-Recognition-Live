import cv2
from deepface import DeepFace
import os

cap = cv2.VideoCapture(0)

THRESHOLD = 0.4  # adjust if needed

while True:
    ret, frame = cap.read()

    if not ret:
        break

    name = "Unknown"

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path="dataset",
            enforce_detection=False
        )

        if len(result) > 0 and len(result[0]) > 0:
            distance = result[0]['distance'][0]

            if distance < THRESHOLD:
                match_path = result[0]['identity'][0]

                # ✅ Get folder name (person name)
                name = os.path.basename(os.path.dirname(match_path))

    except:
        pass

    # Show name
    cv2.putText(frame, f"Name: {name}", (50, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    # Instructions
    cv2.putText(frame, "Press Q to Exit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 255), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()