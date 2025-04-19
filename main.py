import tkinter as tk
from tkinter import filedialog, scrolledtext
import fitz
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

root = tk.Tk()
root.title("Chat-like PDF Summarizer")
root.geometry("700x600")
root.configure(bg="#F0F0F0")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED, bg="#FFFFFF")
chat_display.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

uploaded_file_path = None

def add_message(sender, message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"{sender}: {message}\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def upload_pdf():
    global uploaded_file_path
    uploaded_file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF File"
    )
    if uploaded_file_path:
        file_name = uploaded_file_path.split("/")[-1]
        add_message("You", f"I've uploaded: {file_name}")
        summarize_button.config(state=tk.NORMAL)
    else:
        add_message("Bot", "You didn't select any file.")

def summarize_pdf():
    if not uploaded_file_path:
        add_message("Bot", "Please upload a PDF first.")
        return

    add_message("You", "Summarize this PDF for me, please.")

    pdf_text = ""
    with fitz.open(uploaded_file_path) as doc:
        for page in doc:
            pdf_text += page.get_text("text")

    parser = PlaintextParser.from_string(pdf_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 10)
    summarized_text = "\n".join(str(sentence) for sentence in summary)

    add_message("Bot", summarized_text if summarized_text.strip() else "Sorry, I couldn't generate a summary.")

button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=10)

upload_button = tk.Button(button_frame, text="Upload PDF", command=upload_pdf, font=("Arial", 12))
upload_button.grid(row=0, column=0, padx=10)

summarize_button = tk.Button(button_frame, text="Summarize", command=summarize_pdf, font=("Arial", 12), state=tk.DISABLED)
summarize_button.grid(row=0, column=1, padx=10)

root.mainloop()
