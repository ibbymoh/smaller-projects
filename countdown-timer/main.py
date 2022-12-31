from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------ #
def time_reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text = "00:00")
    checkmark_label.config(text="")
    timer_label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    if reps % 8 == 0 :
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec =  f"0{count_sec}"

    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
        marks += "✔"
        checkmark_label.config(text=marks, fg=GREEN,font=(FONT_NAME,10,"bold"))



    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count -1 )
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomedoro watch")
window.config(padx=100,pady=50,bg=YELLOW)

#canvas

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text= canvas.create_text(100,138,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#buttons
start_button = Button(width=5)
start_button.config(text="start",font=(FONT_NAME,10,"bold"),command=start_timer)
start_button.grid(column=0,row=2)

end_button = Button(width=5)
end_button.config(text="end",font=(FONT_NAME,10,"bold"),command=time_reset)
end_button.grid(column=2,row=2)

#laels
timer_label = Label(bg=YELLOW)
timer_label.config(text="Timer",fg=GREEN,font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0,column=1)

checkmark_label = Label(bg=YELLOW)
checkmark_label.config( fg=GREEN,font=(FONT_NAME,10,"bold"))
checkmark_label.grid(column=1,row=3)

window.mainloop()