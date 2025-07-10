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

    result_var.set(result)

# Hauptfenster
root = tk.Tk()
root.title("📝 Text Analyzer")
root.geometry("800x600")
root.minsize(800, 600)
root.configure(bg="#2d2d2d")

# Fonts & Farben
FONT_HEADER = ("Segoe UI", 12, "bold")
FONT_TEXT = ("Consolas", 11)
COLOR_BG = "#2d2d2d"
COLOR_TEXT = "#ffffff"
COLOR_ACCENT = "#4ecdc4"
COLOR_RESULT = "#d4f4dd"
COLOR_BUTTON = "#4ecdc4"
COLOR_BUTTON_TEXT = "#1e1e1e"

# Hauptlayout (Grid mit 3 Zeilen)
root.grid_rowconfigure(2, weight=1)  # Ergebniszeile bekommt flexiblen Platz
root.grid_columnconfigure(0, weight=1)

# Eingabeaufforderung
label = tk.Label(root, text="Gib deinen Text ein:", fg=COLOR_ACCENT, bg=COLOR_BG, font=FONT_HEADER)
label.grid(row=0, column=0, pady=(15, 5), sticky="n")

# Textfeld
text_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=80, height=12, font=FONT_TEXT,
    bg="#1e1e1e", fg=COLOR_TEXT, insertbackground=COLOR_ACCENT,
    borderwidth=0, relief=tk.FLAT
)
text_area.grid(row=1, column=0, padx=15, pady=5, sticky="n")

# Button
analyze_button = tk.Button(
    root, text="🔍 Analysieren", command=analyze_text,
    bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT,
    activebackground="#76e8e4", font=FONT_HEADER,
    relief=tk.FLAT, padx=10, pady=5, cursor="hand2"
)
analyze_button.grid(row=2, column=0, pady=(10, 0), sticky="n")

# Ergebnisanzeige zentriert
result_var = tk.StringVar()
result_label = tk.Label(
    root, textvariable=result_var, justify="center",
    fg=COLOR_RESULT, bg=COLOR_BG, font=FONT_TEXT
)
result_label.grid(row=3, column=0, pady=(20, 10), sticky="n")

root.mainloop()
