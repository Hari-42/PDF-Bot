import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("PDF Uploader App")
root.geometry("1000x600")


label = tk.Label(root, text="Upload your PDF file:", font=("Roboto", 14))
label.pack(pady=20)


def upload_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF File"
    )
    if file_path:
        print(f"File selected: {file_path}")

upload_button = tk.Button(root, text="Upload PDF", command=upload_pdf, font=("Arial", 12))
upload_button.pack(pady=10)

root.mainloop()