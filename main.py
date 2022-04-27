from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def insert():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    entry3.delete(0,END)
    entry3.insert(0,f"{password}")
    pyperclip.copy(text=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
    webname =entry1.get()
    password = entry3.get()
    email = entry2.get()
    if len(email)==0 or len(webname)==0 or len(password)==0:
        messagebox.showerror(title="error",message="fields cannot be empty")
    else:
        is_ok=messagebox.askokcancel(title="save",message="is it  ok to save ")
        print(is_ok)
        if is_ok:
          with open("data.txt","a") as file:
             file.write(f"\nweb:{webname}|password:{password}|email:{email}\n")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50,pady=50)
canvas = Canvas()
canvas.config(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)


label1 = Label()
label1.config(text="website")
label1.grid(column=0,row=1)

entry1= Entry(width=35)
entry1.grid(column=1,row=1,columnspan=2)
entry1.focus()

label2 = Label()
label2.config(text="emial/username")
label2.grid(column=0,row=2)


entry2= Entry(width=35)
entry2.insert(0,"kartikhegde.2002@gmail.com")
entry2.grid(column=1,row=2,columnspan=2)


label3 = Label()
label3.config(text="password")
label3.grid(column=0,row=3)


entry3= Entry(width=21)
entry3.grid(column=1,row=3,columnspan=1)


button1 =Button()
button1.config(text="generate password",command=insert)

button1.grid(column=2,row=3)


button2 =Button(width=36)
button2.config(text="ADD",command=write_to_file)
button2.grid(column=1,row=4,columnspan=2)





window.mainloop()