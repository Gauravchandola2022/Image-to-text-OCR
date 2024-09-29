import os
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
from PIL import Image
import pytesseract
import gradio as gr




# Function to extract text and search for a keyword
def ocr_with_search(image, keyword):
    
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


   
    text = pytesseract.image_to_string(image, lang='hin+eng')
    
  
    matched_lines = [line for line in text.split('\n') if keyword.lower() in line.lower()]
    
   
    return text, '\n'.join(matched_lines)

# Gradio interface to upload image and search for keywords
def create_interface():

    iface = gr.Interface(
        fn=ocr_with_search, 
        inputs=[
            gr.Image(type="pil", label="Upload Image"),  
            gr.Textbox(placeholder="Enter keyword to search", label="Keyword Search")  
        ],
        outputs=[
            gr.Textbox(label="Extracted Text"),  
            gr.Textbox(label="Search Results")   
        ],
        title="Hindi and English OCR with Keyword Search",
        description="Upload an image containing Hindi and English text. Extract the text and search for keywords."
    )

    # Launch the interface
    iface.launch(share=True)

# Run the Gradio interfacee
if __name__ == "__main__":
    create_interface()
