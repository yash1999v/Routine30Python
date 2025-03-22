import re
pattern=r"rain"
text ="rain rain rain"

match = re.findall(pattern,text)
if match:
    print("match found -->" ,match.span())