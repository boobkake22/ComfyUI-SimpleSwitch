from .simple_switch import SimpleSwitch

NODE_CLASS_MAPPINGS = {
    "SimpleSwitch": SimpleSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleSwitch": "Simple Switch (6 Inputs)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
