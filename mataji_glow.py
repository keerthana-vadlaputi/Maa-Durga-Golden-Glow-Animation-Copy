
import cv2
import numpy as np
import math

# Load your golden Maa Durga artwork
image = cv2.imread("golden_durga.png.png")

if image is None:
    raise FileNotFoundError(
        "Keep golden_durga.png in the project folder."
    )

# Resize for your laptop screen
height, width = image.shape[:2]
scale = min(900 / width, 850 / height, 1.0)
width = int(width * scale)
height = int(height * scale)

image = cv2.imread("golden_durga.png.png")


# Keep the original black background
# and animate the golden artwork appearing.
window = "Maa Durga - Golden Glow Animation"
cv2.namedWindow(window, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window, width, height)

print("Maa Durga golden glow animation started!")
print("Press Q or ESC to close.")

try:
    # Reveal the artwork from top to bottom
    for y in range(1, height + 1, 4):
        frame = np.zeros_like(image)
        frame[:y, :] = image[:y, :]
        cv2.imshow(window, frame)

        key = cv2.waitKey(1) & 0xFF
        if key in (ord("q"), 27):
            raise KeyboardInterrupt

    # Gently pulse the golden glow
    while True:
        for t in range(120):
            # Subtle brightness pulse
            factor = 0.88 + 0.12 * (
                (1 + math.sin(t * 2 * math.pi / 60)) / 2
            )

            frame = np.clip(
                image.astype(np.float32) * factor,
                0, 255
            ).astype(np.uint8)

            cv2.imshow(window, frame)

            key = cv2.waitKey(30) & 0xFF
            if key in (ord("q"), 27):
                raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Animation closed.")

finally:
    cv2.destroyAllWindows()
