from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        # 150 and 120 is the position the item should be relative to width and height, in this case it's in center

        self.question_text = self.canvas.create_text(
            150,
            120,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")

        )
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        self.trueImage = PhotoImage(file="images/true.png")
        self.falseImage = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.trueImage, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.falseImage, highlightthickness=0 )
        self.false_button.grid(column=1, row=2)
        self.window.mainloop()