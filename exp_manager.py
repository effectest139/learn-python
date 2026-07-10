# 경험치(EXP) 관리 모듈
# user_exp.txt 파일에 경험치를 저장하고 불러옵니다.

import os

# 챕터 파일들과 같은 폴더(chapters/)에 경험치 파일을 저장합니다.
EXP_FILE = os.path.join(os.path.dirname(__file__), "chapters", "user_exp.txt")


def load_exp():
    # user_exp.txt를 읽어서 현재 경험치(int)를 반환
    # 파일이 없거나 형식이 깨져 있으면 0을 반환하고 파일을 새로 생성
    try:
        with open(EXP_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

        for line in content.splitlines():
            line = line.strip()
            if line.startswith("exp="):
                value = line.split("=", 1)[1].strip()
                return int(value)

        save_exp(0)
        return 0

    except (FileNotFoundError, ValueError, OSError):
        save_exp(0)
        return 0


def save_exp(exp):
    # 전달받은 경험치 값을 user_exp.txt에 저장
    with open(EXP_FILE, "w", encoding="utf-8") as file:
        file.write(f"exp={exp}\n")


def add_exp(amount):
    # 현재 경험치를 불러와 amount만큼 더한 뒤 저장
    # 갱신된 경험치(int)를 반환
    current_exp = load_exp()
    new_exp = current_exp + amount
    save_exp(new_exp)
    print(f"\n[경험치 획득] +{amount} EXP (현재 경험치: {new_exp})\n")
    return new_exp
