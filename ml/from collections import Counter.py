from collections import Counter

text = "tdtaqnondoldwrncwofoaeizhwkgtop"

print("Frequency:")
for ch, count in Counter(text).most_common():
    print(ch, count)

print("\nRepeated bigrams:")
bigrams = {}
for i in range(len(text)-1):
    bg = text[i:i+2]
    bigrams[bg] = bigrams.get(bg, 0) + 1

for bg, c in sorted(bigrams.items(), key=lambda x: -x[1]):
    if c > 1:
        print(bg, c)

print("\nAll substrings:")
substrings = [text[i:j] for i in range(len(text)) for j in range(i+1, len(text)+1)]
for s in substrings:
    print(s)