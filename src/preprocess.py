import cv2

def preprocess(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # resize with aspect ratio
    h, w = img.shape
    new_w = 300
    new_h = int(h * (new_w / w))
    img = cv2.resize(img, (new_w, new_h))

    # light denoise (safe)
    img = cv2.GaussianBlur(img, (3, 3), 0)

    return img