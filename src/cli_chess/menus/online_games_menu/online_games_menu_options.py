from enum import Enum


class OnlineGamesMenuOptions(Enum):
    """Enum defining the main options for the Online Games menu"""

    CREATE_GAME = "Create a game"
    CONTINUE_PREVIOUS_GAME = "Continue Game"
    VS_COMPUTER_ONLINE = "Play vs Computer"
    WATCH_LICHESS_TV = "Watch Lichess TV"