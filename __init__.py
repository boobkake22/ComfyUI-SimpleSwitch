from .simple_switch import SimpleAnySwitch

NODE_CLASS_MAPPINGS = {
    "SimpleAnySwitch": SimpleAnySwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleAnySwitch": "Simple Switch (6 Inputs)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
