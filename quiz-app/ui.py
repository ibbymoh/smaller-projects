from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_interface: QuizBrain):
        self.quiz = quiz_interface
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR)
        self.score = Canvas(bg=THEME_COLOR,highlightthickness=0,height=20,width=50)
        self.score.grid(row=0,column=1,padx=20,pady=20)
        self.score_text = self.score.create_text(25,10,text="Score: 0",font=("Arial",10,"italic"),fill="white")
        self.canvas = Canvas(bg="white",height=250,width=300)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="hello",
                                                     font=("Arial",
                                                           20,
                                                           "italic"),
                                                     width=280

                                                     )

        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image,height=97,width=100,highlightthickness=0,bg=THEME_COLOR,borderwidth=0,command=self.tick_pressed)
        self.true.grid(row=2,column=0,pady=40,padx=40)

        false_image = PhotoImage(file="images/false.png")
        self.true = Button(image=false_image, height=97, width=100, highlightthickness=0, bg=THEME_COLOR, borderwidth=0,command=self.cross_pressed)
        self.true.grid(row=2, column=1, pady=40, padx=40)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text = q_text)
        else:
            self.canvas.itemconfig(self.question_text ,text="You have reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def tick_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score.itemconfig(self.score_text,text=f"score: {self.quiz.score}")
        self.get_next_question

    def cross_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.get_next_question()

    def reset_background(self):
        self.canvas.config(bg="white")

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green",highlightthickness=0)
            self.window.after(1000,self.reset_background)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
            self.window.after(1000, self.reset_background)


