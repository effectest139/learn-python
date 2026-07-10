# Chapter 0 : 출력(print)
# print() 함수를 배우는 학습 챕터


# 사용자가 엔터를 누르면 다음 단계로 넘어가는 함수
def wait_next():
    input("\n엔터를 누르면 다음 단계로 넘어갑니다...")


# 개념 설명 부분
def explain():
    print()
    print("=== Chapter 0 : 출력(print) ===")
    print()

    print("[학습 목표]")
    print("print() 함수를 사용하여 화면에 글자와 숫자를 출력할 수 있다.")
    print()

    print("[개념 설명]")
    print("print()는 화면에 원하는 내용을 보여주는 함수입니다.")
    print()

    print("문자열(글자)은 따옴표로 감싸서 작성합니다.")
    print("예 : print('Hello')")
    print()

    print("숫자는 따옴표 없이 작성합니다.")
    print("예 : print(100)")
    
    wait_next()


# 예제 1 설명
def example1():
    print()
    print("=== 예제 1 ===")
    print()

    print("다음 코드를 확인해보세요.")
    print()

    print("코드:")
    print("print('Hello, Python!')")
    print()

    print("실행 결과:", end=' ')
    print("Hello, Python!")
    print()

    print("설명:")
    print("print() 안에 있는 글자를 화면에 출력합니다.")

    wait_next()


# 사용자가 직접 코드를 따라 작성하는 단계
def example2():
    print()
    print("=== 따라하기 ===")
    print()

    print("코드: ", end='')
    print("print('첫 파이썬 프로그램입니다.')")
    print()

    print("위 문장을 똑같이 작성하세요.")
    print()

    while True:
        answer = input("코드 입력 : ")

        # 공백 차이를 무시하기 위한 처리
        answer = answer.replace(" ", "")

        if answer == "print('첫파이썬프로그램입니다.')" or answer == 'print("첫파이썬프로그램입니다."")':
            print()
            print("정답입니다!")
            break

        else:
            print("다시 시도해보세요.")
            print("힌트 : 따옴표를 확인하세요")

    wait_next()


# 마지막 실습 문제
def practice():
    print()
    print("=== 최종 실습 ===")
    print()

    print("문제:", end=' ')
    print("화면에 다음 문장을 출력하세요.")
    print()
    print("파이썬은 재미있다!")
    print()

    while True:
        answer = input("작성한 코드를 입력하세요 : ")

        answer = answer.replace(" ", "")

        if answer == "print('파이썬은재미있다!')" or answer == 'print("파이썬은재미있다!")':
            print()
            print("정답입니다!")
            print("Chapter 0 완료!")
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