import easyocr
from preprocess import preprocess
import cv2
import editdistance

# load OCR model (CRNN inside)
reader = easyocr.Reader(['en'])

def cer(pred, gt):
    return editdistance.eval(pred, gt) / len(gt)

# test image
img_path = "images\\TEST_0001.jpg"
#img_path = "images/your_handwriting.png"


# preprocess image
img = preprocess(img_path)

# save temp image for OCR
cv2.imwrite("temp.png", img)

# run OCR
result = reader.readtext("temp.png")

pred_text = " ".join([r[1] for r in result])

# ground truth (for demo)
gt_text = "kevin"
#gt_text = "what you actually wrote"

print("---------------------------------------")
print("------  Prediction:", pred_text)
print("------  Ground Truth:", gt_text)
print("------  CER:", cer(pred_text, gt_text))
print("---------------------------------------")