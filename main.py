import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

# Background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=False
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip for mirror view
    frame = cv2.flip(frame, 1)

    # Create foreground mask
    mask = bg_subtractor.apply(frame)

    # Remove noise
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Extract foreground
    foreground = cv2.bitwise_and(frame, frame, mask=mask)

    # White background
    white_bg = np.full(frame.shape, 255, dtype=np.uint8)

    # Invert mask
    inv_mask = cv2.bitwise_not(mask)

    # Background area
    background = cv2.bitwise_and(white_bg, white_bg, mask=inv_mask)

    # Final output
    final = cv2.add(foreground, background)

    # Show windows
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Background Removed", final)

    # Press ESC to quit
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
