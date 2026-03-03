import tkinter as tk
from tkinter import messagebox
from Ceaser.Cipher_Logic import *


def update_result(text):
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, text)
    entry_result.config(state="readonly")


def handle_encrypt():
    try:
        res = encryption(entry_message.get(), int(entry_key.get()))
        update_result(res)
    except ValueError:
        messagebox.showerror("Error", "Key must be a number")


def handle_decrypt():
    try:
        res = decryption(entry_message.get(), int(entry_key.get()))
        update_result(res)
    except ValueError:
        messagebox.showerror("Error", "Key must be a number")


def handle_brute_force():
    message = entry_message.get()
    if not message:
        messagebox.showwarning("Warning", "Enter a message first!")
        return

    text_area.config(state="normal")
    text_area.delete('1.0', tk.END)

    # Header for clarity
    text_area.insert(tk.END, f"{'KEY':<4} | {'DECRYPTED TEXT':<30}\n")
    text_area.insert(tk.END, "=" * 45 + "\n\n")

    for i in range(26):
        result = decryption(message, i)
        # Added extra newline \n for breathing room between entries
        text_area.insert(tk.END, f"[{i:02}] → {result}\n")
        text_area.insert(tk.END, "-" * 45 + "\n")

    text_area.config(state="disabled")


# --- GUI Setup ---
root = tk.Tk()
root.title("Caesar Cipher - Crypto Project")
root.geometry("950x600")  # Slightly taller to accommodate spacing

# Left Column: Inputs & Controls
left_frame = tk.Frame(root, padx=25, pady=20)
left_frame.grid(row=0, column=0, sticky="n")

tk.Label(left_frame, text="MESSAGE TO PROCESS:", font=("Arial", 10, "bold")).pack(anchor="w")
entry_message = tk.Entry(left_frame, width=35)
entry_message.pack(pady=5)

tk.Label(left_frame, text="SHIFT KEY (0-25):", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
entry_key = tk.Entry(left_frame, width=10)
entry_key.pack(pady=5, anchor="w")

tk.Button(left_frame, text="Encrypt", command=handle_encrypt, bg="#d1e7dd", width=25).pack(pady=10)
tk.Button(left_frame, text="Decrypt", command=handle_decrypt, bg="#f8d7da", width=25).pack(pady=5)
tk.Button(left_frame, text="Run Brute Force Analysis ↓", command=handle_brute_force, bg="#fff3cd", width=25).pack(
    pady=20)

tk.Label(left_frame, text="SINGLE RESULT (COPYABLE):", font=("Arial", 9, "italic")).pack(anchor="w")
entry_result = tk.Entry(left_frame, font=("Courier", 11, "bold"), state="readonly", width=35, fg="blue")
entry_result.pack(pady=5)

# Right Column: Brute Force Table with Scrollbar
right_frame = tk.Frame(root, padx=25, pady=20)
right_frame.grid(row=0, column=1, sticky="nsew")

tk.Label(right_frame, text="FULL KEYSPACE DECRYPTION:", font=("Arial", 10, "bold")).pack()

# Added a scrollbar because spacing makes the list longer
scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_area = tk.Text(
    right_frame,
    width=60,
    height=25,
    font=("Courier New", 10),
    state="disabled",
    yscrollcommand=scrollbar.set,
    spacing3=5  # Adds 5 pixels of extra space after every line
)
text_area.pack(pady=5)
scrollbar.config(command=text_area.yview)

root.mainloop()