import os

print("CWD:", os.getcwd())

file = "samplexml.xml"
print("Absolute path:", os.path.abspath(file))

print("Exists:", os.path.exists(file))

with open(file, "r") as f:
    content = f.read()
    print("RAW CONTENT:")
    print(repr(content))