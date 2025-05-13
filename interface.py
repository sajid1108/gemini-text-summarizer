import streamlit as st
from main import summarize, analyze_sentiment

# Set up Streamlit layout
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

# Input text area for the user
with col1:
    st.text_area("Enter your text here:", height=400, key="input_text")
    input_text = st.session_state["input_text"]
    input_word_count = len(input_text.split())
    input_char_count = len(input_text)
    st.write(f"Words: {input_word_count}, Characters: {input_char_count}")
    if st.button("Summarize and Analyze Sentiment"): 
        # Summarizing the text and analyzing sentiment
        result = summarize(input_text)
        sentiment = analyze_sentiment(input_text)
        st.session_state["output_text"] = result
        st.session_state["sentiment"] = sentiment

# Output column
with col2:
    summarized_text = st.session_state.get("output_text", "")
    summarized_word_count = len(summarized_text.split())
    summarized_char_count = len(summarized_text)
    
    sentiment = st.session_state.get("sentiment", "")
    
    if summarized_text:
        st.write("Summarized Text:")
        st.code(summarized_text, language="text")  
        st.write(f"Words: {summarized_word_count}, Characters: {summarized_char_count}")
        
        # Display Sentiment
        st.write(f"Sentiment: {sentiment}")
