# ComfyUI Simple Switch

ComfyUI custom nodes for returning the first available value from six optional inputs.

## What it does

- `SimpleSwitch`
  - Accepts six optional wildcard inputs: `input01` ... `input06`
  - Returns the first non-empty input in order
  - Preserves original behavior for empty model/clip context dictionaries
  - Uses wildcard typing so it can pass through most ComfyUI value types
- `SimpleLatentSwitch`
  - Accepts six optional `LATENT` inputs
  - Returns the first non-empty latent in order
  - Keeps LTX latents on a typed `LATENT` path instead of a wildcard path
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

1. Add `SimpleSwitch` for general pass-through selection, `SimpleLatentSwitch` for LTX latent selection, or `SimpleAudioLatentSwitch` right before `LTXV Audio VAE Decode`.
2. Connect values to `input01` ... `input06` in your preferred priority order.
3. Use `output` downstream.

## LTX audio note

LTX video latents and LTX audio latents both use the ComfyUI `LATENT` socket type, but
the audio decoder only accepts audio-shaped latents or nested AV latents. If you route
an LTX latent through the generic wildcard `SimpleSwitch`, it can lose the typed latent
path and you may only discover the mismatch at decode time.

Use `SimpleLatentSwitch` anywhere you are switching LTX latents in general, and use
`SimpleAudioLatentSwitch` immediately before `LTXV Audio VAE Decode` when selecting
between LTX audio latent branches.

## License

This repo includes the original upstream `LICENSE` from
`11dogzi/Comfyui-ergouzi-Nodes`.
