from tkinter import  *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_note():
    note_website = entry_website.get()
    note_email = entry_email.get()
    note_password = entry_password.get()
    
    is_ok =  messagebox.askokcancel(title="Confirmation", message=f"Website: {note_website}\nEmail: {note_email}\nPassword: {note_password}\n Is it ok to save that information?")
    
    if is_ok:
        with open ("note.txt", "a") as file:
            file.write(f"Website: {note_website} / ")
            file.write(f"Email: {note_email} / ")
            file.write(f"Password: {note_password} \n")
        
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            
    elif  label1 or label2 or label3 == 0:
        messagebox.showerror(title="Error", message="You shouldn't left spaces empty")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(row=0, column=1)

label1 = Label(text="website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)


entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "joangabrieldj@gmail.com")

entry_password = Entry(width=35)
entry_password.grid(row=3, column=1, columnspan=2)

button1 = Button(text="Gen Password", width=10, command=generate_password)
button1.grid(row=3, column=3, columnspan=1)

button2 = Button(text="Add", width=36, command=save_note)
button2.grid(row=4, column=1, columnspan=2)

window.mainloop()
