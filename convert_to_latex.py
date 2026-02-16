#!/usr/bin/env python3
"""
Convert images to LaTeX document using OCR.
Processes all images in the initial_trial_photos directory and generates a LaTeX document.
"""

import os
import glob
from PIL import Image
import pytesseract
from pathlib import Path


def preprocess_image(image_path):
    """
    Load and preprocess an image for better OCR results.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        PIL Image object
    """
    img = Image.open(image_path)
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img


def extract_text_from_image(image_path):
    """
    Extract text from an image using OCR.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Extracted text as a string
    """
    try:
        img = preprocess_image(image_path)
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        error_msg = f"Error processing {image_path}: {type(e).__name__}: {e}"
        print(error_msg)
        print("  Tip: Ensure Tesseract OCR is properly installed and the image file is valid.")
        return f"[Error processing image: {os.path.basename(image_path)}]"


def escape_latex_special_chars(text):
    """
    Escape special LaTeX characters in the text.
    
    Args:
        text: Input text string
        
    Returns:
        Text with escaped LaTeX special characters
    """
    # Characters that need escaping in LaTeX
    special_chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    
    result = text
    for char, escaped in special_chars.items():
        result = result.replace(char, escaped)
    
    return result


def create_latex_document(image_texts, output_path='notes.tex'):
    """
    Create a LaTeX document with the extracted text from images.
    
    Args:
        image_texts: List of tuples (image_name, extracted_text)
        output_path: Path to save the LaTeX document
    """
    latex_header = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{geometry}
\geometry{margin=1in}

\title{Converted Notes from Images}
\author{OCR Conversion System}
\date{\today}

\begin{document}

\maketitle

\section*{Introduction}
This document contains text extracted from handwritten notes using OCR (Optical Character Recognition).

"""

    latex_footer = r"""
\end{document}
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_header)
        
        for idx, (image_name, text) in enumerate(image_texts, 1):
            # Use verbatim for filename to avoid escaping issues
            f.write(f"\n\\section{{Page {idx}}}\n\n")
            
            # Add reference to the original image in verbatim
            f.write("\\textit{Source: \\texttt{")
            f.write(image_name.replace('_', '\\_'))
            f.write("}}\n\n")
            
            # Add the extracted text
            if text:
                f.write("\\begin{verbatim}\n")
                f.write(text)  # Use unescaped text in verbatim environment
                f.write("\n\\end{verbatim}\n")
            else:
                f.write("\\textit{[No text extracted from this image]}\n")
            
            f.write("\n\\vspace{1em}\n")
        
        f.write(latex_footer)
    
    print(f"LaTeX document created: {output_path}")


def main():
    """
    Main function to process all images and create a LaTeX document.
    """
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    photos_dir = script_dir / "initial_trial_photos"
    
    # Find all JPG images in the photos directory
    image_paths = sorted(glob.glob(str(photos_dir / "*.jpg")))
    
    if not image_paths:
        print(f"No images found in {photos_dir}")
        return
    
    print(f"Found {len(image_paths)} images to process")
    
    # Process each image
    image_texts = []
    for idx, image_path in enumerate(image_paths, 1):
        image_name = os.path.basename(image_path)
        print(f"Processing {idx}/{len(image_paths)}: {image_name}")
        
        text = extract_text_from_image(image_path)
        image_texts.append((image_name, text))
    
    # Create the LaTeX document
    output_path = script_dir / "notes.tex"
    create_latex_document(image_texts, output_path)
    
    print("\nConversion complete!")
    print(f"LaTeX document saved to: {output_path}")
    print("\nTo compile the LaTeX document, run:")
    print(f"  pdflatex {output_path}")


if __name__ == "__main__":
    main()
