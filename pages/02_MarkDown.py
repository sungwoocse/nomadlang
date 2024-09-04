import streamlit as st
import fitz  # PyMuPDF
from pathlib import Path
import io

st.set_page_config(
    page_title="PDF to Markdown Converter",
    page_icon="📄",
)

def convert_pdf_to_markdown(uploaded_file):
    pdf_bytes = uploaded_file.getvalue()
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    markdown_content = ""
    
    # Create directories for images and markdown
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    image_dir = parent_dir / "markdown_images"
    image_dir.mkdir(exist_ok=True)
    markdown_dir = parent_dir / "markdown"
    markdown_dir.mkdir(exist_ok=True)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text = page.get_text()
        
        # Convert page to image
        pix = page.get_pixmap()
        image_path = image_dir / f"{uploaded_file.name.rsplit('.', 1)[0]}_page_{page_num + 1}.png"
        pix.save(str(image_path))
        
        # Add page content and image to markdown
        markdown_content += f"## Page {page_num + 1}\n\n"
        markdown_content += f"![Page {page_num + 1}]({image_path.name})\n\n"
        markdown_content += f"{text}\n\n"
    
    pdf_document.close()
    
    # Save as markdown file
    markdown_file_path = markdown_dir / f"{uploaded_file.name.rsplit('.', 1)[0]}.md"
    
    with open(markdown_file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    return markdown_file_path, image_dir

st.title("PDF to Markdown Converter with Images")

st.markdown(
    """
Welcome!
            
Upload a PDF file to convert it to a Markdown format, including images.
"""
)

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"],
)

if uploaded_file is not None:
    st.write("Converting PDF to Markdown with images...")
    markdown_path, image_dir = convert_pdf_to_markdown(uploaded_file)
    st.success(f"Conversion complete! Markdown file saved at: {markdown_path}")
    st.success(f"Images saved in directory: {image_dir}")
    
    with open(markdown_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    
    st.markdown("### Preview of the Markdown content:")
    st.text_area("Markdown Content", markdown_content, height=300)
    
    st.download_button(
        label="Download Markdown File",
        data=markdown_content,
        file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}.md",
        mime="text/markdown",
    )
else:
    st.info("Please upload a PDF file to begin conversion.")