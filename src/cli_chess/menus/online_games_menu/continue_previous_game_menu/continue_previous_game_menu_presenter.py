from __future__ import annotations

from cli_chess.menus import MenuPresenter
from typing import TYPE_CHECKING
from cli_chess.utils.logging import log
from cli_chess.core.api.api_manager import api_client, api_is_ready

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