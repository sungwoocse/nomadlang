import streamlit as st
from pathlib import Path
import os

st.set_page_config(
    page_title="Code to Markdown Converter",
    page_icon="💻",
)

def convert_code_to_markdown(uploaded_files):
    markdown_content = ""
    
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        file_extension = os.path.splitext(file_name)[1].lower()
        
        if file_extension in ['.py', '.js']:
            code_content = uploaded_file.getvalue().decode('utf-8')
            
            markdown_content += f"# {file_name}\n\n"
            markdown_content += "```" + ('python' if file_extension == '.py' else 'javascript') + "\n"
            markdown_content += code_content + "\n"
            markdown_content += "```\n\n"
    
    return markdown_content

def save_markdown_file(content):
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    markdown_dir = parent_dir / "markdown"
    markdown_dir.mkdir(exist_ok=True)
    
    markdown_file_path = markdown_dir / "code_collection.md"
    
    with open(markdown_file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return markdown_file_path

st.title("Code to Markdown Converter")

st.markdown(
    """
Welcome!
            
Upload Python (.py) or JavaScript (.js) files to convert them into a single Markdown file.
"""
)

uploaded_files = st.file_uploader(
    "Upload Python or JavaScript files",
    type=["py", "js"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write("Converting code files to Markdown...")
    markdown_content = convert_code_to_markdown(uploaded_files)
    markdown_path = save_markdown_file(markdown_content)
    st.success(f"Conversion complete! Markdown file saved at: {markdown_path}")
    
    st.markdown("### Preview of the Markdown content:")
    st.text_area("Markdown Content", markdown_content, height=300)
    
    st.download_button(
        label="Download Markdown File",
        data=markdown_content,
        file_name="code_collection.md",
        mime="text/markdown",
    )
else:
    st.info("Please upload Python (.py) or JavaScript (.js) files to begin conversion.")