````markdown
# BunchOfProjects

```text
╔══════════════════════════════════════════════════════════╗
║              VIKTORIA.HB // PROJECT ARCHIVE              ║
║──────────────────────────────────────────────────────────║
║  STATUS       : ONLINE                                   ║
║  PURPOSE      : EXPERIMENTATION                          ║
║  PROJECTS     : VARIOUS                                  ║
║  QUALITY      : VARIABLE                                 ║
║  DOCUMENTATION: IN PROGRESS                              ║
╚══════════════════════════════════════════════════════════╝
```

A collection of personal projects, university exercises, experiments, repairs, and small things I built because I wanted to figure out how they work.

Some projects are polished.

Some are tiny experiments.

Some started as tutorials.

Some started because I had an idea and wanted to see if I could actually build it.

Some never made it past the "this seemed like a good idea" stage.

More projects and documentation will be added over time.

---

## `00 // PROJECT INDEX`

```text
SOFTWARE
[01] FIRST ADVENTURE GAME
[02] PDF TO MP3 CONVERTER
[03] HEART DRAWING WITH TURTLE
[04] IMPROVED HEART
[05] IT HELPDESK SIMULATOR

HARDWARE
[06] RETRO HARDWARE REPAIR LOG

DOCUMENTATION
[07] CODE ARCHIVE
[08] WHY THIS REPOSITORY EXISTS

PROJECT QUEUE
[09] CURRENT WORK
[10] FUTURE PROJECTS
[11] EXPERIMENTAL IDEAS
[12] PROJECT RULES
[13] PROJECT STATUS
```

---

## `01 // FIRST ADVENTURE GAME`

### Description

A small 2D adventure game developed with Godot and GDScript.

This was one of my first projects in Godot and was created with the help of Brackeys' "How to Make a Video Game in Godot" tutorial.

The project was mainly about getting familiar with Godot and understanding the fundamentals of 2D game development.

### Technologies Used

`Godot` `GDScript`

### Features

- Movement using WASD and arrow keys
- Coin collecting
- Coin counter at the end of the map
- One slime enemy

### Challenges

- Learning a completely new game engine after previously working with Unity
- Understanding the fundamentals of 2D game development
- Getting used to GDScript and Godot's workflow

### Status

```text
ENGINE       : GODOT
LANGUAGE     : GDSCRIPT
TYPE         : 2D GAME
STATUS       : EXPERIMENTAL
```

---

## `02 // PDF TO MP3 CONVERTER`

### Description

A Python script that converts text from PDF files into MP3 audio files, making it easier to listen to documents on the go.

The project was created as a small practical tool while learning Python and working with external libraries.

### Technologies Used

`Python` `PyPDF2` `pyttsx3`

### Features

- Extract text from PDF files
- Convert extracted text into speech audio
- Save generated audio as an MP3 file
- Simple command-line interface

### Challenges

- Handling PDF text extraction
- Dealing with different text formatting inside PDF documents
- Producing clear and accurate text-to-speech output
- Working with external Python libraries

### Status

```text
LANGUAGE     : PYTHON
TYPE         : UTILITY
INTERFACE    : COMMAND LINE
STATUS       : FUNCTIONAL
```

---

## `03 // HEART DRAWING WITH TURTLE`

### Description

A small Python experiment using the Turtle graphics library to draw a heart and display a custom message.

This started as a simple exercise in programmatic drawing and eventually turned into an experiment with positioning, curves, and Turtle's drawing functions.

### Technologies Used

`Python` `Turtle`

### Features

- Draws a heart using Turtle graphics
- Displays a custom message inside the heart
- Uses functions to structure the drawing process

### Files

- `Heart.py` - Draws a heart with a custom message
- `Improved Heart.py` - An alternative implementation using mathematical functions

### Challenges

- Fine-tuning Turtle movements to create a smooth heart shape
- Positioning text inside the graphic
- Understanding how small changes in movement affect the final shape

### Status

```text
LANGUAGE     : PYTHON
LIBRARY      : TURTLE
TYPE         : GRAPHICS EXPERIMENT
STATUS       : COMPLETE
```

---

## `04 // IMPROVED HEART`

### Description

A second version of the heart drawing experiment using mathematical functions to generate the shape.

Instead of manually defining the curves, this version uses trigonometric functions to calculate the coordinates of the heart.

### Technologies Used

`Python` `Math` `Turtle`

### How It Works

The heart is generated using parametric equations:

```python
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (
        12 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )
```

The calculated coordinates are then used to draw the shape.

### Status

```text
LANGUAGE     : PYTHON
TYPE         : MATHEMATICAL GRAPHICS
STATUS       : EXPERIMENTAL
```

