from src.api.true_or_false import TrueOrFalse
from src.enums import GameStatus


game = TrueOrFalse()

game.activate_the_game()
game.generate_questions()
game.set_the_number_of_attempts(int(input("Set the number of attempts: ")))
print(f"The number of attempts: {game.number_of_attempts}")

while game.game_status == GameStatus.IN_PROGRESS:
    game.check_game_status()
    print(game.question())

    answer = input("Enter your answer: ")
    game.check_the_answer(answer)

    game.victory_check()

    if game.game_status == GameStatus.WON:
        print("You win!")
    elif game.game_status == GameStatus.LOST:
        print("You lost!")
    elif game.game_status == GameStatus.IN_PROGRESS:
        game.next_question()



