import cv2

def preprocess(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # resize but keep aspect ratio
    img = cv2.resize(img, (300, 100))

    # LIGHT threshold (not inverted)
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    return img