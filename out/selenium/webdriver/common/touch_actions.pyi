from selenium.webdriver.remote.command import Command as Command

class TouchActions:
    def __init__(self, driver) -> None: ...
    def perform(self) -> None: ...
    def tap(self, on_element): ...
    def double_tap(self, on_element): ...
    def tap_and_hold(self, xcoord, ycoord): ...
    def move(self, xcoord, ycoord): ...
    def release(self, xcoord, ycoord): ...
    def scroll(self, xoffset, yoffset): ...
    def scroll_from_element(self, on_element, xoffset, yoffset): ...
    def long_press(self, on_element): ...
    def flick(self, xspeed, yspeed): ...
    def flick_element(self, on_element, xoffset, yoffset, speed): ...
    def __enter__(self): ...
    def __exit__(self, _type, _value, _traceback) -> None: ...
