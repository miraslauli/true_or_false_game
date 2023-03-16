from pathlib import Path

from src.enums import GameStatus
from src.errors import InvalidOperationException
from src.config import number_of_attempts


class TrueOrFalse:
    def __init__(self):
        self.questions: dict[int : list[str]] = {}
        self.game_file = Path("questions_data", "Questions.csv")
        self.number_of_attempts: int = number_of_attempts
        self.current_question: int = 0
        self.game_status = GameStatus.NOT_STARTED

    def generate_questions(self) -> None:
        with open(self.game_file, "r") as game_file:
            self.questions = {
                i: line.rstrip().split(";") for i, line in enumerate(game_file)
            }

    def activate_the_game(self) -> None:
        self.game_status = GameStatus.IN_PROGRESS

    def question(self) -> str:
        user_question = self.questions[self.current_question]
        return user_question[0]

    def set_the_file_path(self, file: str) -> None:
        self.game_file = Path(file)
        print(f"Path to file: {self.game_file}")

    def set_the_number_of_attempts(self, number: int) -> None:
        self.number_of_attempts = number

    def next_question(self) -> None:
        last_question = len(self.questions) - 1
        if self.current_question < last_question:
            self.current_question += 1
        else:
            self.game_status = GameStatus.WON

    def defeat_check(self) -> None:
        if self.number_of_attempts == 0:
            self.game_status = GameStatus.LOST

    def check_the_answer(self, answer) -> None:
        user_question = self.questions[self.current_question]
        if answer == user_question[1]:
            print(f"This is the correct answer. {user_question[2]}")
        else:
            self.number_of_attempts -= 1
            print(f"That's the wrong answer. {user_question[2]}")

    def check_game_status(self) -> None:
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(
                f"Inappropriate status of game: {self.game_status}"
            )
