import streamlit as st
import os
from langchain import HuggingFaceHub


st.set_page_config(page_title="QA app", page_icon=":robot:")
st.title('Question Answering with LLMS')

#st.subheader('Using flan-t5-large')
question = st.text_input("Enter your question")
question = str(question)

option = st.selectbox(
    'LLM',
    ('flan-t5-large'))


model = HuggingFaceHub(repo_id = "google/flan-t5-large")
submit = st.button("Generate Answer")
if submit:
    answer = model(question)
    st.write(answer)
