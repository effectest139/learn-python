def greet(name):
    return "안녕하세요, " + name + "님!"


def add(a, b):
    return a + b


def start():
    print()
    print("=== Chapter 6: 함수(function) ===")
    print()
    print("[개념 설명]")
    print("함수는 자주 사용하는 코드를 이름으로 묶어 둔 것입니다.")
    print("def 키워드로 함수를 만들고, return 으로 결과를 돌려줄 수 있습니다.")
    print()
    print("[예제 실행]")
    message = greet("파이썬")
    print(message)
    result = add(7, 3)
    print("7 + 3 =", result)
    print()
    input("엔터를 누르면 메뉴로 돌아갑니다...")
