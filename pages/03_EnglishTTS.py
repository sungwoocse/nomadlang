import streamlit as st
import whisper
from pathlib import Path
import torch
import time
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Speech to Markdown Converter",
    page_icon="🎤",
)

@st.cache_resource
def load_whisper_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        model = whisper.load_model("base", device=device)
        # Ensure FP32 is used on CPU
        model = model.float()
    else:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model = whisper.load_model("base", device=device)
    return model

def convert_speech_to_markdown(uploaded_file, progress_bar):
    # Load the Whisper model
    model = load_whisper_model()

    # Create directory for markdown
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    markdown_dir = parent_dir / "markdown"
    markdown_dir.mkdir(exist_ok=True)

    # Save uploaded file temporarily
    temp_file = Path(uploaded_file.name)
    try:
        with open(temp_file, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Transcribe the audio
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = model.transcribe(str(temp_file))
        
        progress_bar.progress(0)
        transcribed_text = result["text"]
        
        # Simulate progress
        for i in range(100):
            progress_bar.progress(i / 100)
            time.sleep(0.01)

        # Create markdown content
        markdown_content = f"# Transcription of {uploaded_file.name}\n\n{transcribed_text}\n"

        # Save as markdown file
        markdown_file_path = markdown_dir / f"{uploaded_file.name.rsplit('.', 1)[0]}.md"
        
        with open(markdown_file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        return markdown_file_path, transcribed_text

    finally:
        # Ensure temporary file is deleted even if an exception occurs
        if temp_file.exists():
            temp_file.unlink()

st.title("Speech to Markdown Converter")

st.markdown(
    """
Welcome!
            
Upload an m4a file to convert its speech to English text and save as a Markdown file.
This version supports large audio files and uses GPU acceleration if available.
"""
)

uploaded_file = st.file_uploader(
    "Upload an m4a file",
    type=["m4a"],
)

if uploaded_file is not None:
    st.write("Transcribing and translating speech to English text...")
    progress_bar = st.progress(0)
    markdown_path, transcribed_text = convert_speech_to_markdown(uploaded_file, progress_bar)
    st.success(f"Conversion complete! Markdown file saved at: {markdown_path}")
    
    st.markdown("### Preview of the transcribed content:")
    st.text_area("Transcribed Text", transcribed_text, height=300)
    
    with open(markdown_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    
    st.download_button(
        label="Download Markdown File",
        data=markdown_content,
        file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}.md",
        mime="text/markdown",
    )
else:
    st.info("Please upload an m4a file to begin conversion.")

# Display GPU usage information
if torch.cuda.is_available():
    st.sidebar.write("GPU is being used for transcription.")
    st.sidebar.write(f"GPU: {torch.cuda.get_device_name(0)}")
    st.sidebar.write(f"Memory Usage: {torch.cuda.memory_allocated(0)/1024**3:.2f} GB")
else:
    st.sidebar.write("CPU is being used for transcription. For faster processing, consider using a machine with a GPU.")