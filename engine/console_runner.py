# STEPS 리스트를 콘솔(글자 화면)로 실행하는 코드

from exp_manager import add_exp


def run(steps):
    for step in steps:
        if step["type"] == "explain":
            show_explain(step)
        elif step["type"] == "quiz":
            show_quiz(step)

    print()
    input("엔터를 누르면 메뉴로 돌아갑니다...")


def show_explain(step):
    print()
    print("=== " + step["title"] + " ===")
    print()
    print(step["body"])
    print()
    input("엔터를 누르면 다음 단계로 넘어갑니다...")


def show_quiz(step):
    print()
    print("=== " + step["title"] + " ===")
    print()
    print(step["prompt"])
    print()

    while True:
        answer = input("코드 입력 : ")
        answer = answer.replace(" ", "")

        if answer in step["answers"]:
            print()
            print("정답입니다!")
            add_exp(step["exp"])
            break
        else:
            print()
            print("다시 시도해보세요.")
            print("힌트 : " + step["hint"])