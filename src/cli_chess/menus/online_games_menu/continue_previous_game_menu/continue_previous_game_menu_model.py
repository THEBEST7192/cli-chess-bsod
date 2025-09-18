from __future__ import annotations
from cli_chess.menus import MenuModel, MenuCategory, MenuOption
from cli_chess.core.api.api_manager import api_client, api_is_ready
from cli_chess.utils.logging import log, configure_logger
from enum import Enum
import requests
import json

# Configure a dedicated debug logger
debug_log = configure_logger("current-game-debug")

class NoGameOption(Enum):
    NO_GAMES = "No ongoing games found"


class ContinuePreviousGameMenuModel(MenuModel):
    """Defines the continue previous game menu model"""
    def __init__(self):
        self.menu = self._create_menu()
        super().__init__(self.menu)

    def refresh_menu(self):
        self.menu = self._create_menu()
        self.selected_option_index = 0

    def _create_menu(self) -> MenuCategory:
        ongoing_games = []
        if api_is_ready():
            try:
                debug_log.info("Fetching ongoing games list")
                ongoing_response = api_client.games.get_ongoing()
                for game in ongoing_response:
                    game_id = game.get("gameId")
                    opponent_username = game.get("opponent", {}).get("username")
                    if game_id and opponent_username:
                        color = game.get("color", "Unknown").capitalize()
                        is_my_turn = "(Your Turn)" if game.get("isMyTurn") else ""
                        display_text = f"{color} vs {opponent_username} {is_my_turn}"
                        debug_log.info(f"Adding ongoing game: {display_text}")
                        ongoing_games.append(MenuOption(game_id, "", display_name=display_text))
            except Exception as e:
                debug_log.exception(f"Failed to fetch ongoing games list: {e}")
        else:
            debug_log.warning("API is not ready, cannot fetch games")

        if not ongoing_games:
            debug_log.info("No ongoing games found, adding placeholder option")
            ongoing_games.append(MenuOption(NoGameOption.NO_GAMES, "No ongoing games found"))

        return MenuCategory("Continue Previous Games", ongoing_games)