from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    label_Timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_lbl.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_countdown():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_Timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_Timer.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        label_Timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_countdown()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"

        check_mark_lbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=600, height=400)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas (Apple)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# GUI Functions
label_Timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_Timer.grid(row=0, column=1)
label_Timer.config(padx=20, pady=20)

start_btn = Button(text="Start", bg=YELLOW, command=start_countdown)
start_btn.grid(row=2, column=0)
start_btn.config(padx=20, pady=20)

reset_btn = Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_btn.grid(row=2, column=2)
reset_btn.config(padx=20, pady=20)

check_mark_lbl = Label(fg=GREEN, bg=YELLOW)
check_mark_lbl.grid(row=3, column=1)
check_mark_lbl.config(padx=20, pady=20)


window.mainloop()
