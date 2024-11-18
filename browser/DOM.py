'''
classes for DOM
-PaiShoFish49
'''

from fractions import Fraction
from typing import Literal

class Page():
    def __init__(self):
        self.children = []
        self.style = Style()

class Style:
    def __init__(self):
        self.originAlignRelative = True
        self.boxAlignRelative = True

        self.originAlign: list[float, float] = [0, 0]
        self.boxAlign: list[float, float] = [0, 0]

        self.scale: Literal["wrap-children", "fit-parent", "fill-parent", "constant"] = "wrap-children"
        self.aspectRatio: Fraction = None
        self.scale = None

        self.margin: float | list[float, float] | list[float, float, float, float] = 0.0
        self.borderWidth: float | list[float, float] | list[float, float, float, float] = 0.0
        self.padding: float | list[float, float] | list[float, float, float, float] = 0.0

        self.borderColor: list[int, int, int, int] = [0, 0, 0, 0]
        self.backgroundColor: list[int, int, int, int] = [255, 255, 255, 0]
        self.contentColor: list[int, int, int, int] = [0, 0, 0, 255]

        self.display: Literal["normal", "contents", "hide"] = "normal"
        self.zindex = None

        self.pack: bool = True
        self.context: Literal["fake-parent", "parent", "screen", "page"] = "fake-parent"

class HFMLElement():
    def __init__(self, ID, elementType, styleClasses, parent, children = None, content = None):
        self.ID = ID
        self.elementType = elementType
        self.styleClasses = styleClasses
        self.parent = parent
        self.children = children
        self.content = content

        self.style = Style()

        eventListeners = {
            "onClick": None,
            "onHover": None,
            "offHover": None,
            "onDbClick": None,
            "onHold": None,
        }