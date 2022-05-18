# -*- coding: utf-8 -*-
"""
Text Extractor from Udemy Certificates
Created to extract the Certificate number & Certificate URL as they come in a image saved as pdf
@author: pedri
"""
import pytesseract
from pdf2image import convert_from_path
import os
import easygui as eg

# Poppler path location
pppath = r'C:\Program Files\poppler-22.04.0\Library\bin'

# Pytesseract path location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Choice function to select certificate file

def Choice():
    print("Select certificate file \n")
    global file
    file = eg.fileopenbox(filetypes=['*.pdf']) #easygui module
    print("Selected file path: "+file+'\n')
    
    if file[-3::] == 'pdf': # reads the last 3 characters from file name
        PDF()
        
    elif file[-3::] == 'jpg':
        JPG()
   
# Function to convert the .pdf to .png so it can be read by pytesseract
def Conversion():
    
    converted = convert_from_path(file, single_file=True, poppler_path = pppath)
    
    # Saves a temporary image file 
    
    for page in converted:
        page.save('temp.png', 'PNG')

# In case of .pdf file
def PDF():
    
    Conversion()    
    
    data = (pytesseract.image_to_string('temp.png')) # Reads the temporary image
    
    ds = data.split('\n')
    
    print(ds[0])
    print(ds[2])
    
    os.remove('temp.png') # Deletes temporary image

# In case of .jpg file - there is no need to create a temp file, so it can be read directly
def JPG():
    data = (pytesseract.image_to_string(file))
    
    ds = data.split('\n')
    
    print(ds[0])
    print(ds[2])
 
# Run the main function:    
Choice()