import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

def analyze_text():
    text = text_area.get("1.0", tk.END).strip()
    char_count = len(text)
    words = text.split()
    word_count = len(words)
    common_words = Counter(words).most_common(5)

    result = f"📊 Analyse:\n"
    result += f"• Zeichenanzahl: {char_count}\n"
    result += f"• Wortanzahl: {word_count}\n"
    result += "• Häufigste Wörter:\n"
    for word, freq in common_words:
        result += f"   → {word}: {freq}\n"

    result_label.config(text=result)

root = tk.Tk()
root.title("📝 Text Analyzer")
root.geometry("600x480")
root.configure(bg="#2d2d2d")

# Fonts & Colors
FONT_HEADER = ("Segoe UI", 12, "bold")
FONT_TEXT = ("Consolas", 11)
FONT_RESULT = ("Consolas", 11)
COLOR_BG = "#2d2d2d"
COLOR_TEXT = "#ffffff"
COLOR_ACCENT = "#4ecdc4"
COLOR_RESULT = "#d4f4dd"
COLOR_BUTTON = "#4ecdc4"
COLOR_BUTTON_TEXT = "#1e1e1e"

# Label
label = tk.Label(root, text="Gib deinen Text ein:", fg=COLOR_ACCENT, bg=COLOR_BG, font=FONT_HEADER)
label.pack(pady=(15, 5))

# Textarea
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=12, font=FONT_TEXT,
                                      bg="#1e1e1e", fg=COLOR_TEXT, insertbackground=COLOR_ACCENT,
                                      borderwidth=0, relief=tk.FLAT)
text_area.pack(padx=15, pady=5)

# Button
analyze_button = tk.Button(root, text="🔍 Analysieren", command=analyze_text,
                           bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT,
                           activebackground="#76e8e4", font=FONT_HEADER,
                           relief=tk.FLAT, padx=10, pady=5, cursor="hand2")
analyze_button.pack(pady=10)

# Results (zentriert)
result_label = tk.Label(root, text="", justify=tk.CENTER, fg=COLOR_RESULT, bg=COLOR_BG, font=FONT_RESULT)
result_label.pack(padx=10, pady=(5, 20), anchor="center")

root.mainloop()

