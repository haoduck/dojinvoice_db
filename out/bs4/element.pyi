from bs4.formatter import Formatter as Formatter, HTMLFormatter as HTMLFormatter, XMLFormatter as XMLFormatter
from typing import Any

DEFAULT_OUTPUT_ENCODING: str
PY3K: Any
nonwhitespace_re: Any
whitespace_re: Any
PYTHON_SPECIFIC_ENCODINGS: Any

class NamespacedAttribute(str):
    def __new__(cls, prefix, name: Any | None = ..., namespace: Any | None = ...): ...

class AttributeValueWithCharsetSubstitution(str): ...

class CharsetMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    def __new__(cls, original_value): ...
    def encode(self, encoding): ...

class ContentMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    CHARSET_RE: Any
    def __new__(cls, original_value): ...
    def encode(self, encoding): ...

class PageElement:
    parent: Any
    previous_element: Any
    next_element: Any
    next_sibling: Any
    previous_sibling: Any
    def setup(self, parent: Any | None = ..., previous_element: Any | None = ..., next_element: Any | None = ..., previous_sibling: Any | None = ..., next_sibling: Any | None = ...) -> None: ...
    def format_string(self, s, formatter): ...
    def formatter_for_name(self, formatter): ...
    nextSibling: Any
    previousSibling: Any
    def replace_with(self, replace_with): ...
    replaceWith: Any
    def unwrap(self): ...
    replace_with_children: Any
    replaceWithChildren: Any
    def wrap(self, wrap_inside): ...
    def extract(self, _self_index: Any | None = ...): ...
    def insert(self, position, new_child) -> None: ...
    def append(self, tag) -> None: ...
    def extend(self, tags) -> None: ...
    def insert_before(self, *args) -> None: ...
    def insert_after(self, *args) -> None: ...
    def find_next(self, name: Any | None = ..., attrs=..., text: Any | None = ..., **kwargs): ...
    findNext: Any
    def find_all_next(self, name: Any | None = ..., attrs=..., text: Any | None = ..., limit: Any | None = ..., **kwargs): ...
    findAllNext: Any
    def find_next_sibling(self, name: Any | None = ..., attrs=..., text: Any | None = ..., **kwargs): ...
    findNextSibling: Any
    def find_next_siblings(self, name: Any | None = ..., attrs=..., text: Any | None = ..., limit: Any | None = ..., **kwargs): ...
    findNextSiblings: Any
    fetchNextSiblings: Any
    def find_previous(self, name: Any | None = ..., attrs=..., text: Any | None = ..., **kwargs): ...
    findPrevious: Any
    def find_all_previous(self, name: Any | None = ..., attrs=..., text: Any | None = ..., limit: Any | None = ..., **kwargs): ...
    findAllPrevious: Any
    fetchPrevious: Any
    def find_previous_sibling(self, name: Any | None = ..., attrs=..., text: Any | None = ..., **kwargs): ...
    findPreviousSibling: Any
    def find_previous_siblings(self, name: Any | None = ..., attrs=..., text: Any | None = ..., limit: Any | None = ..., **kwargs): ...
    findPreviousSiblings: Any
    fetchPreviousSiblings: Any
    def find_parent(self, name: Any | None = ..., attrs=..., **kwargs): ...
    findParent: Any
    def find_parents(self, name: Any | None = ..., attrs=..., limit: Any | None = ..., **kwargs): ...
    findParents: Any
    fetchParents: Any
    @property
    def next(self): ...
    @property
    def previous(self): ...
    @property
    def next_elements(self) -> None: ...
    @property
    def next_siblings(self) -> None: ...
    @property
    def previous_elements(self) -> None: ...
    @property
    def previous_siblings(self) -> None: ...
    @property
    def parents(self) -> None: ...
    @property
    def decomposed(self): ...
    def nextGenerator(self): ...
    def nextSiblingGenerator(self): ...
    def previousGenerator(self): ...
    def previousSiblingGenerator(self): ...
    def parentGenerator(self): ...

class NavigableString(str, PageElement):
    PREFIX: str
    SUFFIX: str
    known_xml: Any
    def __new__(cls, value): ...
    def __copy__(self): ...
    def __getnewargs__(self): ...
    def __getattr__(self, attr): ...
    def output_ready(self, formatter: str = ...): ...
    @property
    def name(self) -> None: ...
    @name.setter
    def name(self, name) -> None: ...

