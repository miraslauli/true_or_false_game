from pathlib import Path
from src.enums import GameStatus
from src.errors import InvalidOperationException


class TrueOrFalse:
    def __init__(self):
        self.questions: dict[int: list[str]] = {}  # type: ignore
        self.game_file = Path("questions_data", "Questions.csv")
        self.number_of_attempts: int = 3  # type: ignore
        self.current_question: int = 0  # type: ignore
        self.game_status = GameStatus.NOT_STARTED

    def question_generation(self) -> str:   # Should add a description of the functions

        with open(self.game_file, "r") as game_file:
            self.questions = {i: line.rstrip().split(";") for i, line in enumerate(game_file)}

        self.game_status = GameStatus.IN_PROGRESS

        return f"The questions have been generated"

    def question(self) -> str:
        user_question = self.questions[self.current_question]
        return user_question[0]

    def path_to_file(self, file: str) -> str:
        self.game_file = Path(file)
        return f"Path to file: {self.game_file}"

    def set_the_number_of_attempts(self, number: int) -> str:
        self.number_of_attempts = number
        return f"The number of attempts: {self.number_of_attempts}"

    def next_question(self) -> str:
        self.current_question += 1

        try:
            self.questions[self.current_question]
        except KeyError:
            self.game_status = GameStatus.WON
            return "You win!"

        return f"Current question: {self.current_question + 1}"

    def give_answer(self, answer: str) -> str:

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(
                f"Inappropriate status of game: {self.game_status}"
            )

        user_question = self.questions[self.current_question]
        if answer == user_question[1]:
            return f"This is the correct answer. {user_question[2]}"
        else:
            self.number_of_attempts -= 1

            if self.number_of_attempts == 0:
                self.game_status = GameStatus.LOST
                print(f"That's the wrong answer. {user_question[2]}")
                return "You lost!"

            return f"That's the wrong answer. {user_question[2]}"

    @property
    def check_game_status(self):
        return self.game_status
