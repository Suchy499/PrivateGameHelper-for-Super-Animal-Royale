import re
from typing import Optional

def loads(string: str, /, *, ignore_empty: bool = False) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for comment in re.finditer(r"/\*.+?\*/|/\*.+", string, re.DOTALL):
        string = string.replace(comment.group(), "")
    for container in re.finditer(r"([^\s].*?)\s*{[^}]+}" if ignore_empty else r"([^\s].+?)\s*{[^}]*}", string, re.DOTALL):
        rule: Optional[re.Match[str]] = re.search(r"{.*}", container.group(), re.DOTALL)
        properties: dict[str, str] = {}
        for property in re.finditer(r"\s*([^{}]+?)\s*:\s*([^{}]+?)\s*[;}]", rule.group()):
            properties[property.group(1)] = property.group(2)
        result[container.group(1)] = properties
    return result

def load(file_path: str, /, *, ignore_empty: bool = False) -> dict[str, dict[str, str]]:
    with open(file_path) as file:
        if re.search(r"\n", file.read()) is None:
            print("Fuck you                      rawr :3")
        file.seek(0)
        return loads(file.read(), ignore_empty=ignore_empty)
    