from .input_device import InputDevice as InputDevice
from .interaction import POINTER as POINTER, POINTER_KINDS as POINTER_KINDS
from selenium.common.exceptions import InvalidArgumentException as InvalidArgumentException
from selenium.webdriver.remote.webelement import WebElement as WebElement
from typing import Any

class PointerInput(InputDevice):
    DEFAULT_MOVE_DURATION: int
    type: Any
    kind: Any
    name: Any
    def __init__(self, kind, name) -> None: ...
    def create_pointer_move(self, duration=..., x: Any | None = ..., y: Any | None = ..., origin: Any | None = ...) -> None: ...
    def create_pointer_down(self, button) -> None: ...
    def create_pointer_up(self, button) -> None: ...
    def create_pointer_cancel(self) -> None: ...
    def create_pause(self, pause_duration) -> None: ...
    def encode(self): ...
