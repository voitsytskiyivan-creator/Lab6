text = input("Введіть текст: ")
counts = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
for ch in text.lower():
    if 'a' <= ch <= 'z':
        counts[ch] += 1
print("Кількість букв у тексті: ")
print(" ".join(str(counts[chr(c)]) for c in range(ord('a'), ord('z') + 1)))