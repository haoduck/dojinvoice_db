from selenium.webdriver.common import service as service
from typing import Any

class Service(service.Service):
    def __init__(self, executable_path, port: int = ..., log_path: Any | None = ...) -> None: ...
    def command_line_args(self): ...
    def send_remote_shutdown_command(self) -> None: ...
