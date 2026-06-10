import re

text = "satya will get his new job soon"
pattern = "satya"

search = re.search(pattern, text)
if search:
    print("match found:", search.group())
else:
    print("not found")