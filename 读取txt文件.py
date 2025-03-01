import tkinter as tk
from tkinter import filedialog, messagebox
import random

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if not lines:
                    messagebox.showinfo("Info", "The file is empty.")
                    return
                random_line = random.choice(lines).strip()
                result_label.config(text=f"Random Line: {random_line}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# 创建主窗口
root = tk.Tk()
root.title("Random Line Drawer")

# 创建并放置按钮和标签
open_button = tk.Button(root, text="Open Text File", command=open_file)
open_button.pack(pady=20)

result_label = tk.Label(root, text="Random Line: ")
result_label.pack(pady=20)

# 运行主循环
root.mainloop()
