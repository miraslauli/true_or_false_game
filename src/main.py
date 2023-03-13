from src.api.true_or_false import TrueOrFalse
from src.enums import GameStatus


game = TrueOrFalse()

print(game.question_generation())
print(game.set_the_number_of_attempts(int(input("Set the number of attempts: "))))
print(game.check_game_status)

while game.game_status == GameStatus.IN_PROGRESS:

    print(game.question())
    print(game.give_answer(input("Enter your answer: ")))
    game.next_question()

