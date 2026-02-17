def create_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ File created: {filename}")