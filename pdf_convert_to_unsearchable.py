from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def pdf_to_uneditable(input_pdf_path, output_pdf_path):
    # Convert each PDF page to an image
    images = convert_from_path(input_pdf_path, poppler_path=r'C:\Program Files (x86)\poppler-24.02.0\Library\bin')
    
    print(f"Number of pages converted: {len(images)}")  # Diagnostic print

    # Prepare for writing images back to a PDF
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    
    for index, image in enumerate(images, start=1):
        print(f"Processing page {index}")  # Diagnostic print

        # Get dimensions
        image_width, image_height = image.size
        # Adjust the size and position here as necessary
        c.setPageSize((image_width, image_height))
        image_path = f'temp_image_{index}.jpg'  # Use unique names for each temp image
        image.save(image_path)
        
        # Place the image on the page
        c.drawImage(image_path, 0, 0, width=image_width, height=image_height)
        c.showPage()  # Finish the page
        
        # Clean up the image file
        os.remove(image_path)

    c.save()  # Save the PDF
    print('done')

# Example usage
input_pdf_path = input(rf'input file name including path C:\path\to\input.pdf> ')
output_pdf_path = input_pdf_path + '_unedible.pdf'

pdf_to_uneditable(input_pdf_path, output_pdf_path)
