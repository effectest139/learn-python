# Chapter 6 : 함수(function)

STEPS = [
    {
        "type": "explain",
        "title": "Chapter 6 : 함수(function)",
        "body": "[학습 목표]\n"
                "def를 사용하여 함수를 정의하고 호출할 수 있다.\n\n"
                "[개념 설명]\n"
                "함수는 반복해서 사용하는 코드를 하나로 묶어 이름을 붙인 것입니다.\n"
                "def 함수이름(): 형태로 정의하고, 함수이름() 형태로 호출합니다.\n\n"
                "예 :\ndef say_hello():\n    print('안녕하세요!')\n\nsay_hello()\n\n"
                "함수는 매개변수(parameter)를 받아서 사용할 수도 있습니다.\n"
                "예 : def greeting(name): ...\n\n"
                "또한 함수는 결과값을 돌려줄 수 있는데, 이때 return을 사용합니다.\n"
                "예 : return a + b\n\n"
                "참고로, 함수 안에서 만든 변수는 함수 밖에서는 사용할 수 없습니다.\n"
                "(이런 변수의 범위를 지역 변수, 함수 밖의 변수를 전역 변수라고 부릅니다.)",
    },
    {
        "type": "explain",
        "title": "예제 1",
        "body": "코드:\ndef function():\n    print(\"Hello, World!\")\n\nfunction()\n\n"
                "실행 결과: Hello, World!\n\n"
                "설명:\ndef function(): 으로 function이라는 이름의 함수를 정의합니다. "
                "\nfunction() 처럼 함수 이름 뒤에 괄호를 붙여 호출하면, \n함수 안에 작성된 코드가 그때 실행됩니다.",
    },
    {
        "type": "quiz",
        "title": "따라하기",
        "prompt": "다음 코드를 똑같이 작성하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "def greeting(name):\n    print(name + \"님, 안녕하세요!\")\n\ngreeting(\"개발자\")",
        "answers": [
            r'defgreeting(name):\print(name+"님,안녕하세요!")\greeting("개발자")',
        ],
        "hint": "매개변수 name과 문자열 더하기(+)를 확인하세요.",
        "exp": 5,
    },
    {
        "type": "quiz",
        "title": "최종 실습",
        "prompt": "두 개의 숫자를 더한 값을 반환(return)하는 함수 add_numbers(a, b)를 만들고,\n"
                  "이를 사용해 3과 7을 더한 결과를 출력하세요.\n"
                  "(줄바꿈은 ' \\ ' 기호를 사용하세요)\n\n"
                  "실행 결과: 10",
        "answers": [
            r"defadd_numbers(a,b):\returna+b\result=add_numbers(3,7)\print(result)",
        ],
        "hint": "def add_numbers(a, b): 형태로 함수를 정의하고, return a + b로 합을 돌려주세요. "
                "\nresult = add_numbers(3, 7)로 호출하고 print(result)로 출력하세요.",
        "exp": 15,
    },
]