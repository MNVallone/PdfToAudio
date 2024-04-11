import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

for i in range(0 ,pages):
    page = pdfreader.pages[i]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()