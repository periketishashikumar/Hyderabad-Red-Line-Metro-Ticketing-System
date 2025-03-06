import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize the QRCode detector
detector = cv2.QRCodeDetector()
d={'mail':'','from':'','to':''}
print("Point the camera at a QR Code.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Detect and decode
    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Code Data:", data)
        for k,v in zip(d,data.split(',')):
            d[k] = v.strip()
        print(d)
        break  # Exit after detecting a QR code

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
