from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
            # this with will make sure all the text is within this width
            width=280,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")

        )
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        self.trueImage = PhotoImage(file="images/true.png")
        self.falseImage = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.trueImage, highlightthickness=0,
                                  command=lambda: self.answer_question("True"))
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.falseImage, highlightthickness=0,
                                   command=lambda: self.answer_question("False"))
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of te quiz")
            # this will prevent the button from being pressed once we reach end of questions
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_question(self, answer):
        q_answer = self.quiz.check_answer(answer)
        self.give_feedback(q_answer)

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

