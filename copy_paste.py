import pyperclip

with open('requirements.txt', 'r') as f:
    contents = f.read()
#print(contents)
pyperclip.copy(contents)
print(pyperclip.paste())