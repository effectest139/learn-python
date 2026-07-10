# Tkinter 메인 메뉴

import subprocess
import sys
import tkinter as tk

from exp_manager import load_exp
from main import CHAPTERS

WIDTH = 480
HEIGHT = 640


def open_chapter(module):
    module_name = module.__name__.split(".")[-1]

    subprocess.Popen(
        [
            sys.executable,
            "-c",
            f"from chapters import {module_name}; {module_name}.start()"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


class LearnPythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("파이썬 학습 프로그램")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)

        self.build_ui()
        self.refresh_exp()

    def build_ui(self):
        tk.Label(self.root, text="파이썬 학습 프로그램").pack(pady=(20, 5))
        tk.Label(self.root, text="챕터를 선택하세요.").pack(pady=(0, 10))

        exp_frame = tk.Frame(self.root)
        exp_frame.pack(pady=10)

        tk.Label(exp_frame, text="현재 경험치").pack()

        self.exp_label = tk.Label(exp_frame, text="EXP 0")
        self.exp_label.pack()

        tk.Button(
            exp_frame,
            text="새로고침",
            command=self.refresh_exp
        ).pack(pady=5)

        chapter_frame = tk.Frame(self.root)
        chapter_frame.pack(fill="both", expand=True, padx=20)

        tk.Label(chapter_frame, text="학습 챕터").pack(pady=5)

        for key in sorted(CHAPTERS.keys(), key=int):
            title, module = CHAPTERS[key]

            tk.Button(
                chapter_frame,
                text=f"{key}. {title}",
                command=lambda m=module: open_chapter(m)
            ).pack(fill="x", pady=2)

        tk.Button(
            self.root,
            text="종료",
            command=self.root.destroy
        ).pack(fill="x", padx=20, pady=15)

    def refresh_exp(self):
        exp = load_exp()
        self.exp_label.config(text=f"EXP {exp}")


def main():
    root = tk.Tk()
    LearnPythonApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()