import streamlit as st
from agent.core import agent

st.set_page_config(page_title="Local AI Agent", layout="wide")

st.title("🤖 Local AI Automation Agent")
st.write("Your personal Jarvis, running on your machine.")

# Task input
tasks_input = st.text_area(
    "Enter tasks (one per line)",
    placeholder="e.g. open google\ntake screenshot\ncreate file...",
    height=100
)

if st.button("Run Agent"):
    tasks = [t.strip() for t in tasks_input.split('\n') if t.strip()]
    if tasks:
        st.write(f"🧠 Agent is thinking... Processing {len(tasks)} task(s)")
        for i, task in enumerate(tasks, 1):
            st.info(f"Running task {i}/{len(tasks)}: {task}")
            agent(task)
        st.success(f"All {len(tasks)} task(s) executed successfully!")
    else:
        st.warning("Enter at least one task")

# Live terminal-like log viewer
st.subheader("📜 Agent Logs")

col1, col2 = st.columns([10, 2])
with col1:
    st.write("")
with col2:
    if st.button("Clear Logs", key="clear_logs"):
        with open("logs/agent.log", "w", encoding="utf-8") as f:
            f.write("")
        st.success("Logs cleared!")
        st.rerun()

with open("logs/agent.log", "r", encoding="utf-8") as f:
    logs = f.read()

st.text_area("Logs", logs, height=300)