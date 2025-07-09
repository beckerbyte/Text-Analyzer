import sys
from collections import Counter

def analyze(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    word_count = len(words)
    char_count = len(text)
    common_words = Counter(words).most_common(5)

    print(f"Zeichenanzahl: {char_count}")
    print(f"Wortanzahl: {word_count}")
    print("Top 5 Wörter:")
    for word, count in common_words:
        print(f"  {word}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python analyzer.py <dateipfad>")
    else:
        analyze(sys.argv[1])
