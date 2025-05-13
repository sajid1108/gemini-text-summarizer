import streamlit as st
from main import summarize

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.text_area("Enter your text here:", height=400, key="input_text")
    input_text = st.session_state["input_text"]
    input_word_count = len(input_text.split())
    input_char_count = len(input_text)
    st.write(f"Words: {input_word_count}, Characters: {input_char_count}")
    if st.button("Summarize"): 
        result = summarize(input_text)
        st.session_state["output_text"] = result

with col2:
    summarized_text = st.session_state.get("output_text", "")
    summarized_word_count = len(summarized_text.split())
    summarized_char_count = len(summarized_text)
    if summarized_text:
        st.write("Summarized Text:")
        st.code(summarized_text, language="text")  
        st.write(f"Words: {summarized_word_count}, Characters: {summarized_char_count}")