# STEPS 리스트를 Tkinter 화면으로 실행하는 코드

import tkinter as tk
from exp_manager import add_exp


class ChapterFrame(tk.Frame):
    def __init__(self, parent, steps, on_finish):
        super().__init__(parent)
        self.steps = steps
        self.step_index = 0
        self.on_finish = on_finish

        self.title_label = tk.Label(self, font=("맑은 고딕", 14, "bold"))
        self.title_label.pack(pady=10)

        self.body_label = tk.Label(self, justify="left")
        self.body_label.pack(pady=10, padx=20)

        self.entry = tk.Entry(self, width=40)

        self.feedback_label = tk.Label(self, text="")
        self.feedback_label.pack()

        self.next_button = tk.Button(self)
        self.show_step()

    def show_step(self):
        self.entry.pack_forget()
        self.next_button.pack_forget()
        self.feedback_label.config(text="")

        step = self.steps[self.step_index]
        self.title_label.config(text=step["title"])

        if step["type"] == "explain":
            self.body_label.config(text=step["body"])
            self.next_button.config(text="다음", command=self.next_step)
            self.next_button.pack(pady=10)

        elif step["type"] == "quiz":
            self.body_label.config(text=step["prompt"])
            self.entry.delete(0, "end")
            self.entry.pack(pady=5)

            self.next_button.config(text="제출", command=self.check_answer)
            self.next_button.pack(pady=10)

    def next_step(self):
        self.step_index = self.step_index + 1

        if self.step_index >= len(self.steps):
            self.on_finish()
        else:
            self.show_step()

    def check_answer(self):
        step = self.steps[self.step_index]
        answer = self.entry.get()
        answer = answer.replace(" ", "")

        if answer in step["answers"]:
            add_exp(step["exp"])
            self.feedback_label.config(text="정답입니다!", fg="green")
            self.next_step()
        else:
            self.feedback_label.config(text="다시 시도해보세요. 힌트: " + step["hint"], fg="red")