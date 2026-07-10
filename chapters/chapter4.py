# Chapter 4 : 조건문(if)
# if문을 사용하여 조건에 따라 다른 코드를 실행할 수 있다.


# 사용자가 엔터를 누르면 다음 단계로 넘어가는 함수
def wait_next():
    input("\n엔터를 누르면 다음 단계로 넘어갑니다...")


# 개념 설명 부분
def explain():
    print()
    print("=== Chapter 4 : 조건문(if, else) ===")
    print()

    print("[학습 목표]")
    print("if문과 else문을 사용하여 조건에 따라 다른 코드를 실행할 수 있다.")
    print()

    print("[개념 설명]")
    print("if문은 특정 조건이 참일 때만 코드를 실행합니다.")
    print()

    print("다음과 같이 작성하면 된다.")
    print("예 : if (조건문):")
    print()

    print("조건문에는 비교 연산자를 사용하여 값을 비교할 수 있습니다.")
    print("예 : if score >= 60:")
    print()
    
    # else 개념 추가된 부분
    print("[추가 개념: else]")
    print("조건문이 거짓(False)일 때 다른 코드를 실행하고 싶다면 'else:'를 사용합니다.")
    print("예 : if score >= 60:")
    print("         print('합격')")
    print("     else:")
    print("         print('불합격')")
    
    wait_next()


# 예제 1 설명
def example1():
    print()
    print("=== 예제 1 ===")
    print()

    print("다음 코드를 확인해보세요.")
    print()

    print("코드:")
    # else 예시가 포함되도록 수정된 부분
    print("if True:\n    print('Hello, World!')\nelse:\n    print('Bye, World!')")
    print()

    print("실행 결과:", end=' ')
    print("Hello, World!")
    print()

    print("설명:")
    print("if문은 조건이 참일 때만 코드를 실행합니다.")
    print("위 예제에서는 조건이 항상 참(True)이므로 'Hello, World!'가 출력되고 else 코드는 무시됩니다.")
    print("만약 if 뒤의 조건이 거짓(False)이었다면 'Bye, World!'가 출력되었을 것입니다.")

    wait_next()


# 사용자가 직접 코드를 따라 작성하는 단계
def example2():
    print()
    print("=== 따라하기 ===")
    print()

    print("코드: ", end='')
    print("if True:\    print('Hello, World!')")
    print()

    print("위 문장을 똑같이 작성하세요.")
    print()

    while True:
        answer = input("코드 입력 : ")

        # 공백 차이를 무시하기 위한 처리
        answer = answer.replace(" ", "")

        if answer == "ifTrue:\print('Hello,World!')" or answer == 'ifTrue:\print("Hello,World!")':
            print()
            print("정답입니다!")
            break

        else:
            print("다시 시도해보세요.")
            print("힌트 : if문과 print() 함수를 확인하세요.")
            print("조건문은 True로 작성하고, print() 안에 'Hello, World!'를 넣어보세요.")

    wait_next()


# 마지막 실습 문제
def practice():
    print()
    print("=== 최종 실습 ===")
    print()

    print("문제:", end=' ')
    print("사용자로부터 'number'을 입력받고")
    print("'number' 변수의 값이 0보다 크면 '양수'를")
    print("그렇지 않으면 '음수 또는 0'이라고 출력하는 코드를 작성하세요.")
    print()
    print("예시 출력:")
    print("양수")
    print()

    while True:
        answer = input("작성한 코드를 입력하세요 : ")

        answer = answer.replace(" ", "")

        if answer == "number=int(input('숫자를입력하세요:'))ifnumber>0:print('양수')else:print('음수또는0')":
            print()
            print("정답입니다!")
            print("Chapter 4 완료!")
            break

        else:
            print()
            print("정답이 아닙니다.")

            hint = input("힌트가 필요하면 h를 입력하세요 : ")

            if hint.lower() == "h":
                print()
                print("[힌트]")
                print("print() 함수를 사용하고")
                print("문장을 따옴표 안에 넣어보세요.")


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