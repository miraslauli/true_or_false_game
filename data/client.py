from true_or_false_API import TrueOrFalse
from game_status import GameStatus


game = TrueOrFalse()

print(game.question_generation())
print(game.set_the_number_of_attempts(int(input('Set the number of attempts: '))))
print(game.check_game_status)

while game.game_status == GameStatus.IN_PROGRESS:

    print(game.question())
    print(game.give_answer(input('Enter your answer: ')))
    game.next_question()