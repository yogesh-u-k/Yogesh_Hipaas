import re

with open("D:\Yogesh_Hipass\\EDI\\edi.txt") as txtfile:
    data = txtfile.read()
# Regular expression pattern to capture the first part of each segment
    pattern = r"^([A-Za-z]+)"

# Find all matching patterns
    first_elements = re.findall(pattern, data)
    print(first_elements)
