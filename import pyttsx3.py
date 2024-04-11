import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askforfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for i in range(0 ,pages):
    page = pdfreader.getPage(i)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()