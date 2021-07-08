from selenium.common.exceptions import WebDriverException as WebDriverException
from selenium.webdriver.common import utils as utils
from typing import Any

class FirefoxBinary:
    NO_FOCUS_LIBRARY_NAME: str
    command_line: Any
    def __init__(self, firefox_path: Any | None = ..., log_file: Any | None = ...) -> None: ...
    def add_command_line_options(self, *args) -> None: ...
    profile: Any
    def launch_browser(self, profile, timeout: int = ...) -> None: ...
    def kill(self) -> None: ...
    def which(self, fname): ...