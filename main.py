# chapters 패키지: 각 챕터는 start() 함수로 학습 내용을 실행합니다.
from chapters import chapter0, chapter1, chapter2, chapter3, chapter4, chapter5, chapter6

#각 챕터를 저장하는 딕셔너리
#시험에서 튜플 틀려서 여기서라도 복습함 ㅜㅜ
CHAPTERS = {
    "0": ("출력(print)", chapter0),
    "1": ("변수(variable)", chapter1),
    "2": ("입력(input)", chapter2),
    "3": ("연산자(operator)", chapter3),
    "4": ("조건문(if)", chapter4),
    "5": ("반복문(loop)", chapter5),
    "6": ("함수(function)", chapter6),
}

# 메뉴를 보여주는 함수
def show_menu():
    print()
    print("=== Python Learning ===")
    print()
    # 각 챕터의 번호와 제목을 출력합니다.
    for key, value in CHAPTERS.items():
        title = value[0]
        print(f"{key}. {title}")

    print("q. 종료")
    print()

# 각 챕터를 실행하는 함수
def run_chapter(chapter_module):
    chapter_module.start()

# 프로그램의 메인 루프
def main():
    while True:
        show_menu()
        # 사용자 입력을 받아 학습할 챕터를 선택합니다.
        # strip() 메서드를 사용하여 입력값의 앞뒤 공백을 제거하고, lower() 메서드를 사용하여 소문자로 변환합니다.
        choice = input("학습할 챕터를 선택하세요: ").strip().lower()

        if choice == "q":
            print("프로그램을 종료합니다.")
            # 프로그램 종료
            break
        # 사용자가 선택한 챕터가 CHAPTERS 딕셔너리에 있는지 확인합니다.
        if choice in CHAPTERS:
            # 선택한 챕터의 모듈을 가져와서 실행합니다.
            chapter = CHAPTERS[choice]
            # chapter 변수는 튜플 형태로 (제목, 모듈)로 되어 있으므로, 모듈을 가져오기 위해 인덱스 1을 사용합니다.
            module = chapter[1]
            # 선택한 챕터의 start() 함수를 호출하여 학습 내용을 실행합니다.
            run_chapter(module)
        else:
            print("잘못된 입력입니다. 다시 선택해 주세요.")

# 프로그램이 직접 실행될 때만 main() 함수를 호출하도록 합니다.
# 다른 파일에서 import할 경우 자동 실행되지 않도록 방지
if __name__ == "__main__":
    #main() 함수를 호출하여 프로그램을 시작합니다.
    main()
