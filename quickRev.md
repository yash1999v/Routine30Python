# Quick revision and tips for python
- **NoneType: Represents the None object, which is used to indicate the absence of a value or a null value.**
- **bytes: Represents immutable sequences of bytes. Example: data = b'Hello'**
- **bytearray: Represents mutable sequences of bytes. Example: data = bytearray(b'Hello')**

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
## modules -- OS, re,sys
- ex 1:
    ```
    import os,sys,re

 **Get the value of an environment variable**
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD", "default_pass")  # Default value if not set
print(f"Database User: {db_user}")
print(f"Database Password: {db_password}")
<!-- export DB_USER="admin"
export DB_PASSWORD="secure123"
python script.py --> 
# Print all arguments
print("Arguments:", sys.argv)
# Access individual arguments
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])  # First argument after script name
<!-- python script.py Hello World -->
    ```
## While loop for job status check 
```
while true; do
    if ! check_service_health; then
        restart_service
    fi
    sleep 30
done
```