---

## `05 // IT HELPDESK SIMULATOR`

### Description

A Roblox game currently in development, built around the idea of turning IT support into a game.

The goal is to create a fun and somewhat chaotic IT Helpdesk Simulator where players can deal with support requests, troubleshoot problems, manage technology, and experience the kinds of situations that make IT support interesting.

It's still very much a work in progress, so the exact mechanics and features are evolving as development continues.

### Current Focus

- Learning Roblox Studio and Lua
- Designing the game's core systems
- Creating IT support scenarios
- Experimenting with gameplay and progression
- Building the game's infrastructure and documentation
- Finding ways to make IT concepts entertaining rather than just educational

### Status

```text
ENGINE       : ROBLOX
LANGUAGE     : LUA
TYPE         : SIMULATION / MANAGEMENT
STATUS       : IN DEVELOPMENT
CURRENT TASK : MAKING IT SUPPORT FUN
```

The project is intended to become a fun IT Helpdesk Simulator rather than a serious IT training application.

Because apparently the natural response to working in IT is to make a game about working in IT.

---

## `06 // RETRO HARDWARE REPAIR LOG`

Not all of my projects live in a code editor.

I also enjoy taking apart, troubleshooting, repairing, modifying, and restoring older hardware.

I've already worked on a variety of consoles and other electronics, including:

```text
NINTENDO
├── 2DS                         [REPAIRED]
├── 3DS                         [REPAIRED]
├── Wii                         [REPAIRED]
└── Switch                      [REPAIRED]

SONY
├── PS4                         [REPAIRED]
├── PSP                         [PLANNED]
├── PS Vita                     [PLANNED]
└── Walkman                     [IN PROGRESS]

OTHER
└── Game Controllers            [REPAIRED]
```

The Walkman is currently sitting open on my desk while I work through its repair.

The repairs I've done so far have involved things such as troubleshooting, cleaning, disassembly, component replacement, testing, and figuring out why something that should work very much does not.

Some of these repairs are already completed, but the detailed documentation has not made its way onto GitHub yet.

That is one of the things I want to change.

### Hardware Documentation Queue

```text
[UNDOCUMENTED]  2DS
[UNDOCUMENTED]  3DS
[UNDOCUMENTED]  Wii
[UNDOCUMENTED]  Switch
[UNDOCUMENTED]  PS4
[UNDOCUMENTED]  Controllers
[IN PROGRESS]   Sony Walkman
```

The goal is not simply to make old hardware work again.

It's to understand what failed, why it failed, and how to bring it back to working condition.

---

## `07 // CODE ARCHIVE`

Some of the original project code is kept here because the code itself is part of the learning process.

### `PDFtoMP3.py`

A Python program for extracting text from PDF files and converting it into speech audio.

```python
from PyPDF2 import PdfReader
import PyPDF2
import pyttsx3

path = open(r"C:File Path", "rb")
pdfreader = PyPDF2.PdfReader(path)
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)

speaker.save_to_file(clean_text, "story.mp3")
speaker.runAndWait()

speaker.stop()
```

---

### `Heart.py`

A Python program using Turtle graphics to draw a heart and display a custom message.

```python
import turtle

# Creating a turtle object (pen)
pen = turtle.Turtle()

# Defining a method to draw a curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# Defining a method to draw a full heart
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

# Defining a method to write text
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color("lightgreen")
    pen.write(
        "Astarion, my beloved",
        font=("Verdana", 12, "bold")
    )

# Draw a heart
heart()

# Write text
txt()

# Hide turtle
pen.ht()
```

---

### `Improved Heart.py`

An alternative implementation using mathematical functions to generate the heart shape.

```python
import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (
        12 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )

speed(1000)
bgcolor("black")

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(5):
        color("red")
    goto(0, 0)

done()
```

---

## `08 // WHY THIS REPOSITORY EXISTS`

Not every project needs to become a polished application.

Some projects exist because I wanted to learn something.

Some exist because a university assignment gave me a reason to try something.

Some are experiments.

Some are prototypes.

Some are repairs.

Some are simply me asking:

> "Can I make this?"

Or, in the case of hardware:

> "Why is this thing broken?"

This repository is where those projects can live.

I also want to keep some of the older projects around instead of hiding them once I've learned something more advanced. They show where I started and how my approach to programming, troubleshooting, and technology changes over time.

---

## `09 // CURRENT WORK`

Things that are currently taking up space on my desk, in my laptop, or somewhere inside a virtual machine.

