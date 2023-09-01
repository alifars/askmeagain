import streamlit as st
import os
from langchain import HuggingFaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
st.set_page_config(page_title="QA app", page_icon=":robot:")
question = st.text_input("Enter your question")

#model = HuggingFaceHub(repo_id = "/google/flan-t5-large")
model = HuggingFaceHub(repo_id = "google/flan-t5-large")

answer = model(question)
st.write(answer)