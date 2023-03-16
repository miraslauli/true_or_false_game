from src.api.true_or_false import TrueOrFalse
from src.enums import GameStatus


def main():
    game = TrueOrFalse()

    game.activate_the_game()
    game.check_game_status()
    game.generate_questions()
    game.set_the_number_of_attempts(int(input("Set the number of attempts: ")))
    print(f"The number of attempts: {game.number_of_attempts}")

    while game.game_status == GameStatus.IN_PROGRESS:
        print(game.question())

        answer = input("Enter your answer: ")
        game.check_the_answer(answer)

        game.defeat_check()
        game.next_question()

        if game.game_status == GameStatus.WON:
            print("You win!")
            break
        elif game.game_status == GameStatus.LOST:
            print("You lost!")
            break

        print(f"The next question is number {game.current_question + 1}")


main()
