# 콘솔 메뉴 진입점
# CHAPTERS 딕셔너리는 여기서 관리하고, app.py(GUI)에서도 이 파일에서 가져다 씁니다.

from chapters import chapter0, chapter1, chapter2, chapter3, chapter4, chapter5, chapter6
from engine import console_runner

CHAPTERS = {
    "0": ("출력(print)", chapter0),
    "1": ("변수(variable)", chapter1),
    "2": ("입력(input)", chapter2),
    "3": ("연산자(operator)", chapter3),
    "4": ("조건문(if)", chapter4),
    "5": ("반복문(loop)", chapter5),
    "6": ("함수(function)", chapter6),
}


def show_menu():
    print()
    print("=== Python Learning ===")
    print()

    for key in CHAPTERS:
        title = CHAPTERS[key][0]
        print(key + ". " + title)

    print("q. 종료")
    print()


def main():
    while True:
        show_menu()
        choice = input("학습할 챕터를 선택하세요: ").strip().lower()

        if choice == "q":
            print("프로그램을 종료합니다.")
            break

        if choice in CHAPTERS:
            module = CHAPTERS[choice][1]
            console_runner.run(module.STEPS)
        else:
            print("잘못된 입력입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    main()