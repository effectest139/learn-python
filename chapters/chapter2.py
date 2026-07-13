# Chapter 2 : 입력(input)

STEPS = [
    {
        "type": "explain",
        "title": "Chapter 2 : 입력(input)",
        "body": "[학습 목표]\n"
                "input() 함수를 사용하여 사용자로부터 데이터를 입력받을 수 있다.\n\n"
                "[개념 설명]\n"
                "input()는 사용자로부터 키보드 입력을 받는 함수입니다.\n\n"
                "괄호 안에 문자열을 넣으면, 그 문자열이 사용자에게 보여집니다.\n"
                "예 : answer = input('질문을 입력하세요: ')\n\n"
                "입력된 데이터는 문자열 형태로 저장됩니다.\n"
                "예 : age = input('나이를 입력하세요: ')",
    },
    {
        "type": "explain",
        "title": "예제 1",
        "body": "코드:\nname = input('이름을 입력하세요: ')\nprint(name)\n\n"
                "실행 결과: <입력된 이름>\n\n"
                "설명:\ninput() 함수를 사용하여 사용자로부터 데이터를 입력받습니다.",
    },
    {
        "type": "quiz",
        "title": "따라하기",
        "prompt": "다음 코드를 똑같이 작성하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "name = input('이름을 입력하세요: ')\n"
                  "print('환영합니다,', name)",
        "answers": [
            r"name=input('이름을입력하세요:')\print('환영합니다,',name)",
        ],
        "hint": "따옴표를 확인하세요.",
        "exp": 5,
    },
    {
        "type": "quiz",
        "title": "최종 실습",
        "prompt": "사용자로부터 좋아하는 과일을 입력받아 'fruit' 변수에 저장하고\n"
                  "그 값을 출력하는 코드를 작성하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "실행 결과: <입력된 과일>",
        "answers": [
            r"fruit=input()\print(fruit)",
            r"fruit=input('좋아하는과일을입력하세요:')\print(fruit)",
        ],
        "hint": "input() 함수를 사용하여 사용자로부터 \n데이터를 입력받고 출력은 print() 함수를 사용합니다.",
        "exp": 15,
    },
]