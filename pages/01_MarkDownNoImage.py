import streamlit as st
import PyPDF2
from pathlib import Path
import io

st.set_page_config(
    page_title="PDF to Markdown Converter",
    page_icon="📄",
)

def convert_pdf_to_markdown(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    
    markdown_content = ""
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        markdown_content += f"## Page {page_num + 1}\n\n{text}\n\n"
    
    # Save as markdown file in the parent directory's 'markdown' folder
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    markdown_dir = parent_dir / "markdown"
    markdown_dir.mkdir(exist_ok=True)
    markdown_file_path = markdown_dir / f"{uploaded_file.name.rsplit('.', 1)[0]}.md"
    
    with open(markdown_file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    return markdown_file_path

st.title("PDF to Markdown Converter")

st.markdown(
    """
Welcome!
            
Upload a PDF file to convert it to a Markdown format.
"""
)

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"],
)

if uploaded_file is not None:
    st.write("Converting PDF to Markdown...")
    markdown_path = convert_pdf_to_markdown(uploaded_file)
    st.success(f"Conversion complete! Markdown file saved at: {markdown_path}")
    
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