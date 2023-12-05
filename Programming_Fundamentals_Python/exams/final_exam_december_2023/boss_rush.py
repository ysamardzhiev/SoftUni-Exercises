import re


def check_if_valid(boss_and_title: str):
    match = re.search(r"\|[A-Z]{4,}\|:#[a-zA-Z]+\s[a-zA-Z]+#", boss_and_title)
    if match:
        return True
    return False


def isolate_name_and_title(boss_and_title: str):
    name, title = boss_and_title.split(':')
    match_name = re.findall(r"[A-Z]+", name)
    match_title = re.findall(r"[A-Za-z\s]+", title)
    return ''.join(match_name), ''.join(match_title)


n = int(input())

for _ in range(n):
    boss = input()
    if check_if_valid(boss):
        name, title = isolate_name_and_title(boss)
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")