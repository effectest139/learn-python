def start():
    print()
    print("=== Chapter 4: 조건문(if) ===")
    print()
    print("[개념 설명]")
    print("조건문은 특정 조건이 참일 때만 코드를 실행합니다.")
    print("if, elif, else 를 사용해 여러 경우를 나눌 수 있습니다.")
    print()
    print("[예제 실행]")
    score = 85
    print("점수:", score)
    if score >= 90:
        print("등급: A")
    elif score >= 80:
        print("등급: B")
    else:
        print("등급: C")
    print()
    input("엔터를 누르면 메뉴로 돌아갑니다...")
