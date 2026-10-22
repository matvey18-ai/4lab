from pathlib import Path

content = """.venv/
__pycache__/
*.pyc
*.log
"""

path = Path(__file__).parent / "12" / ".gitignore"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(content, encoding="utf-8")

print("Файл .gitignore создан:", path)
print(path.read_text())
