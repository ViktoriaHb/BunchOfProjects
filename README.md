# BunchOfProjects

---

# My Projects Portfolio

Here are several projects I have developed both privately and during my time at university, showcasing my coding skills and technical expertise. Im going to add more porjects with time.

## PDF to MP3 Converter

**Description:**
A Python script that converts text from PDF files into MP3 audio files, making it easier to listen to documents on the go.

**Technologies Used:**
- **Programming Language:** Python
- **Libraries:** PyPDF2 for reading PDF files, pyttsx3 for text-to-speech conversion

**Features:**
- Extract text from PDF files
- Convert extracted text to MP3 audio files
- Simple command-line interface for ease of use

**Challenges Overcome:**
- Handled various PDF text extraction issues
- Ensured clear and accurate text-to-speech conversion

## Heart Drawing with Turtle Graphics

**Description:**
A Python program that uses the Turtle graphics library to draw a heart shape and display a custom message, showcasing creative coding skills.

**Technologies Used:**
- **Programming Language:** Python
- **Library:** Turtle

**Features:**
- Draws a heart shape using Turtle

graphics
- Displays a custom message within the heart

**Files:**
- `Heart.py`: Draws a heart with a custom message
- `Improved Heart.py`: Another version of the heart drawing with a different implementation

**Challenges Overcome:**
- Fine-tuned the turtle movements to create a smooth heart shape
- Managed text positioning within the graphic

---

## Project Details

### PDFtoMP3.py

**Description:**
A python program to convert text from PDF files into MP3 audio files

**Code Overview:**
```python
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
```

### Heart.py

**Description:**
A Python program that uses the Turtle graphics library to draw a heart shape and display a custom message.

**Code Overview:**
```python
import turtle

# Creating a turtle object(pen) 
pen = turtle.Turtle() 

# Defining a method to draw curve 
def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 

# Defining method to draw a full heart 
def heart(): 
    pen.fillcolor('red') 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120) 
    curve() 
    pen.forward(112) 
    pen.end_fill() 

# Defining method to write text 
def txt(): 
    pen.up() 
    pen.setpos(-68, 95) 
    pen.down() 
    pen.color('lightgreen') 
    pen.write("Astarion, my beloved", font=("Verdana", 12, "bold")) 

# Draw a heart 
heart() 

# Write text 
txt() 

# To hide turtle 
pen.ht()
```

### Improved Heart.py

**Description:**
An improved version of the heart drawing script with a different approach to draw the heart shape using mathematical functions.

**Code Overview:**
```python
import math
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed(1000)
bgcolor("black")

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(5):
        color("red")
    goto(0, 0)
done()
```

