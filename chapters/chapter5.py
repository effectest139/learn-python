# Chapter 5 : 반복문(loop)
# while문을 사용하여 반복 실행을 배우는 학습 챕터


# 사용자가 엔터를 누르면 다음 단계로 넘어가는 함수
def wait_next():
    input("\n엔터를 누르면 다음 단계로 넘어갑니다...")


# 개념 설명 부분
def explain():
    print()
    print("=== Chapter 5 : 반복문(loop) ===")
    print()

    print("[학습 목표]")
    print("while문을 사용하여 조건에 따라 코드를 반복 실행할 수 있다.")
    print()

    print("[개념 설명]")
    print("반복문은 정해진 조건을 만족하는 동안 코드를 여러 번 실행합니다.")
    print("while 조건: 형태로 작성하며, 조건이 참(True)인 동안 반복합니다.")
    print()

    print("예 :")
    print("count = 1")
    print("while count <= 3:")
    print("    print(count)")
    print("    count += 1")
    print()

    print("조건 없이 무조건 반복하고 싶다면 while True: 를 사용합니다.")
    print("이 경우 반복을 멈추려면 break문을 사용해야 합니다.")
    print()

    print("예 :")
    print("while True:")
    print("    print('반복')")
    print("    break")

    wait_next()


# 예제 1 설명
def example1():
    print()
    print("=== 예제 1 ===")
    print()

    print("다음 코드를 확인해보세요.")
    print()

    print("코드:")
    print("count = 0")
    print("while True:")
    print("    print(\"Hello, World!\")")
    print("    count += 1")
    print("    if count == 3:")
    print("        break")
    print()

    print("실행 결과:")
    print("Hello, World!")
    print("Hello, World!")
    print("Hello, World!")
    print()

    print("설명:")
    print("while True는 조건이 항상 참이므로 무한히 반복됩니다.")
    print("count가 1씩 증가하다가 3이 되면 if문 조건이 참이 되어")
    print("break가 실행되고 반복문이 종료됩니다.")

    wait_next()


# 사용자가 직접 코드를 따라 작성하는 단계
def example2():
    print()
    print("=== 따라하기 ===")
    print()

    print("코드:")
    print("count = 0")
    print("while True:")
    print("    print(\"반복문!\")")
    print("    count += 1")
    print("    if count == 2:")
    print("        break")
    print()

    print("위 문장을 똑같이 작성하세요.")
    print("(줄바꿈은 ' \\ ' 기호를 사용하세요)")
    print()

    target = r'count=0\whileTrue:\print("반복문!")\count+=1\ifcount==2:\break'

    while True:
        answer = input("코드 입력 : ")

        # 공백 차이를 무시하기 위한 처리
        answer = answer.replace(" ", "")

        if answer == target:
            print()
            print("정답입니다!")
            break

        else:
            print("다시 시도해보세요.")
            print("힌트 : while True와 break, if문의 조건을 확인하세요.")

    wait_next()


# 마지막 실습 문제
def practice():
    print()
    print("=== 최종 실습 ===")
    print()

    print("문제:", end=' ')
    print("while문을 사용하여 1부터 3까지의 숫자를 차례대로 출력하세요.")
    print("(줄바꿈은 ' \\ ' 기호를 사용하세요)")
    print()
    print("1")
    print("2")
    print("3")
    print()

    answer1 = r'count=1\whilecount<=3:\print(count)\count+=1'
    answer2 = r'count=1\whileTrue:\print(count)\count+=1\ifcount>3:\break'

    while True:
        answer = input("작성한 코드를 입력하세요 : ")

        answer = answer.replace(" ", "")

        if answer == answer1 or answer == answer2:
            print()
            print("정답입니다!")
            print("Chapter 5 완료!")
            break

        else:
            print()
            print("정답이 아닙니다.")

            hint = input("힌트가 필요하면 h를 입력하세요 : ")

            if hint.lower() == "h":
                print()
                print("[힌트]")
                print("count 변수를 1로 초기화하세요.")
                print("while count <= 3: 조건으로 반복문을 만드세요.")
                print("반복문 안에서 count를 출력하고, count += 1로 값을 증가시키세요.")


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