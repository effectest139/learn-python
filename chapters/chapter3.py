# Chapter 3 : 연산자(operator)

STEPS = [
    {
        "type": "explain",
        "title": "Chapter 3 : 연산자(operator)",
        "body": "[학습 목표]\n"
                "연산자를 사용하여 값을 계산하고 비교할 수 있다.\n\n"
                "[개념 설명]\n"
                "연산자는 값을 계산하거나 비교할 때 사용합니다.\n"
                "예 : +, -, *, / 는 사칙연산, ==, !=, >, < 는 비교 연산자입니다.\n\n"
                "값을 계산해서 변수에 저장할 수도 있습니다.\n"
                "예 : sum = 5 + 3\n\n"
                "다른 문법과 함께 사용하여 조건문과 반복문을 만들 수 있습니다.\n"
                "예 : if score >= 60:\n    print('합격')",
    },
    {
        "type": "explain",
        "title": "예제 1",
        "body": "코드:\nprint(10+5)\n\n"
                "실행 결과: 15\n\n"
                "설명:\nprint() 안에 있는 값을 더하여 화면에 출력합니다.",
    },
    {
        "type": "quiz",
        "title": "따라하기",
        "prompt": "다음 코드를 똑같이 작성하세요.\n\nprint(20-7)",
        "answers": [
            "print(20-7)",
        ],
        "hint": "연산자 '-'를 확인하세요.",
        "exp": 5,
    },
    {
        "type": "quiz",
        "title": "최종 실습",
        "prompt": "가로 길이(width) 5와 세로 길이(height) 8을 변수에 저장하고\n"
                  "가로 길이와 세로 길이를 곱하여 넓이(area)를 계산하고 출력하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "실행 결과: 40",
        "answers": [
            r"width=5\height=8\area=width*height\print(area)",
            r"width=5\height=8\print(width*height)",
        ],
        "hint": "가로 길이와 세로 길이를 곱하면 넓이를 구할 수 있습니다. "
                "\n연산자 '*'를 사용하고, 넓이 변수를 area로 지정하여 print()로 출력하세요.",
        "exp": 15,
    },
]