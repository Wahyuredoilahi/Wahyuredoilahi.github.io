import tkinter as tk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def on_encrypt_button_click():
    text = entry.get()
    shift = int(shift_entry.get())
    encrypted_text.set(encrypt(text, shift))

def on_decrypt_button_click():
    text = entry.get()
    shift = int(shift_entry.get())
    decrypted_text.set(decrypt(text, shift))

app = tk.Tk()
app.title("Caesar Cipher")

label = tk.Label(app, text="Text:")
label.pack()

entry = tk.Entry(app)
entry.pack()

shift_label = tk.Label(app, text="Shift:")
shift_label.pack()

shift_entry = tk.Entry(app)
shift_entry.pack()

encrypt_button = tk.Button(app, text="Encrypt", command=on_encrypt_button_click)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Decrypt", command=on_decrypt_button_click)
decrypt_button.pack()

encrypted_text = tk.StringVar()
decrypted_text = tk.StringVar()

encrypted_label = tk.Label(app, textvariable=encrypted_text)
encrypted_label.pack()

decrypted_label = tk.Label(app, textvariable=decrypted_text)
decrypted_label.pack()

app.mainloop()