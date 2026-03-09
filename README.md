# ComfyUI Simple Switch

ComfyUI custom nodes for returning the first available value from six optional inputs.

## What it does

- `SimpleSwitch`
  - Accepts six optional wildcard inputs: `input01` ... `input06`
  - Returns the first non-empty input in order
  - Preserves original behavior for empty model/clip context dictionaries
  - Uses wildcard typing so it can pass through most ComfyUI value types
- `SimpleAudioLatentSwitch`
  - Accepts six optional `LATENT` inputs
  - Returns the first latent compatible with LTX audio decode
  - Rejects incompatible latent shapes instead of forwarding them blindly

## Credits

This node is isolated and renamed from `EGRYQHNode` in:

- [11dogzi/Comfyui-ergouzi-Nodes](https://github.com/11dogzi/Comfyui-ergouzi-Nodes)
- Source file: `nodes/egryqh.py`

Original author: **11dogzi**

## Installation

Clone into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/boobkake22/ComfyUI-SimpleSwitch.git
```

Restart ComfyUI after installing.

## Usage

1. Add `SimpleSwitch` for general pass-through selection, or `SimpleAudioLatentSwitch` for LTX audio pipelines.
2. Connect values to `input01` ... `input06` in your preferred priority order.
3. Use `output` downstream.

## LTX audio note

LTX video latents and LTX audio latents both use the ComfyUI `LATENT` socket type, but
the audio decoder only accepts audio-shaped latents or nested AV latents. If you route
an LTX audio path through a generic wildcard switch, it is easy to accidentally forward
an incompatible latent and only discover it at decode time.

Use `SimpleAudioLatentSwitch` before `LTXV Audio VAE Decode` when selecting between LTX
audio latent branches.

## License

This repo includes the original upstream `LICENSE` from
`11dogzi/Comfyui-ergouzi-Nodes`.
