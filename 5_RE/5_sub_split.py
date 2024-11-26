import re

text = "Moje numery telefonu to 123-456-7890 oraz 098-765-4321."
pattern = r'\d'
new_text = (re.sub(pattern, '#', text))
print(new_text)