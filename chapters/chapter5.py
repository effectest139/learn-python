def start():
    print()
    print("=== Chapter 5: 반복문(loop) ===")
    print()
    print("[개념 설명]")
    print("반복문은 같은 작업을 여러 번 실행할 때 사용합니다.")
    print("for 는 정해진 횟수만큼, while 은 조건이 참인 동안 반복합니다.")
    print()
    print("[예제 실행]")
    print("--- for 예제 ---")
    for i in range(1, 4):
        print("i =", i)

    print()
    print("--- while 예제 ---")
    count = 1
    while count <= 3:
        print("count =", count)
        count = count + 1
    print()
    input("엔터를 누르면 메뉴로 돌아갑니다...")
