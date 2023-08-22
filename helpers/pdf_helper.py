import fitz 

def read_pdf(file):
  context = ''
  
  # Open the PDF file
  with fitz.open(stream=file.read(), filetype='pdf') as pdf_file:
  
    # Get the number of pages in the PDF file
    num_pages = pdf_file.page_count
    
    # Loop through each page in the PDF file
    for page_num in range(num_pages):
      
      # Get the current page
      page = pdf_file[page_num]
      
      # Get the text from the current page
      page_text = page.get_text()
      
      # Append the text to context
      context += page_text
  return context