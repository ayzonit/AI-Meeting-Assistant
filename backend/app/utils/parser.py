def parse_output(text: str):
    sections = {"summary": "", "decisions": [], "actions": []}

    current = None
    for line in text.split("\n"):
        line = line.strip()

        if line.lower().startswith("summary"):
            current = "summary"
            continue
        if line.lower().startswith("decisions"):
            current = "decisions"
            continue
        if line.lower().startswith("action"):
            current = "actions"
            continue

        if current == "summary":
            sections["summary"] += line + " "
        elif current == "decisions" and line:
            sections["decisions"].append(line)
        elif current == "actions" and line:
            parts = line.split(" - ")
            if len(parts) == 2:
                sections["actions"].append({"owner": parts[0], "task": parts[1]})
            else:
                sections["actions"].append({"owner": None, "task": line})

    return sections