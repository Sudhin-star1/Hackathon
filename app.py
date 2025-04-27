import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("SudhinK/AI-Health-Coach", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("SudhinK/AI-Health-Coach")

st.title("AI Health Coach")

user_input = st.text_area("Ask me a health-related question:")

if st.button("Get Advice"):
    if user_input:
        inputs = tokenizer(user_input, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=100)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.write(f"**Coach Response:** {response}")
    else:
        st.write("Please enter a question.")
