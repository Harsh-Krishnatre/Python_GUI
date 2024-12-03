from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Quiz App")
        self.screen.config(bg=THEME_COLOR, padx=50, pady=30)
        self.screen.minsize(height=600, width=400)

        self.board = Canvas(height=300, width=600,bg="white")
        self.Questions = self.board.create_text(300, 150,
                                                text="Insert Question Here...",
                                                font=("Ariel", 28, "normal"),
                                                fill=THEME_COLOR,
                                                width=580,
                                                )
        self.board.grid(column=0, row=1, columnspan=2,pady=50)

        self.score = Label(text=f"Score: {self.quiz.score}",
                           font=("Ariel", 14, "bold"),
                           fg="white",
                           bg=THEME_COLOR)
        self.score.grid(column=0, row=0, columnspan=2, sticky="ns")

        true_img = PhotoImage(file="./images/true.png")
        self.true = Button(image=true_img,
                           width=90, height=90,
                           highlightthickness=0,
                           command=self.check_true)
        self.true.grid(column=0, row=2, padx=50, pady=20, sticky="ws")

        false_img = PhotoImage(file="./images/false.png", )
        self.false = Button(image=false_img,
                            width=90, height=90,
                            highlightthickness=0,
                            command=self.check_false)
        self.false.grid(column=1, row=2, padx=50, pady=20, sticky="es")

        self.get_next_ques()

        self.screen.mainloop()

    def get_next_ques(self):
        self.board.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            ques_text = self.quiz.next_question()

            self.board.itemconfig(self.Questions,text=ques_text)
        else:
            self.board.itemconfig(self.Questions,
                              text=f"You've reached the end of the Quiz Your Final score is {self.quiz.score}/10")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def check_true(self):
        if self.quiz.check_answer("true"):
            self.board.config(bg="green")
        else:
            self.board.config(bg="red")
        self.board.after(2000,self.get_next_ques)


    def check_false(self):
        if self.quiz.check_answer("false"):
            self.board.config(bg="green")
        else:
            self.board.config(bg="red")
        self.board.after(2000,self.get_next_ques)



