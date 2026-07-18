import json


def parse_llm_json(text: str) -> dict:

    text = text.strip()

    if text.startswith("```"):

        lines = text.splitlines()

        if lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]

        text = "\n".join(lines).strip()

    return json.loads(text)