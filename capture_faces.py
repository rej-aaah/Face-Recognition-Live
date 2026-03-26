import cv2
import os

name = input("Enter person name: ")

dataset_path = os.path.join("dataset", name)

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

cap = None

# Try different camera backends
for backend in [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY]:
    for i in range(5):
        temp = cv2.VideoCapture(i, backend)
        if temp.isOpened():
            print(f"Camera opened with index {i} and backend {backend}")
            cap = temp
            break
    if cap:
        break

if cap is None:
    print("Unable to access camera")
    exit()

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame not received")
        break

    # Instructions on screen
    cv2.putText(frame, "Press C to Capture | Q to Quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):
        img_path = os.path.join(dataset_path, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Saved {img_path}")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()