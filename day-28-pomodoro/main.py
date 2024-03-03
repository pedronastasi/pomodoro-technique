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
timer = None
reps = 0



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    print(reps)
    short_brea_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        print("long break")
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        print("short break")
        count_down(short_brea_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """
    Countdown function that updates the timer display and triggers the next countdown recursively.

    Args:
        count (int): The remaining time in seconds.

    Returns:
        None
    """
    global timer
    # format the count down into 00:00
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    formatted_count = f"{count_min}:{count_sec}"
    
    canvas.itemconfig(timer_text, text=formatted_count)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 8 == 0:
            return reset_timer()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        if reps % 8 != 0:
            for _ in range(work_sessions):
                marks += "✔"
            check_marks.config(text=marks)
   

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


# buttons
start_button = Button(text="Start", highlightthickness=0, bg=GREEN, bd=0, command=start_timer)
start_button.grid(column=0, row=3)
end_button = Button(text="Reset", highlightthickness=0, bg=RED, command=reset_timer)
end_button.grid(column=2, row=3)

# check marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# create coudt down function from 5
window

canvas.grid(column=1, row=1)

window.mainloop()
