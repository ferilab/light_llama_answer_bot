# This is the main code that runs the model and launches the frontend using streamlit

import streamlit as st
from transcriber import transcribe_audio
from model_inference import generate_answer

st.title("Light Answering Bot")
input_mode = st.radio("Choose input method:", ["Text", "Audio"])

if input_mode == "Text":
    question = st.text_area("Enter your question or request:")
elif input_mode == "Audio":
    uploaded_file = st.file_uploader("Upload audio file (wav/mp3)", type=["wav", "mp3"])
    if uploaded_file is not None:
        question = transcribe_audio(uploaded_file)
        st.markdown(f"**Transcribed Question:** {question}")
    else:
        question = ""

if st.button("Get Answer") and question.strip():
    with st.spinner("Generating answer..."):
        answer = generate_answer(question)
        st.success("Answer ready!")
        st.markdown(f"**Answer:** {answer}")