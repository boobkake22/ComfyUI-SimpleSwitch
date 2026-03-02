# ComfyUI Simple Switch

ComfyUI custom node that returns the first available value from six optional wildcard inputs.

## What it does

- Accepts six optional inputs: `input01` ... `input06`
- Returns the first non-empty input in order
- Preserves original behavior for empty model/clip context dictionaries
- Uses wildcard typing so it can pass through most ComfyUI value types

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

1. Add the `SimpleSwitch` node.
2. Connect values to `input01` ... `input06` in your preferred priority order.
3. Use `output` downstream.

## License

This repo includes the original upstream `LICENSE` from
`11dogzi/Comfyui-ergouzi-Nodes`.
