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
root.geometry("800x600")         # Startgröße
root.minsize(800, 600)           # Mindestgröße
root.configure(bg="#2d2d2d")     # Dark-Theme-Hintergrund

# Fonts & Farben
FONT_HEADER = ("Segoe UI", 12, "bold")
FONT_TEXT = ("Consolas", 11)
COLOR_BG = "#2d2d2d"
COLOR_TEXT = "#ffffff"
COLOR_ACCENT = "#4ecdc4"
COLOR_RESULT = "#d4f4dd"
COLOR_BUTTON = "#4ecdc4"
COLOR_BUTTON_TEXT = "#1e1e1e"

# Eingabeaufforderung
label = tk.Label(root, text="Gib deinen Text ein:", fg=COLOR_ACCENT, bg=COLOR_BG, font=FONT_HEADER)
label.pack(pady=(15, 5))

# Textfeld
text_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=80, height=15, font=FONT_TEXT,
    bg="#1e1e1e", fg=COLOR_TEXT, insertbackground=COLOR_ACCENT,
    borderwidth=0, relief=tk.FLAT
)
text_area.pack(padx=15, pady=5)

# Analyse-Button
analyze_button = tk.Button(
    root, text="🔍 Analysieren", command=analyze_text,
    bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT,
    activebackground="#76e8e4", font=FONT_HEADER,
    relief=tk.FLAT, padx=10, pady=5, cursor="hand2"
)
analyze_button.pack(pady=10)

# Ergebnisanzeige zentriert im Frame
result_var = tk.StringVar()
result_frame = tk.Frame(root, bg=COLOR_BG)
result_frame.pack(fill="both", expand=True)

result_label = tk.Label(
    result_frame, textvariable=result_var, justify="center",
    fg=COLOR_RESULT, bg=COLOR_BG, font=FONT_TEXT
)
result_label.pack(expand=True)

# Start
root.mainloop()
