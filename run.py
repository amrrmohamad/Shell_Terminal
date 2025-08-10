import subprocess
import tkinter as tk

def run_shell():
    subprocess.Popen(["gnome-terminal", "--", "./hsh"])

root = tk.Tk()
root.title("Run My Shell")
btn = tk.Button(root, text="Start Shell", command=run_shell)
btn.pack(padx=30, pady=30)
root.mainloop()

