import pickle
import streamlit as st
import gTTS
import io
import os
import base64
language = 'en'


model= pickle.load(open('spam123.pkl','rb'))
cv= pickle.load(open('vect123.pkl','rb'))


def get_audio_bytes(filename):
    """Convert the audio file to a base64 encoded string for embedding in HTML."""
    with open(filename, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode("utf-8")



def main():
  st.title("Email Spam Classification Application")
  st.write("This is an Machine Learning Application to classify the mails/messages")
  st.subheader("Classification")
  user_input=st.text_area("Enter an email to classify", height=100)
  if st.button("Classify"):
    data=[user_input]
    print(data)
    vec=cv.transform(data).toarray()
    result=model.predict(vec)
    if result[0]==0:
      st.success("This is not a Spam Email")
      tts = gTTS(text="This is not a Spam Email", lang=language)
      audio_filename = "output.mp3"
      tts.save(audio_filename)
        
        # Get the base64 encoded audio data
      audio_base64 = get_audio_bytes(audio_filename)

        # HTML for autoplay audio (using base64)
      audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """

        # Display the audio player with autoplay
      st.markdown(audio_html, unsafe_allow_html=True)

        # Optionally, delete the file after playing to avoid clutter
      os.remove(audio_filename)
      
    else :
      st.error("This is a Spam Email")
      tts = gTTS(text="This is  a Spam Email", lang=language)
      audio_filename = "output.mp3"
      tts.save(audio_filename)
        
        # Get the base64 encoded audio data
      audio_base64 = get_audio_bytes(audio_filename)

        # HTML for autoplay audio (using base64)
      audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """

        # Display the audio player with autoplay
      st.markdown(audio_html, unsafe_allow_html=True)

        # Optionally, delete the file after playing to avoid clutter
      os.remove(audio_filename)


main()

