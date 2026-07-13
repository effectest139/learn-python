# Chapter 1 : 변수(Variable)

STEPS = [
    {
        "type": "explain",
        "title": "Chapter 1 : 변수(Variable)",
        "body": "[학습 목표]\n"
                "변수를 사용하여 값을 저장하고 사용할 수 있다.\n\n"
                "[개념 설명]\n"
                "변수는 값을 저장하는 공간입니다.\n\n"
                "문자열(글자)은 따옴표로 감싸서 작성합니다.\n"
                "예 : world = 'Hello, World!'\n\n"
                "숫자는 따옴표 없이 작성합니다.\n"
                "예 : age = 25",
    },
    {
        "type": "explain",
        "title": "예제 1",
        "body": "코드:\nworld = 'Hello, World!'\nprint(world)\n\n"
                "실행 결과: Hello, World!\n\n"
                "설명:\n변수 world에 문자열 'Hello, World!'를 저장하고, "
                "\nprint() 함수를 사용하여 그 값을 출력합니다.",
    },
    {
        "type": "quiz",
        "title": "따라하기",
        "prompt": "다음 코드를 똑같이 작성하세요.\n\nname = 'snake'",
        "answers": [
            "name='snake'",
            'name="snake"',
        ],
        "hint": "따옴표를 확인하세요",
        "exp": 5,
    },
    {
        "type": "quiz",
        "title": "최종 실습",
        "prompt": "숫자 10을 변수(num)에 저장하고, 그 값을 출력하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "실행 결과: 10",
        "answers": [
            r"num=10\print(num)",
        ],
        "hint": "print() 함수를 사용하고 변수를 만들 때는 \n변수이름 = 저장할값 형태로 작성합니다.",
        "exp": 15,
    },
]