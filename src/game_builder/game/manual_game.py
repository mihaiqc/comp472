from game_builder.game.abstract_game import AbstractGame
from game_builder.game.abstract_game import CommandEnum


class ManualGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        """
        runs the game on manual mode

        1) While the game isn't completed, accept a user's inputs
        2) Validate the user's inputs. If not correct then re-prompt
        3) If user's input is valid then move on the board
        4) When the game is cleared the return a success message to the command line

        :return: None
        """

        while not self._board.game_cleared():
            while True:
                self._board.display()
                input_str = input('\nEnter you next move. (u, r, d, l)')
                if ManualGame.__validate_input(input_str):
                    self._move(input_str)
                    break
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        self._board.display()
        print("\n++++++++++++++++++++++++++++++++++++++++++")
        print('You have cleared the game!')

    def _move(self, input_str):
        """
        Moves the empty cell up, left, down, or right based on input_str
        UP: 'u'
        DOWN: 'd'
        LEFT: 'l'
        RIGHT: 'r'

        :param input_str: string
        :return: None
        """

        if input_str == CommandEnum.LEFT:
            self._board.move_left()

        elif input_str == CommandEnum.RIGHT:
            self._board.move_right()

        elif input_str == CommandEnum.UP:
            self._board.move_up()

        elif input_str == CommandEnum.DOWN:
            self._board.move_down()

    @staticmethod
    def __validate_input(input_str):
        """
        Validates the input string of the user

        1) Iterate CommandEnum list
        2) if iterated variable matches input_str then return True
        3) else return False if no matches are found

        :param input_str: string
        :return: boolean
        """

        for variable in CommandEnum.MOVES:
            if variable == input_str:
                return True
        print('invalid input')
        return False
