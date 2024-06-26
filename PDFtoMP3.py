from PyPDF2 import PdfReader
import PyPDF2
import pyttsx3

path = open(r"C:File Path","rb")
pdfreader = PyPDF2.PdfReader(path)
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n"," ")
    print(clean_text)

speaker.save_to_file(clean_text, "story.mp3")
speaker.runAndWait()

speaker.stop()