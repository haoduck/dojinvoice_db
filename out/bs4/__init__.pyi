from .element import Tag
from typing import Any

class GuessedAtParserWarning(UserWarning): ...
class MarkupResemblesLocatorWarning(UserWarning): ...

class BeautifulSoup(Tag):
    ROOT_TAG_NAME: str
    DEFAULT_BUILDER_FEATURES: Any
    ASCII_SPACES: str
    NO_PARSER_SPECIFIED_WARNING: str
    element_classes: Any
    builder: Any
    is_xml: Any
    known_xml: Any
    parse_only: Any
    markup: Any
    def __init__(self, markup: str = ..., features: Any | None = ..., builder: Any | None = ..., parse_only: Any | None = ..., from_encoding: Any | None = ..., exclude_encodings: Any | None = ..., element_classes: Any | None = ..., **kwargs): ...
    def __copy__(self): ...
    hidden: int
    current_data: Any
    currentTag: Any
    tagStack: Any
    open_tag_counter: Any
    preserve_whitespace_tag_stack: Any
    string_container_stack: Any
    def reset(self) -> None: ...
    def new_tag(self, name, namespace: Any | None = ..., nsprefix: Any | None = ..., attrs=..., sourceline: Any | None = ..., sourcepos: Any | None = ..., **kwattrs): ...
    def string_container(self, base_class: Any | None = ...): ...
    def new_string(self, s, subclass: Any | None = ...): ...
    def insert_before(self, *args) -> None: ...
    def insert_after(self, *args) -> None: ...
    def popTag(self): ...
    def pushTag(self, tag) -> None: ...
    def endData(self, containerClass: Any | None = ...) -> None: ...
    def object_was_parsed(self, o, parent: Any | None = ..., most_recent_element: Any | None = ...) -> None: ...
    def handle_starttag(self, name, namespace, nsprefix, attrs, sourceline: Any | None = ..., sourcepos: Any | None = ...): ...
    def handle_endtag(self, name, nsprefix: Any | None = ...) -> None: ...
    def handle_data(self, data) -> None: ...
    def decode(self, pretty_print: bool = ..., eventual_encoding=..., formatter: str = ...): ...

class BeautifulStoneSoup(BeautifulSoup):
    def __init__(self, *args, **kwargs) -> None: ...

class StopParsing(Exception): ...
class FeatureNotFound(ValueError): ...