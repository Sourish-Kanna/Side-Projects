# Visitor Entry Log System (Class 11 Computer Project)

This project is a Visitor Entry Log system made in Python, with both:

- Command-line version
- GUI version using Tkinter
- Versions with and without file storage

The program stores and searches visitor details like name, reason, date/time, wing, flat, and address.

## Main Files

- Project.py: Main launcher menu to run project versions
- 1.py: Command-line version (without data storage)
- 1-1.py: Command-line version with data storage using pickle
- 2.py: GUI version (without data storage)
- 2-2.py: GUI version with data storage using pickle

## Features

- Add new visitor entry
- View last entry
- View all entries
- Search by:
  - Name
  - Wing
  - Flat
  - Address
  - Reason
  - Flat + Wing
- Clear all saved entries (storage versions)

## Requirements

- Python 3.x
- Tkinter (usually included with Python on Windows)
- pickle module (built-in)

## How to Run

Option 1: Run launcher  

- python Project.py

Option 2: Run directly
  
- python 1.py
- python 1-1.py
- python 2.py
- python 2-2.py

## Data Storage

- Storage-based versions use a binary file named Visitor.bin.
- Visitor.bin is automatically created/updated when running 1-1.py or 2-2.py.

## Notes

- Wing input is expected as A, B, C, or D.
- Some input prompts may ask again if invalid data is entered.
- The launcher Project.py is designed to start the two storage-based versions.
