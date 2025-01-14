import regex

text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Extracted emails:", emails)
