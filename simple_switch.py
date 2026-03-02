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


class SimpleSwitch:
    """Return the first non-empty value from input01..input06."""

    CATEGORY = "Simple Switch"
    FUNCTION = "switch"
    RETURN_TYPES = (ANY_TYPE,)
    RETURN_NAMES = ("output",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "input01": (ANY_TYPE,),
                "input02": (ANY_TYPE,),
                "input03": (ANY_TYPE,),
                "input04": (ANY_TYPE,),
                "input05": (ANY_TYPE,),
                "input06": (ANY_TYPE,),
            },
        }

    def switch(
        self,
        input01=None,
        input02=None,
        input03=None,
        input04=None,
        input05=None,
        input06=None,
    ):
        for candidate in (input01, input02, input03, input04, input05, input06):
            if not _is_none(candidate):
                return (candidate,)
        return (None,)
