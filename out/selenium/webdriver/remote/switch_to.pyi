from .command import Command as Command
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException, NoSuchFrameException as NoSuchFrameException, NoSuchWindowException as NoSuchWindowException
from selenium.webdriver.common.alert import Alert as Alert
from selenium.webdriver.common.by import By as By
from typing import Any

basestring = str

class SwitchTo:
    def __init__(self, driver) -> None: ...
    @property
    def active_element(self): ...
    @property
    def alert(self): ...
    def default_content(self) -> None: ...
    def frame(self, frame_reference) -> None: ...
    def new_window(self, type_hint: Any | None = ...) -> None: ...
    def parent_frame(self) -> None: ...
    def window(self, window_name) -> None: ...