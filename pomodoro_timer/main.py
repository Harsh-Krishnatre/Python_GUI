from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    image.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    check.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work Time",fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    image.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >0:
        timer = window.after(10,count_down,count-1)
    else:
        start_timer()
        check_mark = ""
        for _ in range(reps//2):
            check_mark += "✔"
        check.config(text=check_mark, fg=GREEN, bg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50,pady=50,bg=YELLOW)
window.minsize(410,400)



image = Canvas(width=300, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
image.create_image(150,112,image=tomato_img)
timer_text = image.create_text(152,132,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
image.grid(column=1,row=1)

label = Label(text="Timer", font=(FONT_NAME,42,"normal"),fg=GREEN,bg=YELLOW,highlightthickness=0)
label.grid(column=1,row=0)

bt_start = Button(text="Start",fg=GREEN,command=start_timer)
bt_reset = Button(text="Reset",fg=GREEN,command=reset_timer)
bt_start.grid(column=0,row=2)
bt_reset.grid(column=2,row=2)

check = Label(text="",fg=GREEN,bg=YELLOW)
check.grid(column=1,row=3)



window.mainloop()