import streamlit as st
from simplify import simplify_text

st.set_page_config(page_title="SahajAI - Scheme Simplifier", page_icon="🧠")

st.title("🧠 SahajAI — Government Scheme Simplifier")
st.write("Paste any paragraph from a government document or scheme below, and I’ll simplify it into 3 easy bullet points!")

# Text Input
user_input = st.text_area("Enter your paragraph:", height=200)

if st.button("Simplify Text"):
    with st.spinner("Simplifying..."):
        output = simplify_text(user_input)
        st.success("✅ Simplified Summary:")
        st.write(output)
