from PIL import Image
import pytesseract
t = pytesseract.image_to_string(Image.open("45.jpg"),lang="eng")
print(t)
