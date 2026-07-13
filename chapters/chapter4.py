# Chapter 4 : 조건문(if, else)

STEPS = [
    {
        "type": "explain",
        "title": "Chapter 4 : 조건문(if, else)",
        "body": "[학습 목표]\n"
                "if문과 else문을 사용하여 조건에 따라 다른 코드를 실행할 수 있다.\n\n"
                "[개념 설명]\n"
                "if문은 특정 조건이 참일 때만 코드를 실행합니다.\n\n"
                "다음과 같이 작성합니다.\n"
                "예 : if (조건문):\n\n"
                "조건문에는 비교 연산자를 사용하여 값을 비교할 수 있습니다.\n"
                "예 : if score >= 60:\n\n"
                "[추가 개념: else]\n"
                "조건문이 거짓(False)일 때 다른 코드를 실행하고 싶다면 else:를 사용합니다.\n"
                "예 :\nif score >= 60:\n    print('합격')\nelse:\n    print('불합격')",
    },
    {
        "type": "explain",
        "title": "예제 1",
        "body": "코드:\nif True:\n    print('Hello, World!')\nelse:\n    print('Bye, World!')\n\n"
                "실행 결과: Hello, World!\n\n"
                "설명:\nif문은 조건이 참일 때만 코드를 실행합니다. "
                "위 예제에서는 \n조건이 항상 참(True)이므로 'Hello, World!'가 출력되고 else 코드는 무시됩니다.",
    },
    {
        "type": "quiz",
        "title": "따라하기",
        "prompt": "다음 코드를 똑같이 작성하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "if True:\n    print('Hello, World!')",
        "answers": [
            r"ifTrue:\print('Hello,World!')",
            r'ifTrue:\print("Hello,World!")',
        ],
        "hint": "조건문은 True로 작성하고,\n print() 안에 'Hello, World!'를 넣어보세요.",
        "exp": 5,
    },
    {
        "type": "quiz",
        "title": "최종 실습",
        "prompt": "사용자로부터 'number'를 입력받고\n"
                  "number 값이 0보다 크면 '양수'를, \n그렇지 않으면 '음수 또는 0'을 출력하는 코드를 작성하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "예시 출력: 양수",
        "answers": [
            r"number=int(input())\ifnumber>0:\print('양수')\else:\print('음수또는0')",
        ],
        "hint": "input()으로 입력받은 값은 문자열이므로 int()로 숫자로 바꿔주세요. "
                "\nif number > 0: 과 else: 를 사용하여 양수/음수를 구분하세요.",
        "exp": 15,
    },
]