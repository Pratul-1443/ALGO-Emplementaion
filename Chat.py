import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#key




# --- Page Config ---
st.set_page_config(page_title="ML Algorithm Explainer", page_icon="✨", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #e3f2fd, #fff);
    }
    .stTextInput > div > div > input {
        font-size: 18px;
        padding: 0.5em;
    }
    .stButton > button {
        background-color: #2962ff;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("<h1 style='text-align: center;'>🤖 GenAI ML Tutor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Get Step-by-Step Python Implementation of Any ML Algorithm</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Sidebar ---
with st.sidebar:
    st.image("https://www.python.org/static/community_logos/python-logo.png", use_container_width=True)
    st.markdown("### 🔍 Examples to Try:")
    st.markdown("- Random Forest")
    st.markdown("- Linear Regression")
    st.markdown("- KMeans Clustering")
    st.markdown("- PCA")
    st.markdown("---")
    st.markdown("Made by Pratul")

# --- Input Field ---
st.markdown("### 📥 Ask for ML Algorithm Implementation")
name_of_algo = st.text_input("Enter ML Algorithm Name Here")

# --- Button ---
click_btn = st.button("🚀 Generate Code")



import os
from dotenv import load_dotenv
load_dotenv()


# --- LangChain Setup ---

llm = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-1.5-flash"
)




chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI tutor with expertise in Data Science and AI who tells step-by-step Python implementation for machine learning algorithms."),
    ("human", "Tell me Python implementation of {user}?")
])

output_parser = StrOutputParser()
chain = chat_prompt | llm | output_parser

# --- On Button Click ---
if click_btn:
    if not name_of_algo:
        st.warning("⚠️ Please enter an algorithm name.")
    else:
        with st.spinner("🧠 Generating step-by-step implementation..."):
            user_input = {"user": name_of_algo}
            result = chain.invoke(user_input)
            st.success("✅ Here's the implementation:")
            st.markdown(f"```python\n{result}\n```")
