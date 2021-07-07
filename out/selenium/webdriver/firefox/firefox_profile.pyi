from selenium.common.exceptions import WebDriverException as WebDriverException
from typing import Any

WEBDRIVER_EXT: str
WEBDRIVER_PREFERENCES: str
EXTENSION_NAME: str

class AddonFormatError(Exception): ...

class FirefoxProfile:
    ANONYMOUS_PROFILE_NAME: str
    DEFAULT_PREFERENCES: Any
    default_preferences: Any
    profile_dir: Any
    tempfolder: Any
    extensionsDir: Any
    userPrefs: Any
    def __init__(self, profile_directory: Any | None = ...) -> None: ...
    def set_preference(self, key, value) -> None: ...
    def add_extension(self, extension=...) -> None: ...
    def update_preferences(self) -> None: ...
    @property
    def path(self): ...
    @property
    def port(self): ...
    @port.setter
    def port(self, port) -> None: ...
    @property
    def accept_untrusted_certs(self): ...
    @accept_untrusted_certs.setter
    def accept_untrusted_certs(self, value) -> None: ...
    @property
    def assume_untrusted_cert_issuer(self): ...
    @assume_untrusted_cert_issuer.setter
    def assume_untrusted_cert_issuer(self, value) -> None: ...
    @property
    def encoded(self): ...
