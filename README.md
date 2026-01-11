# Screen Pause

Pause a region of the screen and drag the frozen image around—no desktop hotkey scripting required.

## Install (editable for demo)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

- Run the tool: `screen-pause` (installed via the console script).
- Click and drag to select a region. It will reappear as a movable window.
- Drag the frozen window by clicking inside it; close it by clicking the white triangle or pressing `Esc`.

## Notes

- Requires Python 3.8+ and Pillow.
- Tested on Linux with Tkinter available; other platforms may need Tk support installed.