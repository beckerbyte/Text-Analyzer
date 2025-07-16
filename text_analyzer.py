import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox, Toplevel, PhotoImage, ttk
from collections import Counter
import re
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------------- Textanalyse-Funktionen ---------------------- #

def analyze_text():
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        result_var.set("⚠️ Kein Text vorhanden.")
        return

    char_count = len(text)
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    sentence_count = len(re.findall(r'[.!?]', text))
    avg_word_len = sum(len(w) for w in words) / word_count if word_count else 0
    syllables = sum(count_syllables(word) for word in words)
    flesch_score = 206.835 - 1.015 * (word_count / (sentence_count or 1)) - 84.6 * (syllables / (word_count or 1))

    common_words = Counter(words).most_common(5)

    result = f"📊 Analyse:\n"
    result += f"• Zeichenanzahl: {char_count}\n"
    result += f"• Wortanzahl: {word_count}\n"
    result += f"• Satzanzahl: {sentence_count}\n"
    result += f"• ⌀ Wortlänge: {avg_word_len:.2f} Zeichen\n"
    result += f"• Lesbarkeit (Flesch): {flesch_score:.2f}\n"
    result += "• Häufigste Wörter:\n"
    for word, freq in common_words:
        result += f"   → {word}: {freq}\n"

    result_var.set(result)

def count_syllables(word):
    return len(re.findall(r'[aeiouyäöü]+', word.lower()))

def export_result():
    text = result_var.get()
    if not text:
        messagebox.showwarning("Fehler", "Keine Analyse zum Exportieren.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Erfolg", "Analyse gespeichert.")

def show_word_histogram():
    text = text_area.get("1.0", tk.END).strip()
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    if not counter:
        messagebox.showwarning("Fehler", "Keine Daten für Histogramm.")
        return

    top_words = counter.most_common(10)
    labels, values = zip(*top_words)

    fig_win = Toplevel(root)
    fig_win.title("📈 Wortfrequenz")
    fig = plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title("Top 10 Wörter")
    plt.ylabel("Häufigkeit")
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fig_win)
    canvas.get_tk_widget().pack()
    canvas.draw()

# ---------------------- Haupt-GUI ---------------------- #

def start_main_gui():
    global root, text_area, result_var

    root = tk.Tk()
    root.title("📝 Text Analyzer Pro")
    root.geometry("900x650")
    root.configure(bg="#1e1e1e")

    try:
        logo_img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo.png"))
        root.iconphoto(False, logo_img)
    except Exception as e:
        print(f"⚠️ Fenster-Logo konnte nicht geladen werden: {e}")

    FONT_HEADER = ("Segoe UI", 13, "bold")
    FONT_TEXT = ("Consolas", 11)
    COLOR_BG = "#1e1e1e"
    COLOR_TEXT = "#ffffff"
    COLOR_ACCENT = "#4ecdc4"
    COLOR_RESULT = "#d4f4dd"
    COLOR_BUTTON = "#4ecdc4"
    COLOR_BUTTON_TEXT = "#1e1e1e"

    label = tk.Label(root, text="Text eingeben:", fg=COLOR_ACCENT, bg=COLOR_BG, font=FONT_HEADER)
    label.pack(pady=(15, 5))

    text_area = scrolledtext.ScrolledText(
        root, wrap=tk.WORD, width=100, height=15, font=FONT_TEXT,
        bg="#2a2a2a", fg=COLOR_TEXT, insertbackground=COLOR_ACCENT,
        borderwidth=0, relief=tk.FLAT
    )
    text_area.pack(padx=20, pady=5)

    btn_frame = tk.Frame(root, bg=COLOR_BG)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="🔍 Analysieren", command=analyze_text,
              bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_HEADER,
              relief=tk.FLAT, padx=12, pady=5, cursor="hand2").grid(row=0, column=0, padx=5)

    tk.Button(btn_frame, text="💾 Exportieren", command=export_result,
              bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_HEADER,
              relief=tk.FLAT, padx=12, pady=5, cursor="hand2").grid(row=0, column=1, padx=5)

    tk.Button(btn_frame, text="📈 Häufigkeit", command=show_word_histogram,
              bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_HEADER,
              relief=tk.FLAT, padx=12, pady=5, cursor="hand2").grid(row=0, column=2, padx=5)

    result_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_var, justify="left",
                            fg=COLOR_RESULT, bg=COLOR_BG, font=FONT_TEXT, anchor="w")
    result_label.pack(padx=20, pady=20, fill="both")

    root.mainloop()

# ---------------------- Splash Screen ---------------------- #

def show_splash_and_start():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.configure(bg="#1e1e1e")

    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    width, height = 320, 320
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    splash.geometry(f"{width}x{height}+{x}+{y}")

    try:
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        logo_img = PhotoImage(file=logo_path)
        logo_label = tk.Label(splash, image=logo_img, bg="#1e1e1e")
        logo_label.image = logo_img
        logo_label.pack(pady=(40, 10))
    except Exception as e:
        print(f"⚠️ Splash-Logo konnte nicht geladen werden: {e}")

    loading_label = tk.Label(splash, text="Wird geladen...", fg="#4ecdc4", bg="#1e1e1e", font=("Segoe UI", 10, "italic"))
    loading_label.pack()

    progress = ttk.Progressbar(splash, orient=tk.HORIZONTAL, mode='indeterminate', length=180)
    progress.pack(pady=15)
    progress.start(10)

    def close_splash():
        progress.stop()
        splash.destroy()
        start_main_gui()

    splash.after(2000, close_splash)
    splash.mainloop()

# ---------------------- Main Entry Point ---------------------- #

if __name__ == "__main__":
    show_splash_and_start()
