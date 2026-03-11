import tkinter as tk
from tkinter import messagebox, ttk
# Import your algorithms
from Ceaser import Algorithm as caesar_algo
from Monoalphabitic import Algorithm as mono_algo


# --- Logic Handlers ---

def update_result(text):
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, text)
    entry_result.config(state="readonly")


def handle_encrypt():
    mode = algo_selector.get()
    msg = entry_message.get()
    key_input = entry_key.get()

    if not msg or not key_input:
        messagebox.showwarning("Missing Input", "Please enter both a message and a key.")
        return

    try:
        if mode == "Caesar Cipher":
            # Caesar expects: encryption(msg, int_key)
            key = int(key_input)
            res = caesar_algo.encryption(msg, key)
        else:
            # Mono expects: encryption(str_key, msg)
            res = mono_algo.encryption(key_input, msg)

        update_result(res)

    except ValueError:
        messagebox.showerror("Error", "For Caesar Cipher, Key must be a number!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def handle_decrypt():
    mode = algo_selector.get()
    msg = entry_message.get()
    key_input = entry_key.get()

    if not msg or not key_input:
        messagebox.showwarning("Missing Input", "Please enter both a message and a key.")
        return

    try:
        if mode == "Caesar Cipher":
            # Caesar expects: decryption(cipher, int_key)
            key = int(key_input)
            res = caesar_algo.decryption(msg, key)
        else:
            # Mono expects: decryption(str_key, encrypted_message)
            res = mono_algo.decryption(key_input, msg)

        update_result(res)

    except ValueError:
        messagebox.showerror("Error", "For Caesar Cipher, Key must be a number!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def handle_brute_force():
    mode = algo_selector.get()

    # Brute force is only logical for Caesar in this specific app context
    if mode != "Caesar Cipher":
        messagebox.showinfo("Unavailable", "Brute Force is only available for Caesar Cipher.")
        return

    message = entry_message.get()
    if not message:
        messagebox.showwarning("Warning", "Enter a message first!")
        return

    text_area.config(state="normal")
    text_area.delete('1.0', tk.END)

    # Header
    text_area.insert(tk.END, f"{'KEY':<4} | {'DECRYPTED TEXT':<30}\n")
    text_area.insert(tk.END, "=" * 45 + "\n\n")

    for i in range(26):
        result = caesar_algo.decryption(message, i)
        text_area.insert(tk.END, f"[{i:02}] → {result}\n")
        text_area.insert(tk.END, "-" * 45 + "\n")

    text_area.config(state="disabled")


def on_mode_change(event):
    """Updates labels and button states based on selected algorithm"""
    mode = algo_selector.get()
    if mode == "Caesar Cipher":
        lbl_key.config(text="SHIFT KEY (0-25):")
        btn_brute.config(state="normal", bg="#fff3cd")
    else:
        lbl_key.config(text="KEYWORD (String):")
        btn_brute.config(state="disabled", bg="#e0e0e0")


# --- GUI Setup ---
root = tk.Tk()
root.title("Crypto Project - Multi-Algo")
root.geometry("950x650")

# Left Column: Inputs & Controls
left_frame = tk.Frame(root, padx=25, pady=20)
left_frame.grid(row=0, column=0, sticky="n")

# 1. Algorithm Selector
tk.Label(left_frame, text="SELECT ALGORITHM:", font=("Arial", 10, "bold")).pack(anchor="w")
algo_selector = ttk.Combobox(left_frame, values=["Caesar Cipher", "Monoalphabetic Cipher"], state="readonly", width=33)
algo_selector.current(0)  # Default to Caesar
algo_selector.pack(pady=5)
algo_selector.bind("<<ComboboxSelected>>", on_mode_change)

# 2. Message Input
tk.Label(left_frame, text="MESSAGE TO PROCESS:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(15, 0))
entry_message = tk.Entry(left_frame, width=35)
entry_message.pack(pady=5)

# 3. Key Input (Label changes dynamically)
lbl_key = tk.Label(left_frame, text="SHIFT KEY (0-25):", font=("Arial", 10, "bold"))
lbl_key.pack(anchor="w", pady=(10, 0))
entry_key = tk.Entry(left_frame, width=35)  # Made wider to accommodate keywords
entry_key.pack(pady=5, anchor="w")

# 4. Action Buttons
tk.Button(left_frame, text="Encrypt", command=handle_encrypt, bg="#d1e7dd", width=25).pack(pady=10)
tk.Button(left_frame, text="Decrypt", command=handle_decrypt, bg="#f8d7da", width=25).pack(pady=5)
btn_brute = tk.Button(left_frame, text="Run Brute Force Analysis ↓", command=handle_brute_force, bg="#fff3cd", width=25)
btn_brute.pack(pady=20)

# 5. Result Display
tk.Label(left_frame, text="SINGLE RESULT (COPYABLE):", font=("Arial", 9, "italic")).pack(anchor="w")
entry_result = tk.Entry(left_frame, font=("Courier", 11, "bold"), state="readonly", width=35, fg="blue")
entry_result.pack(pady=5)

# Right Column: Brute Force Table with Scrollbar
right_frame = tk.Frame(root, padx=25, pady=20)
right_frame.grid(row=0, column=1, sticky="nsew")

tk.Label(right_frame, text="ANALYSIS OUTPUT (Caesar Only):", font=("Arial", 10, "bold")).pack()

scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_area = tk.Text(
    right_frame,
    width=60,
    height=25,
    font=("Courier New", 10),
    state="disabled",
    yscrollcommand=scrollbar.set,
    spacing3=5
)
text_area.pack(pady=5)
scrollbar.config(command=text_area.yview)

root.mainloop()