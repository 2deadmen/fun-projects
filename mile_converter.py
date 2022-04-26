import tkinter

def onclick():
    user_input = input.get()
    value = int(user_input) / 1.6
    label3.config(text=value)

window = tkinter.Tk()
window.minsize(width=600,height=500)
window.config(padx=100,pady=100)
window.title("converter")

label = tkinter.Label(text="kilo meter ",font=("Ariel",20,))
label.grid(column=0,row=0)

button = tkinter.Button(text="convert",command=onclick )
button.grid(column=1,row=3)

label1 = tkinter.Label(text="in miles",font=("Ariel",20,))
label1.grid(column=2,row=0)


label3 = tkinter.Label(text=0,font=("Ariel",20,))
label3.grid(column=3,row=0)





input = tkinter.Entry()
input.grid(column=1,row=0)









window.mainloop()