import ollama
from config import MODEL
from agent.parser import parse_response
from agent.tools import run_tool

import logging
from config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

SYSTEM_PROMPT = open("prompts/system_prompt.txt").read()

def agent(task):
    logging.info(f"USER: {task}")
    res = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": task}
        ]
    )

    text = res["message"]["content"]
    print("RAW:", text)
    logging.info(f"AI: {text}")
    cmd = parse_response(text)
    run_tool(cmd)