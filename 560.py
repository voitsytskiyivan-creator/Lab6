text = input("Введіть текст: ")
text = text.lower()
counts = [0] * 26
for ch in text:
    if 'a' <= ch <= 'z':
        index = ord(ch) - ord('a')
        counts[index] += 1
print(f"Кількість букв в тексті: {counts}")