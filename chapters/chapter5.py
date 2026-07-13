# Chapter 5 : 반복문(loop)

STEPS = [
    {
        "type": "explain",
        "title": "Chapter 5 : 반복문(loop)",
        "body": "[학습 목표]\n"
                "while문을 사용하여 조건에 따라 코드를 반복 실행할 수 있다.\n\n"
                "[개념 설명]\n"
                "반복문은 정해진 조건을 만족하는 동안 코드를 여러 번 실행합니다.\n"
                "while 조건: 형태로 작성하며, 조건이 참(True)인 동안 반복합니다.\n\n"
                "예 :\ncount = 1\nwhile count <= 3:\n    print(count)\n    count += 1\n\n"
                "조건 없이 무조건 반복하고 싶다면 while True: 를 사용합니다.\n"
                "이 경우 반복을 멈추려면 break문을 사용해야 합니다.\n\n"
                "예 :\nwhile True:\n    print('반복')\n    break",
    },
    {
        "type": "explain",
        "title": "예제 1",
        "body": "코드:\ncount = 0\nwhile True:\n"
                "    print(\"Hello, World!\")\n"
                "    count += 1\n"
                "    if count == 3:\n"
                "        break\n\n"
                "실행 결과:\nHello, World!\nHello, World!\nHello, World!\n\n"
                "설명:\nwhile True는 조건이 항상 참이므로 무한히 반복됩니다. "
                "\ncount가 1씩 증가하다가 3이 되면 if문 조건이 참이 되어 \nbreak가 실행되고 반복문이 종료됩니다.",
    },
    {
        "type": "quiz",
        "title": "따라하기",
        "prompt": "다음 코드를 똑같이 작성하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "count = 0\nwhile True:\n    print(\"반복문!\")\n    count += 1\n    if count == 2:\n        break",
        "answers": [
            r'count=0\whileTrue:\print("반복문!")\count+=1\ifcount==2:\break',
        ],
        "hint": "while True와 break, if문의 조건을 확인하세요.",
        "exp": 5,
    },
    {
        "type": "quiz",
        "title": "최종 실습",
        "prompt": "while문을 사용하여 1부터 3까지의 숫자를 차례대로 출력하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "실행 결과:\n1\n2\n3",
        "answers": [
            r"count=1\whilecount<=3:\print(count)\count+=1",
            r"count=1\whileTrue:\print(count)\count+=1\ifcount>3:\break",
        ],
        "hint": "count 변수를 1로 초기화하세요. while count <= 3: 조건으로 반복문을 만드세요. "
                "\n반복문 안에서 count를 출력하고, count += 1로 값을 증가시키세요.",
        "exp": 15,
    },
]