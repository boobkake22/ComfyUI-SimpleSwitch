"""Standalone renamed switch node for ComfyUI.

Derived from `EGRYQHNode` in `nodes/egryqh.py` from:
https://github.com/11dogzi/Comfyui-ergouzi-Nodes
Original author: 11dogzi
"""


class AnyType(str):
    """Wildcard type that compares equal to every ComfyUI type."""

    def __ne__(self, _value: object) -> bool:
        return False


ANY_TYPE = AnyType("*")


def _is_context_empty(ctx):
    return not ctx or all(v is None for v in ctx.values())


def _is_none(value):
    if value is not None:
        if isinstance(value, dict) and "model" in value and "clip" in value:
            return _is_context_empty(value)
    return value is None


class SimpleAnySwitch:
    """Return the first non-empty value from value_1..value_6."""

    CATEGORY = "Simple Switch"
    FUNCTION = "switch"
    RETURN_TYPES = (ANY_TYPE,)
    RETURN_NAMES = ("output",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "value_1": (ANY_TYPE,),
                "value_2": (ANY_TYPE,),
                "value_3": (ANY_TYPE,),
                "value_4": (ANY_TYPE,),
                "value_5": (ANY_TYPE,),
                "value_6": (ANY_TYPE,),
            },
        }

    def switch(
        self,
        value_1=None,
        value_2=None,
        value_3=None,
        value_4=None,
        value_5=None,
        value_6=None,
    ):
        for candidate in (value_1, value_2, value_3, value_4, value_5, value_6):
            if not _is_none(candidate):
                return (candidate,)
        return (None,)
