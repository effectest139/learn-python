# Chapter 3 : 연산자(operator)
# 연산자를 배우는 학습 챕터


# 사용자가 엔터를 누르면 다음 단계로 넘어가는 함수
def wait_next():
    input("\n엔터를 누르면 다음 단계로 넘어갑니다...")


# 개념 설명 부분
def explain():
    print()
    print("=== Chapter 3 : 연산자(operator) ===")
    print()

    print("[학습 목표]")
    print("연산자를 사용하여 값을 계산하고 비교할 수 있다.")
    print()

    print("[개념 설명]")
    print("연산자는 값을 계산하거나 비교할 때 사용합니다.")
    print("예 : +, -, *, / 는 사칙연산, ==, !=, >, < 는 비교 연산자입니다.")
    print()

    print("값을 계산해서 변수에 저장할 수도 있습니다.")
    print("예 : sum = 5 + 3")
    print()

    print("다른 문법과 함께 사용하여 조건문과 반복문을 만들 수 있습니다.")
    print("예 : if score >= 60: print('합격')")
    
    wait_next()


# 예제 1 설명
def example1():
    print()
    print("=== 예제 1 ===")
    print()

    print("다음 코드를 확인해보세요.")
    print()

    print("코드:")
    print("print(10+5)")
    print()

    print("실행 결과:", end=' ')
    print(15)
    print()

    print("설명:")
    print("print() 안에 있는 값을 더하여 화면에 출력합니다.")

    wait_next()


# 사용자가 직접 코드를 따라 작성하는 단계
def example2():
    print()
    print("=== 따라하기 ===")
    print()

    print("코드: ", end='')
    print("print(20-7)")
    print()

    print("위 문장을 똑같이 작성하세요.")
    print()

    while True:
        answer = input("코드 입력 : ")

        # 공백 차이를 무시하기 위한 처리
        answer = answer.replace(" ", "")

        if answer == "print(20-7)":
            print()
            print("정답입니다!")
            break

        else:
            print("다시 시도해보세요.")
            print("힌트 : 연산자 '-'를 확인하세요.")

    wait_next()


# 마지막 실습 문제
def practice():
    print()
    print("=== 최종 실습 ===")
    print()

    print("문제:", end=' ')
    print("가로 길이(width) 5와 세로 길이(height) 8을 변수에 저장하고")
    print("가로 길이와 세로 길이를 곱하여 넓이(area)를 계산하고 출력하세요.")
    print("(줄바꿈은' \ '기호를 사용하세요)")
    print()
    print("40")
    print()

    while True:
        answer = input("작성한 코드를 입력하세요 : ")

        answer = answer.replace(" ", "")

        if answer == "width=5\height=8\area=width*height\print(area)" or answer == "width=5\height=8\print(width*height)":
            print()
            print("정답입니다!")
            print("Chapter 3 완료!")
            break

        else:
            print()
            print("정답이 아닙니다.")

            hint = input("힌트가 필요하면 h를 입력하세요 : ")

            if hint.lower() == "h":
                print()
                print("[힌트]")
                print("가로 길이와 세로 길이를 곱하면 넓이를 구할 수 있습니다.")
                print("연산자 '*'를 사용하여 계산하세요.")
                print("넓이 변수를 area로 지정하고, print() 함수를 사용하여 출력하세요.")


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