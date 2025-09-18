from cli_chess.menus import MenuModel, MenuOption, MenuCategory
from cli_chess.menus.online_games_menu.online_games_menu_options import OnlineGamesMenuOptions


class OnlineGamesMenuModel(MenuModel):
    def __init__(self):
        self.menu = self._create_menu()
        super().__init__(self.menu)

    @staticmethod
    def _create_menu() -> MenuCategory:
        """Create the menu options"""
        menu_options = [
            MenuOption(OnlineGamesMenuOptions.CREATE_GAME, "Create an online game against a random opponent"),
            MenuOption(OnlineGamesMenuOptions.CONTINUE_PREVIOUS_GAME, "Continue an ongoing game"),
            MenuOption(OnlineGamesMenuOptions.VS_COMPUTER_ONLINE, "Play online against the computer"),
            MenuOption(OnlineGamesMenuOptions.WATCH_LICHESS_TV, "Watch top rated Lichess players compete live"),
        ]

        return MenuCategory("Online Games", menu_options)
