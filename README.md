# Udemy-Certificate-Code-Reader

This project was born after i completed a Udemy course and got the certificate. To my surprise, the PDF is just a image converted instead of text. The fast solution would have been to just type the certified number and link into Notepad and move on. Instead, i built this script in Python to automate the reading for me.

This project was first tried using a module like PyPDF2, but the pdf file from Udemy doesn't have the readable text to extract. Instead, it is opened using the easygui module to copy its path, which will be used in pdf2image module to create a temporary image file that can be read in Pytesseract.
