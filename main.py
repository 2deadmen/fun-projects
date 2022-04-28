from tkinter import *
import pandas

count = 0
BACKGROUND_COLOR = "#B1DDC6"
with open("data/french_words.csv","r")as file:
    data = pandas.read_csv(file)
    data_dict = data.to_dict()
def trigger():
    global count
    print_word()
    window.update()
    window.after(3000)
    timer()
    count += 1
#print start
def print_word():
    french_word = data_dict["French"][count]
    canvas.itemconfig(text1,text="French")
    canvas.itemconfig(text,text=french_word)
    canvas.itemconfig(image,image=img)


#timer
def timer():


    front = PhotoImage(file="images\card_front.png")
    canvas.itemconfig(image,image=front)

    english_word = data_dict["English"][count]
    canvas.itemconfig(text, text=english_word,fill="black")
    canvas.itemconfig(text1, text="English", fill="black")

#remove card
def delete():
    global count
    del  data_dict["English"][count-1]
    del data_dict["French"][count-1]
    trigger()


#dont remove the card
def dont_delete():
    trigger()
#ui section
window =Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50,width=300,height=300)

window.title("flash cards")

canvas = Canvas(width=200,height=200)

img = PhotoImage(file="images/card_back.png")
image =canvas.create_image(100,100,image=img)
text =canvas.create_text(100,140,fill="black",text="",font=("Times",35,"bold"))
text1=canvas.create_text(100,80,fill="black",text="",font=("Times",25,"bold"))
canvas.grid(column=0,row=0,columnspan=2)




img1 =PhotoImage(file="images/wrong.png")
button1= Button(command=dont_delete,image=img1,width=80,height=80)
button1.grid(column=0,row=1)

img2 = PhotoImage(file="images/right.png")
button2 = Button(command=delete,image=img2,width=80,height=80)
button2.grid(column=1,row =1)

trigger()

window.mainloop()


