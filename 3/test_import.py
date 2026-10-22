import importlib.util
from pathlib import Path

path = Path(__file__).parent.parent / "3.py"
spec = importlib.util.spec_from_file_location("task3", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print("main() не вызвалась автоматически при импорте")
