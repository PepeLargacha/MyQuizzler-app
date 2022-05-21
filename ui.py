from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, brain: QuizBrain):
        super().__init__()
        self.brain = brain
        self.window = Tk()
        self.window.title('Quizzer by Pepe')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.eval('tk::PlaceWindow . center')

        self.score_lb = Label(text=f"Score: 0 / 0", bg=THEME_COLOR, fg='white', font=('Arial', 10, 'bold'))
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="Some Question",
                                                font=('Arial', 16, 'italic'),
                                                fill=THEME_COLOR, width=280)

        false_img = PhotoImage(file='images/false.png')
        true_img = PhotoImage(file='images/true.png')
        self.false_btn = Button(image=false_img, highlightthickness=0, bg='red',
                                command=self.false_pressed)
        self.true_btn = Button(image=true_img, highlightthickness=0, bg='green',
                               command=self.true_pressed)

        self.score_lb.grid(column=1, row=0, pady=20)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.true_btn.grid(column=0, row=2, pady=30)
        self.false_btn.grid(column=1, row=2, pady=30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.brain.still_has_questions():
            q_text = self.brain.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='You finished this session, want to play again?')
            self.true_btn.config(command=lambda: self.keep_playing(True))
            self.false_btn.config(command=lambda: self.keep_playing(False))

    def update_score(self):
        self.score_lb.config(text=f"Score: {self.brain.score} / {self.brain.question_number}")

    def true_pressed(self):
        is_right = self.brain.check_answer(True)
        self.give_feedback(is_right)
        self.update_score()

    def false_pressed(self):
        is_right = self.brain.check_answer(False)
        self.give_feedback(is_right)
        self.update_score()

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
            self.window.after(500, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(500, self.get_next_question)

    def keep_playing(self, answer: bool):
        if answer:
            self.brain.get_questions_from_api()
            self.get_next_question()
            self.true_btn.config(command=self.true_pressed)
            self.false_btn.config(command=self.false_pressed)
        else:
            self.window.destroy()
