
with open("text1.txt", mode="rt", encoding="utf-8") as text_file:
    first_line = text_file.readline().strip().upper()

with open("text2.txt", mode="x", encoding="utf-8") as new_file:
    new_file.write(first_line)