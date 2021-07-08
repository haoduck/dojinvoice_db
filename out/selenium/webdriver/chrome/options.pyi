from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DesiredCapabilities
from selenium.webdriver.common.options import ArgOptions as ArgOptions

class Options(ArgOptions):
    KEY: str
    def __init__(self) -> None: ...
    @property
    def binary_location(self): ...
    @binary_location.setter
    def binary_location(self, value) -> None: ...
    @property
    def debugger_address(self): ...
    @debugger_address.setter
    def debugger_address(self, value) -> None: ...
    @property
    def extensions(self): ...
    def add_extension(self, extension) -> None: ...
    def add_encoded_extension(self, extension) -> None: ...
    @property
    def experimental_options(self): ...
    def add_experimental_option(self, name, value) -> None: ...
    @property
    def headless(self): ...
    @headless.setter
    def headless(self, value) -> None: ...
    def to_capabilities(self): ...
    @property
    def default_capabilities(self): ...