import tkinter as tk
import fitz
from tkinter import filedialog, scrolledtext

root = tk.Tk()
root.title("PDF Uploader App")
root.geometry("1000x600")

label = tk.Label(root, text="Upload your PDF file:", font=("Roboto", 14))
label.pack(pady=20)

file_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
file_label.pack(pady=10)


text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=20, font=("Arial", 12), state=tk.DISABLED)
text_area.pack(pady=10)

uploaded_file_path = None

summarize_button = tk.Button(root, text="Summarize PDF", font=("Arial", 12), state=tk.DISABLED)

def upload_pdf():
    global uploaded_file_path
    uploaded_file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF File"
    )
    if uploaded_file_path:
        file_name = uploaded_file_path.split("/")[-1]
        file_label.config(text=f"Uploaded: {file_name}", fg="green")
        summarize_button.config(state=tk.NORMAL)  # Enable summarize button
    else:
        file_label.config(text="No file selected", fg="red")
        summarize_button.config(state=tk.DISABLED)



def summarize_pdf():
    global uploaded_file_path

    if not uploaded_file_path:
        file_label.config(text="No PDF uploaded!", fg="red")
        return

    pdf_text = ""
    with fitz.open(uploaded_file_path) as doc:
        for page in doc:
            pdf_text += page.get_text("text")

    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, pdf_text)



upload_button = tk.Button(root, text="Upload PDF", command=upload_pdf, font=("Arial", 12))
upload_button.pack(pady=10)



summarize_button.config(command=summarize_pdf)
summarize_button.pack(pady=5)


root.mainloop()
