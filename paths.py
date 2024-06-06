import os
import pytesseract
current_dir = os.getcwd()

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

img_path = current_dir + '\\img'
output_img_path = current_dir + '\\img_output'
processed_img_path = current_dir + '\\img_processed'
text_path = current_dir + '\\text_output'
# Path to the Poppler binary files, Install https://github.com/oschwartz10612/poppler-windows/releases/tag/v24.02.0-0
poppler_path = r'C:\Program Files\Release-24.02.0-0\poppler-24.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'