```text
C:\VIKTORIA\PROJECTS> queue

[IN PROGRESS]   ROBLOX IT HELPDESK SIMULATOR
[IN PROGRESS]   SONY WALKMAN REPAIR
[IN PROGRESS]   OLD LAPTOP HOMELAB

[LEARNING]      KUBERNETES HOMELAB
[LEARNING]      CONTAINER EXPERIMENTS

[DONE]          SELF-HOSTED SERVICES
[DONE]          NETWORK / MONITORING EXPERIMENTS

C:\VIKTORIA\PROJECTS> _
```

---

## `10 // FUTURE PROJECTS`

Things I want to build, repair, experiment with, or learn more about.

```text
[PLANNED]       PSP REPAIR / MODIFICATION
[PLANNED]       PS VITA REPAIR / MODIFICATION

[PLANNED]       EXPAND THE OLD LAPTOP HOMELAB
[PLANNED]       MORE SELF-HOSTED SERVICES
[PLANNED]       NETWORK EXPERIMENTS
[PLANNED]       MONITORING PROJECTS

[PLANNED]       HARDWARE INVENTORY SYSTEM
[PLANNED]       PERSONAL MONITORING DASHBOARD
[PLANNED]       OLD HARDWARE REVIVAL PROJECT

[IDEA]          SOMETHING INVOLVING TOO MANY VIRTUAL MACHINES
[IDEA]          SOMETHING THAT PROBABLY SHOULD NOT BE RUN ON AN OLD LAPTOP
```

The list will probably change.

Some projects will move from `PLANNED` to `DONE`.

Some will be abandoned.

Some will turn into something completely different.

That's fine.

---

## `11 // EXPERIMENTAL IDEAS`

Not everything in the project queue has to be serious.

Some ideas are here because they sound fun.

### Hardware Inventory System

A small application for keeping track of old hardware, including:

- Device
- Model
- Condition
- Repair status
- Parts needed
- Purchase price
- Repair cost
- Notes
- Photos

Essentially a database for all the things that somehow ended up on my desk.

### Old Hardware Revival

Find an old laptop, PC, or other piece of hardware and see how far it can be brought back to life.

```text
OLD HARDWARE
      |
      v
  DIAGNOSIS
      |
      v
    REPAIR
      |
      v
   LINUX?
      |
      v
  SELF-HOSTED
   SERVICE
      |
      v
"WHY IS THIS
 ACTUALLY WORKING?"
```

### Personal Infrastructure Lab

Build a small isolated environment for experimenting with:

`Linux` `Docker` `Virtual Machines` `Networking` `Monitoring` `Security`

The goal would be to break things safely, document what happened, and learn how to fix them.

### Kubernetes Homelab

Continue learning Kubernetes by gradually expanding from a small experimental cluster into something more useful.

Possible areas to explore:

- Kubernetes fundamentals
- Container networking
- Services and deployments
- Persistent storage
- Ingress
- Monitoring
- Container orchestration

This is a learning project rather than a claim of Kubernetes expertise.

### The Questionable Project

Every project archive needs one.

The details are currently classified.

```text
PROJECT: ????
STATUS : QUESTIONABLE
PURPOSE: UNKNOWN
RISK   : PROBABLY FINE
```

---

## `12 // PROJECT RULES`

```text
RULE 01  - Learn something.
RULE 02  - Break something.
RULE 03  - Figure out why it broke.
RULE 04  - Document it.
RULE 05  - Try not to break the same thing twice.
RULE 06  - If it works, find out why.
RULE 07  - If it doesn't work, investigate.
RULE 08  - "I'll fix it later" is not documentation.
```

Projects may change, disappear, get abandoned, or turn into something completely different.

That's fine.

This repository is about learning and experimenting, not maintaining a perfect record of finished products.

---

## `13 // PROJECT STATUS`

```text
┌──────────────────────────────────────────────────────────┐
│ VIKTORIA.HB // PROJECT ARCHIVE STATUS                    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  SOFTWARE              .......... ACTIVE                 │
│  HARDWARE              .......... ACTIVE                 │
│  REPAIRS               .......... ONGOING                │
│  EXPERIMENTS           .......... ONGOING                │
│  DOCUMENTATION         .......... IMPROVING              │
│  IDEAS                 .......... ACCUMULATING           │
│  BROKEN THINGS         .......... EXPECTED               │
│  COFFEE                .......... REQUIRED               │
│                                                          │
└──────────────────────────────────────────────────────────┘

C:\VIKTORIA\PROJECTS> _
```

More projects will be added as I build, experiment, learn, repair, and inevitably break a few things along the way.

```text
END OF ARCHIVE
```
````
