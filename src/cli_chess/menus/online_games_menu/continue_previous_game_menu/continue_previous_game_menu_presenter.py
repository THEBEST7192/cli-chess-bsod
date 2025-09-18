from __future__ import annotations

from cli_chess.menus import MenuPresenter
from typing import TYPE_CHECKING
from cli_chess.utils.logging import log
from cli_chess.core.api.api_manager import api_client, api_is_ready
from cli_chess.core.game.online_game.online_game_presenter import OnlineGamePresenter
from cli_chess.core.game.online_game.online_game_model import OnlineGameModel
from cli_chess.utils.ui_common import change_views
from cli_chess.core.game.game_options import GameOption
from prompt_toolkit.application import Application

if TYPE_CHECKING:
    from .continue_previous_game_menu_model import ContinuePreviousGameMenuModel
    from .continue_previous_game_menu_view import ContinuePreviousGameMenuView


class ContinuePreviousGameMenuPresenter(MenuPresenter):
    """Handles the presentation logic for the Continue Previous Games menu."""

    def __init__(self, model: "ContinuePreviousGameMenuModel", view: "ContinuePreviousGameMenuView"):
        super().__init__(model, view)

    def on_enter(self):
        """Called when the menu is entered."""
        self.model.refresh_menu()

    def continue_game(self):
        game_id = self.selection
        if game_id:
            try:
                log.debug(f"Attempting to continue game with ID: {game_id}")
                game_data = api_client.games.export(game_id)
                log.debug(f"Retrieved game data: {game_data}")

                # Determine if the game is against AI
                is_vs_ai = game_data.get("opponent", {}).get("ai", False)

                # Determine the color the user is playing as
                current_user_id = api_client.account.get()['id']
                play_as_color = None
                for color, player_data in game_data['players'].items():
                    if player_data.get('user', {}).get('id') == current_user_id:
                        play_as_color = color
                        break

                if not play_as_color:
                    log.error(f"Could not determine player color for game {game_id}")
                    return

                # Construct game_parameters in the format expected by OnlineGameModel
                clock_data = game_data.get('clock', {})
                initial_time = clock_data.get('initial', 0)
                increment_time = clock_data.get('increment', 0)

                game_parameters = {
                    GameOption.COLOR: play_as_color,
                    GameOption.VARIANT: game_data['variant'],
                    GameOption.TIME_CONTROL: [initial_time, increment_time],
                    "fen": game_data.get('fen', "")
                }

                online_game_model = OnlineGameModel(game_parameters, is_vs_ai)
                online_game_presenter = OnlineGamePresenter(online_game_model)
                change_views(online_game_presenter.view, online_game_presenter.view.input_field_container)

                log.debug("Calling online_game_model._start_game()")
                online_game_model._start_game(game_id)
                log.debug("Game continuation process completed successfully.")
            except Exception as e:
                log.exception(f"Failed to continue game {game_id}: {e}")