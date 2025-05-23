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
    # timer_text = 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label = "Timer"
    title_label.config(text="Timer")
    # reset check_marks
    check_marks.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    # if it's the 1st/3rd/5th/7th rep:
    if reps % 2 > 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    # if it's the 8th rep:
    elif reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # if it's the 2nd/4th/6th rep:
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
      global timer
      timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# x and y value for which the image will be displayed the width and height
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Entry
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "normal"))
title_label.grid(column=1, row=0)
# Start Button
start_button = Button(text="Start",  highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
# End Button
end_button = Button(text="Reset",  highlightthickness=0, command=reset_timer)
end_button.grid(column=2, row=2)
# Check
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
