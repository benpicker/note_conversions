# note_conversions

This repository converts images of handwritten notes into LaTeX documents using OCR (Optical Character Recognition).

## Features

- Processes multiple image files (JPG format)
- Extracts text from images using Tesseract OCR
- Generates a formatted LaTeX document with the extracted text
- Organizes content by page/image

## Prerequisites

- Python 3.7+
- Tesseract OCR installed on your system

### Installing Tesseract

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

**Windows:**
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

## Installation

1. Clone this repository
2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the conversion script:
```bash
python convert_to_latex.py
```

This will:
1. Process all images in the `initial_trial_photos` directory
2. Extract text from each image using OCR
3. Generate a `notes.tex` LaTeX document

## Compiling the LaTeX Document

After running the conversion script, compile the generated LaTeX document:

```bash
pdflatex notes.tex
```

This will create a `notes.pdf` file with your converted notes.

## Project Structure

- `convert_to_latex.py` - Main script for image-to-LaTeX conversion
- `initial_trial_photos/` - Directory containing input images
- `notes.tex` - Generated LaTeX document (created after running the script)
- `requirements.txt` - Python dependencies

## How It Works

1. The script scans the `initial_trial_photos` directory for JPG images
2. Each image is processed using Tesseract OCR to extract text
3. Extracted text is formatted and inserted into a LaTeX document
4. Each image's content is placed in a separate section
5. The final document can be compiled to PDF using pdflatex