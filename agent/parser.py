import json

def parse_response(text):
    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    except Exception:
        return {"tool": "none", "message": text}