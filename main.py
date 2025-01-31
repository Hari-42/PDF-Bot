import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("PDF Uploader App")
root.geometry("1000x600")

label = tk.Label(root, text="Upload your PDF file:", font=("Roboto", 14))
label.pack(pady=20)

file_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
file_label.pack(pady=10)

def upload_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF File"
    )
    if file_path:
        file_name = file_path.split("/")[-1]
        file_label.config(text=f"Uploaded: {file_name}")
    else:
        file_label.config(text="No file selected", fg="red")

def summarize_pdf():
    pass

upload_button = tk.Button(root, text="Upload PDF", command=upload_pdf, font=("Arial", 12))
upload_button.pack(pady=10)


summarize_button = tk.Button(root, text="Summarize PDF", command=summarize_pdf)
summarize_button.pack(pady=5)

root.mainloop()
