# Here the inquery (text or the transcript of the audio) is answered with a few references.

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model once
model_name = "tiiuae/falcon-rw-1b"  
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_answer(question):
    prompt = f"""Answer the following question briefly. Cite 1-2 references if applicable.\n\nQuestion: {question}\nAnswer:"""
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("Answer:")[-1].strip()
