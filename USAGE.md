# Usage Examples

## Basic Usage

To convert all images in the `initial_trial_photos` directory to a LaTeX document:

```bash
python convert_to_latex.py
```

This will:
1. Process all JPG images in the `initial_trial_photos` directory
2. Extract text from each image using Tesseract OCR
3. Generate `notes.tex` LaTeX document

## Compiling to PDF

After generating the LaTeX document, compile it to PDF:

```bash
pdflatex notes.tex
```

Or run it twice to ensure all references are resolved:

```bash
pdflatex notes.tex && pdflatex notes.tex
```

## Output

The script generates:
- `notes.tex` - LaTeX source document with extracted text
- `notes.pdf` - Compiled PDF (after running pdflatex)

## What Gets Extracted

The OCR engine (Tesseract) will extract:
- Printed text
- Handwritten text (quality varies)
- Numbers and mathematical symbols
- Some special characters

Note: OCR accuracy depends on image quality, handwriting clarity, and text orientation.

## Customization

To modify the script behavior, edit `convert_to_latex.py`:

### Change input directory:
```python
photos_dir = script_dir / "your_directory_name"
```

### Change output filename:
```python
output_path = script_dir / "your_output_name.tex"
```

### Adjust LaTeX document formatting:
Modify the `latex_header` variable in the `create_latex_document()` function.
