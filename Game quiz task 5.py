import tkinter as tk
from tkinter import messagebox

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "Who wrote the play 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
                "correct_answer": "William Shakespeare"
            }
            # Add more questions here
        ]

        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to the Quiz Game!", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.question_label = tk.Label(self, text="", font=("Arial", 12))
        self.question_label.pack()

        self.answer_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self, text="", variable=self.answer_var, value="", font=("Arial", 12))
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor=tk.W)

        self.submit_button = tk.Button(self, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 12, "italic"))
        self.feedback_label.pack()

        self.next_button = tk.Button(self, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question]
        question_text = question_data["question"]
        options = question_data["options"]

        self.question_label.config(text=question_text)

        for i in range(4):
            self.radio_buttons[i].config(text=options[i], value=options[i])

    def check_answer(self):
        selected_answer = self.answer_var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]

        if selected_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. The correct answer is: " + correct_answer, fg="red")

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.feedback_label.config(text="")
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.question_label.config(text="Quiz Completed!")
        self.feedback_label.config(text=f"Your final score is: {self.score}/{len(self.questions)}", fg="blue")
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(text="Play Again", command=self.play_again)

    def play_again(self):
        self.current_question = 0
        self.score = 0
        self.show_question()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
