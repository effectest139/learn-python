# Tkinter GUI 진입점

import tkinter as tk

from main import CHAPTERS
from exp_manager import load_exp
from engine.gui_runner import ChapterFrame

WIDTH = 480
HEIGHT = 640


class LearnPythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("파이썬 학습 프로그램")
        self.root.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.root.resizable(False, False)

        # 메인 메뉴 <-> 챕터 화면을 바꿔 끼우는 컨테이너
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.show_main_menu()

    def show_main_menu(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        tk.Label(self.container, text="파이썬 학습 프로그램", font=("맑은 고딕", 14, "bold")).pack(pady=(20, 5))
        tk.Label(self.container, text="챕터를 선택하세요.").pack(pady=(0, 10))

        exp = load_exp()
        tk.Label(self.container, text="현재 경험치: " + str(exp)).pack(pady=10)

        for key in CHAPTERS:
            title = CHAPTERS[key][0]
            module = CHAPTERS[key][1]

            button = tk.Button(
                self.container,
                text=key + ". " + title,
                command=lambda m=module: self.show_chapter(m),
            )
            button.pack(fill="x", padx=20, pady=2)

        tk.Button(self.container, text="종료", command=self.root.destroy).pack(fill="x", padx=20, pady=15)

    def show_chapter(self, module):
        for widget in self.container.winfo_children():
            widget.destroy()

        ChapterFrame(self.container, module.STEPS, on_finish=self.show_main_menu).pack(fill="both", expand=True)


def main():
    root = tk.Tk()
    LearnPythonApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()