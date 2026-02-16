
import tkinter as tk
from translator_util import TextTranslator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")
        self.root.geometry("600x400")

        # Translator utility
        self.translator_util = TextTranslator()

        # Original Text Entry
        tk.Label(root, text="Enter text:", font=("Arial", 14)).pack(pady=10)
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()

        # Dropdown for language selection
        tk.Label(root, text="Select Language:", font=("Arial", 14)).pack(pady=10)
        self.selected_lang = tk.StringVar()
        self.selected_lang.set("Select Language")
        language_names = self.translator_util.language_names
        self.lang_menu = tk.OptionMenu(root, self.selected_lang, *language_names)
        self.lang_menu.pack()

        # Translate Button
        self.translate_btn = tk.Button(root, text="Translate", font=("Arial", 14, "bold"),
                                       bg="#28a745", fg="white", command=self.translate_text)
        self.translate_btn.pack(pady=10)

        # Translated Text Display
        tk.Label(root, text="Translated Text:", font=("Arial", 14)).pack(pady=10)
        self.output_text = tk.Text(root, height=5, width=50)
        self.output_text.pack()

    def translate_text(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                return

            lang_name = self.selected_lang.get()
            if lang_name == "Select Language":
                return  # Do nothing if no language selected

            # Translate using utility
            translated = self.translator_util.translate(text, lang_name)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Error: {e}")

# Run App
root = tk.Tk()
app = TranslatorApp(root)
root.mainloop()
