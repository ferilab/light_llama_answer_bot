# light_llama_answer_bot

The bot gets a question or task in voice or transcript and answers it in transcript with some references. It is deployable for real-time answering using streamlit.

It uses tiiuae/falcon-rw-1b + Whisper + Streamlit. Input text or voice, get brief answers with optional references.

1. Package Structure

light_llama_answer_bot/
  ├── app.py           # The main code. Use "streamlit run app.py" to deploy the application on an endpoint
  ├── model_inference.py
  ├── transcriber.py
  ├── dev_run.ipynb        # For development and test purposes
  ├── requirements.txt
  └── README.md

2. Features

- Accepts voice (via Whisper) or text
- Answers via TinyLLaMA locally
- Optional Streamlit UI for real-time inference

3. Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Notes:

- With CPU-only, launching the will takes 10-20 minutes as pythorch is heavy.