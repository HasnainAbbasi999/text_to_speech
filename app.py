# Step 1: Install necessary libraries
# !pip install streamlit TTS torchaudio

# Step 2: Import necessary libraries
import streamlit as st
from TTS.api import TTS
import os
import base64

# Step 3: Load the pre-trained TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# Step 4: Function to convert text to speech and save it as a WAV file
def text_to_speech(text, file_name="output.wav"):
    """
    Converts input text to speech and saves it as a WAV file.
    
    Args:
    - text (str): Text to be converted to speech.
    - file_name (str): File name to save the output audio.
    """
    # Generate speech and save to file
    tts.tts_to_file(text=text, file_path=file_name)

# Step 5: Function to generate download link for audio
def get_audio_download_link(file_path, file_label="Download audio"):
    with open(file_path, "rb") as file:
        audio_data = file.read()
    b64_audio = base64.b64encode(audio_data).decode()
    href = f'<a href="data:audio/wav;base64,{b64_audio}" download="{file_path}">{file_label}</a>'
    return href

# Step 6: Streamlit app interface
def main():
    st.title("Text to Speech Application")
    
    st.write("Enter the text you want to convert to speech:")
    
    # Text input from the user
    text_input = st.text_area("Enter text here", "Hello! This is a text-to-speech demo.")
    
    # Button to generate speech
    if st.button("Convert to Speech"):
        if text_input:
            file_name = "output.wav"
            
            # Convert text to speech
            text_to_speech(text_input, file_name)
            
            # Display success message
            st.success("Speech generated successfully!")
            
            # Play audio
            audio_file = open(file_name, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav")
            
            # Provide download link
            st.markdown(get_audio_download_link(file_name, "Download the audio"), unsafe_allow_html=True)

# Step 7: Run the app
if __name__ == "__main__":
    main()
