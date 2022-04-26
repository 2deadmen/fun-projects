import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer =0

# ---------------------------- TIMER RESET ------------------------------- # 
def restart():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(text, text="00:00")
    label1.config(text="")
    label.config(text="Timer",fg=GREEN,font=("Ariel",34,"bold"))
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps+=1
    if reps%2==0:
        breaks = SHORT_BREAK_MIN * 60
        label.config(text="Small Break", fg=GREEN, font=("Ariel", 34, "bold"))
        countdown(breaks)
    elif reps ==7:
        min = LONG_BREAK_MIN *60
        countdown(min)
    elif reps % 2 !=0:

      work=WORK_MIN * 60
      label.config(text="Work", fg=GREEN, font=("Ariel", 34, "bold"))
      countdown(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min =math.floor( count /60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer =window.after(1000,countdown,count -1)
    if count ==0:
        if reps==2:
            label1.config(text="✔")
        elif reps ==4:
            label1.config(text="✔✔")


        start()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW,padx=100,pady=50)

label= Label()
label.config(text="Timer",fg=GREEN,font=("Ariel",34,"bold"))
label.grid(column=1,row=0)

canvas = Canvas()
canvas.config(width=200,height=224,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
text =canvas.create_text(100,130,fill="white",text="00:00",font=("Ariel",34,"bold"))
canvas.grid(column=1,row=1)

button1= Button()
button1.config(text="start",command=start)
button1.grid(column=0,row=2)

button= Button()
button.config(text="restart",command=restart)
button.grid(column=2,row=2)

label1 = Label()

label1.grid(column=1,row=2)


window.mainloop()