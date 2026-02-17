import streamlit as st
from agent.core import agent

st.set_page_config(page_title="Local AI Agent", layout="wide")

st.title("🤖 Local AI Automation Agent")
st.write("Your personal Jarvis, running on your machine.")

# Task input
task = st.text_input("Enter a task", placeholder="e.g. open google, take screenshot, create file...")

if st.button("Run Agent"):
    if task.strip():
        st.write("🧠 Agent is thinking...")
        agent(task)
        st.success("Task executed")
    else:
        st.warning("Enter a task first")

# Live terminal-like log viewer
with open("logs/agent.log", "r", encoding="utf-8") as f:
    logs = f.read()

st.subheader("📜 Agent Logs")
st.text_area("Logs", logs, height=300)