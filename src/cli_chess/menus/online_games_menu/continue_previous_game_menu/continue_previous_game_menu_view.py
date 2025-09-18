from __future__ import annotations

from cli_chess.menus import MenuView
from typing import TYPE_CHECKING
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings, KeyBindingsBase

if TYPE_CHECKING:
    from .continue_previous_game_menu_presenter import ContinuePreviousGameMenuPresenter


class ContinuePreviousGameMenuView(MenuView):
    """Handles rendering the Continue Previous Games menu."""

    def __init__(self, presenter: "ContinuePreviousGameMenuPresenter"):
        self.presenter = presenter
        # Width chosen to align reasonably with other menu widths used in the project
        super().__init__(self.presenter, container_width=38)

    def get_function_bar_fragments(self) -> list[FormattedText]:
        return [("class:function-bar.key", "F1"), ("class:function-bar.label", "Continue Game")]

    def get_function_bar_key_bindings(self) -> KeyBindingsBase:
        kb = KeyBindings()
        @kb.add("f1")
        def _(event):
            self.presenter.continue_game()
        return kb