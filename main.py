import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

def analyze_text():
    text = text_area.get("1.0", tk.END).strip()
    char_count = len(text)
    words = text.split()
    word_count = len(words)
    common_words = Counter(words).most_common(5)

    result = f"Zeichenanzahl: {char_count}\n"
    result += f"Wortanzahl: {word_count}\n"
    result += "Häufigste Wörter:\n"
    for word, freq in common_words:
        result += f"  {word}: {freq}\n"

    result_label.config(text=result)

root = tk.Tk()
root.title("Text Analyzer")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

label = tk.Label(root, text="Text eingeben:", fg="white", bg="#1e1e1e")
label.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, font=("Consolas", 10))
text_area.pack(padx=10, pady=5)

analyze_button = tk.Button(root, text="Analysieren", command=analyze_text)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT, fg="lightgreen", bg="#1e1e1e", font=("Consolas", 10))
result_label.pack(pady=5)

root.mainloop()
