def dumps(css: dict[str, dict[str, str]], /, *, indent: int = 4, sep: int = 2) -> str:
    if indent < 1:
        raise ValueError("Indentation level must be at least 1")
    if sep < 1:
        raise ValueError("The separator between ids must be at least 1")
    items: list[str] = []
    for item, rules in css.items():
        s_item: str = f"{item} {{\n"
        for name, value in rules.items():
            s_item += f"{" "*indent}{name}: {value};\n"
        items.append(f"{s_item}}}")
    return ("\n"*sep).join(items)

def dump(values: dict[str, dict[str, str]], file_path: str, /, *, indent: int = 4, sep: int = 2, append = False) -> None:
    with open(file_path, "a" if append else "w") as file:
        file.write(dumps(values, indent=indent, sep=sep))
