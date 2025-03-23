# Quick revision and tips for python
** NoneType: Represents the None object, which is used to indicate the absence of a value or a null value. **
** bytes: Represents immutable sequences of bytes. Example: data = b'Hello'
** bytearray: Represents mutable sequences of bytes. Example: data = bytearray(b'Hello')

## String manipulation & Functions 
```
def string_operations(text):
    print("Original String:", text)
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title Case:", text.title())
    print("Reversed:", text[::-1])
    print("Word Count:", len(text.split()))
    print("Character Count (excluding spaces):", len(text.replace(" ", "")))
    print("Stripped:", text.strip())
    print("Replaced 'Python' with 'World':", text.replace("Python", "World"))
    print("Split into list:", text.split())
    print("Joined with '-':", "-".join(text.split()))
    print("Starts with 'Hello':", text.startswith("Hello"))
    print("Ends with 'Python!':", text.endswith("Python!"))
    print("Index of 'Python':", text.find("Python"))
    print("Count of 'o':", text.count("o"))
    print("Is alphabetic:", text.isalpha())
    print("Is digit:", text.isdigit())
    print("Is alphanumeric:", text.isalnum())
    print("Capitalized:", text.capitalize())
    print("Swapcase:", text.swapcase())

# Example usage
input_text = "Hello, welcome to Python!"
string_operations(input_text)
```
