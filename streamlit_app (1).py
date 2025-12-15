import streamlit as st
import subprocess
import os

# Page config
st.set_page_config(
    page_title="Earthquake Prediction System",
    page_icon="🌍",
    layout="wide"
)

# Title
st.markdown(
    "<h1 style='text-align:center;'>🌍 Earthquake Prediction Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Model Performance & Risk Analysis</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# Country selector
countries = [
    "Pakistan", "Japan", "USA", "China", "Turkey",
    "Iran", "Nepal", "Indonesia", "Mexico", "Chile"
]

country = st.selectbox("🌐 Select Country", countries)

# Run model
if st.button("🚨 Run Earthquake Prediction"):

    st.info("Running earthquake prediction model... Please wait")

    # 1️⃣ Execute notebook (UNCHANGED)
    subprocess.run([
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--output", "executed.ipynb",
        "AI_PROJECT_GRAPH.ipynb"
    ], check=True)

    # 2️⃣ Convert executed notebook to HTML
    subprocess.run([
        "jupyter", "nbconvert",
        "--to", "html",
        "executed.ipynb"
    ], check=True)

    st.success("Prediction completed successfully")

    # 3️⃣ Display notebook output (ALL GRAPHS + METRICS)
    st.markdown("## 📊 Model Results & Visualizations")

    with open("executed.html", "r", encoding="utf-8") as f:
        html_data = f.read()

    st.components.v1.html(html_data, height=1000, scrolling=True)
