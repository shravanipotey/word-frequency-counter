import string

with open("sample.txt", "r") as file:
    text = file.read()

text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print(f"Total words: {len(words)}")
print(f"Unique words: {len(counts)}")
print("\nTop 5 words:")
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")