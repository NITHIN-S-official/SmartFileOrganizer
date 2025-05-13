import os
import shutil
from tkinter import Tk, filedialog, Button, Label

FILE_TYPES = {
    "Word Documents": [".doc", ".docx"],
    "PDFs": [".pdf"],
    "Presentations": [".ppt", ".pptx"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Text Files": [".txt", ".md", ".rtf"],
    "eBooks": [".epub", ".mobi"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    dest = os.path.join(folder_path, category)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, filename))
                    moved = True
                    break

            if not moved:
                dest = os.path.join(folder_path, "Others")
                os.makedirs(dest, exist_ok=True)
                shutil.move(file_path, os.path.join(dest, filename))

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        organize_files(folder)
        status_label.config(text="Files organized successfully!")

# GUI
root = Tk()
root.title("Smart File Organizer")
root.geometry("350x180")
Label(root, text="Smart File Organizer", font=("Arial", 14, "bold")).pack(pady=10)
Button(root, text="Select Folder to Organize", command=select_folder, height=2, width=25).pack(pady=10)
status_label = Label(root, text="", fg="green")
status_label.pack()
root.mainloop()
