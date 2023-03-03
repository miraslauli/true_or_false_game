key: int = 0
questions: dict[int:list[str]] = {}

with open('Questions.csv', 'r') as game_file:
    for line in game_file:
        questions[key] = line.rstrip().split(';')
        key += 1

user_q = questions[0]
print(user_q)
