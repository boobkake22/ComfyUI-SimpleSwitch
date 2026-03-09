from .simple_switch import SimpleAudioLatentSwitch, SimpleSwitch

NODE_CLASS_MAPPINGS = {
    "SimpleSwitch": SimpleSwitch,
    "SimpleAudioLatentSwitch": SimpleAudioLatentSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleSwitch": "Simple Switch (6 Inputs)",
    "SimpleAudioLatentSwitch": "Simple Audio Latent Switch (6 Inputs)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