class PreformattedString(NavigableString):
    PREFIX: str
    SUFFIX: str
    def output_ready(self, formatter: Any | None = ...): ...

class CData(PreformattedString):
    PREFIX: str
    SUFFIX: str

class ProcessingInstruction(PreformattedString):
    PREFIX: str
    SUFFIX: str

class XMLProcessingInstruction(ProcessingInstruction):
    PREFIX: str
    SUFFIX: str

class Comment(PreformattedString):
    PREFIX: str
    SUFFIX: str

class Declaration(PreformattedString):
    PREFIX: str
    SUFFIX: str

class Doctype(PreformattedString):
    @classmethod
    def for_name_and_ids(cls, name, pub_id, system_id): ...
    PREFIX: str
    SUFFIX: str

class Stylesheet(NavigableString): ...
class Script(NavigableString): ...
class TemplateString(NavigableString): ...

class Tag(PageElement):
    parser_class: Any
    name: Any
    namespace: Any
    prefix: Any
    sourceline: Any
    sourcepos: Any
    known_xml: Any
    attrs: Any
    contents: Any
    hidden: bool
    can_be_empty_element: Any
    cdata_list_attributes: Any
    preserve_whitespace_tags: Any
    def __init__(self, parser: Any | None = ..., builder: Any | None = ..., name: Any | None = ..., namespace: Any | None = ..., prefix: Any | None = ..., attrs: Any | None = ..., parent: Any | None = ..., previous: Any | None = ..., is_xml: Any | None = ..., sourceline: Any | None = ..., sourcepos: Any | None = ..., can_be_empty_element: Any | None = ..., cdata_list_attributes: Any | None = ..., preserve_whitespace_tags: Any | None = ...) -> None: ...
    parserClass: Any
    def __copy__(self): ...
    @property
    def is_empty_element(self): ...
    isSelfClosing: Any
    @property
    def string(self): ...
    @string.setter
    def string(self, string) -> None: ...
    strings: Any
    @property
    def stripped_strings(self) -> None: ...
    def get_text(self, separator: str = ..., strip: bool = ..., types=...): ...
    getText: Any
    text: Any
    def decompose(self) -> None: ...
    def clear(self, decompose: bool = ...) -> None: ...
    def smooth(self) -> None: ...
    def index(self, element): ...
    def get(self, key, default: Any | None = ...): ...
    def get_attribute_list(self, key, default: Any | None = ...): ...
    def has_attr(self, key): ...
    def __hash__(self): ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __contains__(self, x): ...
    def __bool__(self): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, tag): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __unicode__(self): ...
    def encode(self, encoding=..., indent_level: Any | None = ..., formatter: str = ..., errors: str = ...): ...
    def decode(self, indent_level: Any | None = ..., eventual_encoding=..., formatter: str = ...): ...
    def prettify(self, encoding: Any | None = ..., formatter: str = ...): ...
    def decode_contents(self, indent_level: Any | None = ..., eventual_encoding=..., formatter: str = ...): ...
    def encode_contents(self, indent_level: Any | None = ..., encoding=..., formatter: str = ...): ...
    def renderContents(self, encoding=..., prettyPrint: bool = ..., indentLevel: int = ...): ...
    def find(self, name: Any | None = ..., attrs=..., recursive: bool = ..., text: Any | None = ..., **kwargs): ...
    findChild: Any
    def find_all(self, name: Any | None = ..., attrs=..., recursive: bool = ..., text: Any | None = ..., limit: Any | None = ..., **kwargs): ...
    findAll: Any
    findChildren: Any
    @property
    def children(self): ...
    @property
    def descendants(self) -> None: ...
    def select_one(self, selector, namespaces: Any | None = ..., **kwargs): ...
    def select(self, selector, namespaces: Any | None = ..., limit: Any | None = ..., **kwargs): ...
    def childGenerator(self): ...
    def recursiveChildGenerator(self): ...
    def has_key(self, key): ...

class SoupStrainer:
    name: Any
    attrs: Any
    text: Any
    def __init__(self, name: Any | None = ..., attrs=..., text: Any | None = ..., **kwargs) -> None: ...
    def search_tag(self, markup_name: Any | None = ..., markup_attrs=...): ...
    searchTag: Any
    def search(self, markup): ...

class ResultSet(list):
    source: Any
    def __init__(self, source, result=...) -> None: ...
    def __getattr__(self, key) -> None: ...
