# Chapter 6 : 함수(function)
# def를 사용하여 함수를 만들고 호출하는 학습 챕터

from exp_manager import add_exp


# 사용자가 엔터를 누르면 다음 단계로 넘어가는 함수
def wait_next():
    input("\n엔터를 누르면 다음 단계로 넘어갑니다...")


# 개념 설명 부분
def explain():
    print()
    print("=== Chapter 6 : 함수(function) ===")
    print()

    print("[학습 목표]")
    print("def를 사용하여 함수를 정의하고 호출할 수 있다.")
    print()

    print("[개념 설명]")
    print("함수는 반복해서 사용하는 코드를 하나로 묶어 이름을 붙인 것입니다.")
    print("def 함수이름(): 형태로 정의하고, 함수이름() 형태로 호출합니다.")
    print()

    print("예 :")
    print("def say_hello():")
    print("    print('안녕하세요!')")
    print()
    print("say_hello()")
    print()

    print("함수는 매개변수(parameter)를 받아서 사용할 수도 있습니다.")
    print("예 : def greeting(name): ...")
    print()

    print("또한 함수는 결과값을 돌려줄 수 있는데, 이때 return을 사용합니다.")
    print("예 : return a + b")
    print()

    print("참고로, 함수 안에서 만든 변수는 함수 밖에서는 사용할 수 없습니다.")
    print("(이런 변수의 범위를 지역 변수, 함수 밖의 변수를 전역 변수라고 부릅니다.)")

    wait_next()


# 예제 1 설명
def example1():
    print()
    print("=== 예제 1 ===")
    print()

    print("다음 코드를 확인해보세요.")
    print()

    print("코드:")
    print("def function():")
    print("    print(\"Hello, World!\")")
    print()
    print("function()")
    print()

    print("실행 결과:")
    print("Hello, World!")
    print()

    print("설명:")
    print("def function(): 으로 function이라는 이름의 함수를 정의합니다.")
    print("function() 처럼 함수 이름 뒤에 괄호를 붙여 호출하면,")
    print("함수 안에 작성된 코드가 그때 실행됩니다.")

    wait_next()


# 사용자가 직접 코드를 따라 작성하는 단계
def example2():
    print()
    print("=== 따라하기 ===")
    print()

    print("코드:")
    print("def greeting(name):")
    print("    print(name + \"님, 안녕하세요!\")")
    print()
    print("greeting(\"개발자\")")
    print()

    print("위 문장을 똑같이 작성하세요.")
    print("(줄바꿈은 ' \\ ' 기호를 사용하세요)")
    print()

    target = r'defgreeting(name):\print(name+"님,안녕하세요!")\greeting("개발자")'

    while True:
        answer = input("코드 입력 : ")

        # 공백 차이를 무시하기 위한 처리
        answer = answer.replace(" ", "")

        if answer == target:
            print()
            print("정답입니다!")
            add_exp(5)
            break

        else:
            print("다시 시도해보세요.")
            print("힌트 : 매개변수 name과 문자열 더하기(+)를 확인하세요.")

    wait_next()


# 마지막 실습 문제
def practice():
    print()
    print("=== 최종 실습 ===")
    print()

    print("문제:", end=' ')
    print("두 개의 숫자를 더한 값을 반환(return)하는 함수 add_numbers(a, b)를 만들고,")
    print("이를 사용해 3과 7을 더한 결과를 출력하세요.")
    print("(줄바꿈은 ' \\ ' 기호를 사용하세요)")
    print()
    print("10")
    print()

    target = r'defadd_numbers(a,b):\returna+b\result=add_numbers(3,7)\print(result)'

    while True:
        answer = input("작성한 코드를 입력하세요 : ")

        answer = answer.replace(" ", "")

        if answer == target:
            print()
            print("정답입니다!")
            add_exp(15)
            print("Chapter 6 완료!")
            break

        else:
            print()
            print("정답이 아닙니다.")

            hint = input("힌트가 필요하면 h를 입력하세요 : ")

            if hint.lower() == "h":
                print()
                print("[힌트]")
                print("def add_numbers(a, b): 형태로 함수를 정의하세요.")
                print("함수 안에서 return a + b 로 두 값의 합을 돌려주세요.")
                print("result = add_numbers(3, 7) 로 함수를 호출하고 결과를 저장하세요.")
                print("print(result) 로 결과를 출력하세요.")


# 챕터 실행 함수
# main.py에서 이 함수를 호출합니다.
def start():

    # 1. 개념 설명
    explain()

    # 2. 예제 확인
    example1()

    # 3. 따라하기
    example2()

    # 4. 실습
    practice()

    print()
    input("엔터를 누르면 메뉴로 돌아갑니다...")