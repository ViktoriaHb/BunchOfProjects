# BunchOfProjects

```text
╔══════════════════════════════════════════════════╗
║           VIKTORIA.HB // PROJECT ARCHIVE         ║
║──────────────────────────────────────────────────║
║  STATUS        : ONLINE                          ║
║  PURPOSE       : EXPERIMENTATION                 ║
║  PROJECTS      : VARIOUS                         ║
║  REPAIRS       : ONGOING                         ║
║  DOCUMENTATION : IN PROGRESS                     ║
╚══════════════════════════════════════════════════╝
```

A collection of personal projects, university exercises, experiments, repairs, and various things I built because I wanted to know how they worked.

Some started as tutorials.

Some started as university exercises.

Some started because I had an idea at an inconvenient time.

Some involved considerably more debugging than originally planned.

Some are here simply because I thought:

> "I wonder if I can build this."

And some started with a broken piece of hardware sitting on my desk.

More projects and documentation will be added over time.

---

## `00 // PROJECT INDEX`

| Project | Type | Status |
|---|---|---|
| First Adventure Game | Game Development | Complete |
| PDF to MP3 Converter | Python / Utility | Complete |
| Heart Drawing | Python / Graphics | Complete |
| Improved Heart | Python / Graphics | Complete |
| IT Helpdesk Simulator | Roblox / Game Development | In Development |
| Retro Hardware Repair | Hardware | Ongoing |

---

## `01 // FIRST ADVENTURE GAME`

A small 2D adventure game developed with Godot and GDScript.

This was one of my first projects in Godot and was created with the help of Brackeys' "How to Make a Video Game in Godot" tutorial.

The project was mainly about getting familiar with Godot and understanding the fundamentals of 2D game development.

### Technologies

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

**Complete**

---

## `02 // PDF TO MP3 CONVERTER`

A Python tool that extracts text from PDF files and converts it into speech audio.

The project was created as a small practical utility while learning Python and experimenting with external libraries.

### Technologies

`Python` `PyPDF2` `pyttsx3`

### Features

- Extract text from PDF files
- Convert extracted text into speech audio
- Save generated audio as an MP3 file
- Simple command-line interface

### Challenges

- Handling PDF text extraction
- Dealing with different text formatting inside PDF documents
- Producing clear text-to-speech output
- Working with external Python libraries

### Status

**Complete**

---

## `03 // HEART DRAWING`

A small Python experiment using Turtle graphics to draw a heart and display a custom message.

It started as a simple exercise and turned into an experiment with positioning, curves, and programmatic drawing.

### Technologies

`Python` `Turtle`

### Features

- Draws a heart using Turtle graphics
- Displays a custom message
- Uses functions to structure the drawing process

### Files

- `Heart.py`
- `Improved Heart.py`

### Status

**Complete**

---

## `04 // IMPROVED HEART`

An alternative version of the heart drawing experiment using mathematical functions to generate the shape.

Instead of manually defining the curves, this version uses trigonometric functions to calculate the coordinates.

### Technologies

`Python` `Math` `Turtle`

### What I Experimented With

- Parametric equations
- Trigonometric functions
- Coordinate systems
- Programmatic drawing

### Status

**Complete**

---

## `05 // IT HELPDESK SIMULATOR`

A Roblox game currently in development.

The idea is to turn IT support into a fun simulation where players deal with support requests, troubleshoot problems, manage technology, and experience the chaos of working in IT.

The game is still in development, so the mechanics and features are likely to change.

### Current Focus

- Learning Roblox Studio and Lua
- Designing the game's core systems
- Creating IT support scenarios
- Experimenting with gameplay and progression
- Building the game's systems and documentation

### Technologies

`Roblox Studio` `Lua`

### Status

**In Development**

> Apparently the natural response to working in IT is to make a game about working in IT.

---

## `06 // RETRO HARDWARE REPAIR`

Not all of my projects live in a code editor.

I also enjoy taking apart, troubleshooting, repairing, modifying, and restoring older hardware.

So far I've repaired or worked on a variety of consoles and electronics.

### Repaired

- Nintendo 2DS
- Nintendo 3DS
- Nintendo Wii
- Nintendo Switch
- Sony PS4
- Game controllers

### Currently Working On

- Sony Walkman

The Walkman is currently sitting open on my desk while I work through its repair.

### Planned

- Sony PSP
- PlayStation Vita
- More retro consoles
- More electronics

The repairs involve troubleshooting, cleaning, disassembly, component replacement, testing, and figuring out why something that should work very much does not.

Some of these repairs are already completed, but the detailed documentation has not made its way onto GitHub yet.

That's something I want to change.

### What I Like About Hardware Repair

There is something particularly satisfying about taking a device that has been sitting unused for years, figuring out what failed, repairing it, and seeing it work again.

It combines:

