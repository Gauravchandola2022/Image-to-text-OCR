import os
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
from PIL import Image
import pytesseract
import gradio as gr




# Function to extract text and search for a keyword
def ocr_with_search(image, keyword):
    # Extract text using OCR (supports Hindi and English)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   
    text = pytesseract.image_to_string(image, lang='hin+eng')
    
    # Split text into lines and search for keyword
    matched_lines = [line for line in text.split('\n') if keyword.lower() in line.lower()]
    
    # Return extracted text and matching lines
    return text, '\n'.join(matched_lines)

# Gradio interface to upload image and search for keywords
def create_interface():
    # Create Gradio interface
    iface = gr.Interface(
        fn=ocr_with_search,  # Function for OCR and search
        inputs=[
            gr.Image(type="pil", label="Upload Image"),  # Image upload
            gr.Textbox(placeholder="Enter keyword to search", label="Keyword Search")  # Keyword search input
        ],
        outputs=[
            gr.Textbox(label="Extracted Text"),  # Full extracted text
            gr.Textbox(label="Search Results")   # Matching keyword results
        ],
        title="Hindi and English OCR with Keyword Search",
        description="Upload an image containing Hindi and English text. Extract the text and search for keywords."
    )

    # Launch the interface
    iface.launch(share=True)

# Run the Gradio interface
if __name__ == "__main__":
    create_interface()
