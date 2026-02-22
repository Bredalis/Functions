
# Most used string methods
text_string = "Hello, World"

methods = [
    ("Capitalize", text_string.capitalize()),
    ("Casefold", text_string.casefold()),
    ("Count 'o'", text_string.count("o")),
    ("Find 'Hello'", text_string.find("Hello")),
    ("Index 'World'", text_string.index("World")),
    ("Isalnum", text_string.isalnum()),
    ("Isalpha", text_string.isalpha()),
    ("Isascii", text_string.isascii()),
    ("Isdecimal", text_string.isdecimal()),
    ("Isdigit", text_string.isdigit()),
    ("Islower", text_string.islower()),
    ("Isnumeric", text_string.isnumeric()),
    ("Isprintable", text_string.isprintable()),
]

for name, result in methods:
    print(f"{name}: {result}")