`Electronics` `Hardware` `Software` `Troubleshooting` `Patience`

And occasionally a little detective work.

Sometimes the problem is obvious.

Sometimes it is a tiny component hiding somewhere on a board.

And sometimes the solution is, unfortunately:

> "Have you tried turning it off and on again?"

---

## `07 // CODE ARCHIVE`

Some of the original project code is kept here because the code itself is part of the learning process.

### `PDFtoMP3.py`

A Python program for extracting text from PDF files and converting it into speech audio.

```python
from PyPDF2 import PdfReader
import pyttsx3

reader = PdfReader("example.pdf")
speaker = pyttsx3.init()

for page in reader.pages:
    text = page.extract_text()

    if text:
        print(text)

speaker.save_to_file(text, "story.mp3")
speaker.runAndWait()
speaker.stop()
```

---

### `Heart.py`

A Python program using Turtle graphics to draw a heart and display a custom message.

```python
import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

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

def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color("lightgreen")
    pen.write(
        "Astarion, my beloved",
        font=("Verdana", 12, "bold")
    )

heart()
txt()

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
    goto(0, 0)

done()
```

---

## `08 // CURRENT WORK`

Things currently taking up space on my desk, laptop, or somewhere inside a virtual machine.

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

## `09 // FUTURE PROJECTS`

There are always more things I want to build, repair, or experiment with.

### Retro Hardware

- PSP repair and modification
- PS Vita repair and modification
- More console repairs
- More controller repairs
- Hardware restoration documentation

### Old Laptop Homelab

I have an older laptop that I want to turn into a small playground for IT experiments.

Possible uses include:

- Linux
- Docker
- Self-hosted services
- Monitoring
- Networking experiments
- Virtual machines
- Security experiments
- Small infrastructure projects

The exact purpose will probably evolve once I start throwing things at it.

### Hardware Inventory System

A small application for keeping track of old hardware.

Possible information:

- Device
- Model
- Condition
- Repair status
- Parts needed
- Purchase price
- Repair cost
- Photos
- Notes

Essentially a database for all the things that somehow ended up on my desk.

### Personal Monitoring Dashboard

A small dashboard combining information from different services and systems.

Possible technologies:

`Grafana` `Prometheus` `Uptime Kuma` `Docker`

The goal would be to have one place where I can see what is happening across my little collection of machines and services.

### Old Hardware Revival

Take an old laptop or PC and see how far it can be brought back to life.

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

### Kubernetes Homelab

Continue learning Kubernetes by gradually expanding my small experimental cluster.

This is currently a learning project rather than a claim of Kubernetes expertise.

Possible areas to explore:

- Deployments
- Services
- Networking
- Persistent storage
- Ingress
- Monitoring
- Container orchestration

---

## `10 // EXPERIMENTAL IDEAS`

Not every idea needs to become a serious project.

Some things are interesting simply because I want to see if I can make them work.

### Personal IT Lab

A small isolated environment where I can experiment with:

`Linux` `Docker` `Virtual Machines` `Networking` `Monitoring` `Security`

The basic idea:

```text
BREAK IT
   |
   v
FIND OUT WHY
   |
   v
FIX IT
   |
   v
DOCUMENT IT
   |
   v
BREAK SOMETHING ELSE
```

### Old Hardware Server

Take an old laptop or PC and turn it into something genuinely useful.

Maybe a server.

Maybe a monitoring system.

Maybe a collection of containers.

Maybe all of the above.

### Too Many Virtual Machines

Because apparently having one virtual machine is not enough.

```text
VM 01
 |
 +-- VM 02
      |
      +-- VM 03
           |
           +-- "This was a bad idea."
```

**Status:** Idea

---

## `11 // WHY THIS REPOSITORY EXISTS`

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

I also want to keep some of the older projects around instead of hiding them once I've learned something more advanced.

They show where I started, what I experimented with, and how my approach to programming and technology changes over time.

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

---

## `13 // PROJECT STATUS`

```text
┌──────────────────────────────────────────────────┐
│ VIKTORIA.HB // PROJECT ARCHIVE STATUS            │
├──────────────────────────────────────────────────┤
│                                                  │
│  SOFTWARE          .......... ACTIVE             │
│  HARDWARE          .......... ACTIVE             │
│  REPAIRS           .......... ONGOING            │
│  EXPERIMENTS       .......... ONGOING            │
│  DOCUMENTATION     .......... IMPROVING          │
│  IDEAS             .......... ACCUMULATING       │
│  BROKEN THINGS     .......... EXPECTED           │
│  COFFEE            .......... REQUIRED           │
│                                                  │
└──────────────────────────────────────────────────┘

C:\VIKTORIA\PROJECTS> _
```

More projects will be added as I build, experiment, learn, repair, and inevitably break a few things along the way.

```text
END OF ARCHIVE
```
