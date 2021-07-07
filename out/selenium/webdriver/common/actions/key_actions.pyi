from ..utils import keys_to_typing as keys_to_typing
from .interaction import Interaction as Interaction, KEY as KEY
from .key_input import KeyInput as KeyInput
from typing import Any

class KeyActions(Interaction):
    source: Any
    def __init__(self, source: Any | None = ...) -> None: ...
    def key_down(self, letter): ...
    def key_up(self, letter): ...
    def pause(self, duration: int = ...): ...
    def send_keys(self, text): ...
