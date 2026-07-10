# Chapter 2 : 입력(input)
# input() 함수를 배우는 학습 챕터

from exp_manager import add_exp


def wait_next():
    input("\n엔터를 누르면 다음 단계로 넘어갑니다...")


def explain():
    print()
    print("=== Chapter 2 : 입력(input) ===")
    print()

    print("[학습 목표]")
    print("input() 함수를 사용하여 사용자로부터 데이터를 입력받을 수 있다.")
    print()

    print("[개념 설명]")
    print("input()는 사용자로부터 키보드 입력을 받는 함수입니다.")
    print()

    print("괄호 안에 문자열을 넣으면, 그 문자열이 사용자에게 보여집니다.")
    print("예 : answer = input('질문을 입력하세요: ')")
    print()

    print("입력된 데이터는 문자열 형태로 저장됩니다.")
    print("예 : age = input('나이를 입력하세요: ')")

    wait_next()


def example1():
    print()
    print("=== 예제 1 ===")
    print()

    print("다음 코드를 확인해보세요.")
    print()

    print("코드:")
    print("name = input('이름을 입력하세요: ')")
    print("print(name)")
    print()

    print("실행 결과:", end=' ')
    print("<입력된 이름>")
    print()

    print("설명:")
    print("input() 함수를 사용하여 사용자로부터 데이터를 입력받습니다.")

    wait_next()


def example2():
    print()
    print("=== 따라하기 ===")
    print()

    print("코드:")
    print("name = input('이름을 입력하세요: ')")
    print("print('환영합니다,', name)")
    print()

    print("위 문장을 똑같이 작성하세요.")
    print("(줄바꿈은 ' \\ ' 기호를 사용하세요)")
    print()

    target = r"name=input('이름을입력하세요:')\print('환영합니다,',name)"

    while True:
        answer = input("코드 입력 : ")
        answer = answer.replace(" ", "")

        if answer == target:
            print()
            print("정답입니다!")
            add_exp(5)
            break
        else:
            print("다시 시도해보세요.")
            print("힌트 : 따옴표를 확인하세요.")

    wait_next()


def practice():
    print()
    print("=== 최종 실습 ===")
    print()

    print("문제:", end=' ')
    print("사용자로부터 좋아하는 과일을 입력받아 'fruit' 변수에 저장하고")
    print("다음 문장을 출력하는 코드를 작성하세요.")
    print("(줄바꿈은 ' \\ ' 기호를 사용하세요)")
    print()
    print("<입력된 과일>")
    print()

    answer1 = r"fruit=input()\print(fruit)"
    answer2 = r"fruit=input('좋아하는과일을입력하세요:')\print(fruit)"

    while True:
        answer = input("작성한 코드를 입력하세요 : ")
        answer = answer.replace(" ", "")

        if answer == answer1 or answer == answer2:
            print()
            print("정답입니다!")
            add_exp(15)
            print("Chapter 2 완료!")
            break
        else:
            print()
            print("정답이 아닙니다.")

            hint = input("힌트가 필요하면 h를 입력하세요 : ")
            if hint.lower() == "h":
                print()
                print("[힌트]")
                print("input() 함수를 사용하여 사용자로부터 데이터를 입력받고")
                print("출력은 print() 함수를 사용합니다.")


def start():
    explain()
    example1()
    example2()
    practice()

    print()
    input("엔터를 누르면 메뉴로 돌아갑니다...")