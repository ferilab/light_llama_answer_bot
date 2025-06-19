# This module converts audio (given by the user) to transcript

from faster_whisper import WhisperModel
import tempfile

def transcribe_audio(file):
    model = WhisperModel("base", compute_type="int8")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        temp.write(file.read())
        segments, _ = model.transcribe(temp.name)
        return " ".join([seg.text for seg in segments])
