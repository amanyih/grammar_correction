import streamlit as st
from happytransformer import HappyTextToText, TTSettings

st.set_page_config(page_title="Grammar Correction Tool", layout="centered")

checkpoint = "amanuelyh/grammar_correction"

@st.cache_resource
def get_happy_text(model_name):
    return HappyTextToText("T5", model_name)

happy_tt = get_happy_text(checkpoint)
args = TTSettings(num_beams=5, min_length=1)

st.title(" NLP - Grammar Correction Tool")
st.subheader("Software - Group 2")
st.markdown("""
Simply enter your text below or use one of the example sentences to get started!
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("Example 1: Incorrect Grammar"):
        st.session_state.input_text = "Speed of light is fastest then speed of sound"
with col2:
    if st.button("Example 2: Common Mistake"):
        st.session_state.input_text = "Who are the president?"

input_text = st.text_area("Enter your text here:", st.session_state.get("input_text", ""))

if st.button("Correct Grammar"):
    if input_text.strip():
        with st.spinner("Correcting grammar..."):
            formatted_input = "grammar: " + input_text
            result = happy_tt.generate_text(formatted_input, args=args)
            st.markdown("### Corrected Text:")
            st.write(result.text.strip())
    else:
        st.warning("Please enter text to correct.")

st.markdown("---")
