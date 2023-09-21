import string
import random
import tkinter as tk
from tkinter import ttk, messagebox

def generate_password():
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    characters_numbers = entry_characters.get()

    try:
        characters_numbers = int(characters_numbers)
        if characters_numbers < 6:
            messagebox.showerror("Error", "Password must have at least 6 characters!")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    # 30% letters, 20% digits, 20% punctuation
    part1 = round(characters_numbers * (30/100))
    part2 = round(characters_numbers * (20/100))

    password = []
    for i in range(part1):
        password.append(s1[i])
        password.append(s2[i])

    for i in range(part2):
        password.append(s3[i])
        password.append(s4[i])

    random.shuffle(password)  # Shuffle the entire password list

    password = "".join(password[0:characters_numbers])
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

app_view = tk.Tk()
app_view.title("Password Generator")

frame = ttk.Frame(app_view, padding="20")
frame.grid(row=0, column=0)

label_characters = ttk.Label(frame, text="Number of Characters:")
label_characters.grid(row=0, column=0)

entry_characters = ttk.Entry(frame)
entry_characters.grid(row=0, column=1)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2)

label_password = ttk.Label(frame, text="Generated Password:")
label_password.grid(row=2, column=0)

entry_password = ttk.Entry(frame)
entry_password.grid(row=2, column=1)

app_view.mainloop()
