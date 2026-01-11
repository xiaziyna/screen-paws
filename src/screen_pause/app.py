"""Minimal Tkinter-based screen pause tool."""

import tkinter as tk
from typing import Dict, Tuple

from PIL import ImageGrab, ImageTk


def make_snip() -> None:
    """Capture a region of the screen, then display and drag it around."""
    full_image = ImageGrab.grab()

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)

    state: Dict[str, object] = {"start_x": 0, "start_y": 0, "rect_id": None}
    drag = {"x": 0, "y": 0}

    canvas = tk.Canvas(root, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    background = ImageTk.PhotoImage(full_image)
    canvas.create_image(0, 0, anchor="nw", image=background)

    def close_window(_event=None) -> None:
        root.destroy()

    def on_press(event) -> None:
        state["start_x"] = event.x
        state["start_y"] = event.y
        if state["rect_id"]:
            canvas.delete(state["rect_id"])
            state["rect_id"] = None

    def on_drag(event) -> None:
        if state["rect_id"]:
            canvas.delete(state["rect_id"])
        state["rect_id"] = canvas.create_rectangle(
            state["start_x"],
            state["start_y"],
            event.x,
            event.y,
            outline="light grey",
            width=2,
        )

    def on_release(event) -> None:
        x1 = min(state["start_x"], event.x)
        y1 = min(state["start_y"], event.y)
        x2 = max(state["start_x"], event.x)
        y2 = max(state["start_y"], event.y)

        root.withdraw()
        root.update_idletasks()

        image = full_image.crop((x1, y1, x2, y2))
        width = x2 - x1
        height = y2 - y1

        root.attributes("-fullscreen", False)
        root.overrideredirect(True)
        root.geometry(f"{width}x{height}+{x1}+{y1}")

        canvas.destroy()

        view = tk.Canvas(root, width=width, height=height, highlightthickness=0, bd=0)
        view.pack()

        photo = ImageTk.PhotoImage(image)
        view.create_image(0, 0, anchor="nw", image=photo)
        view.image = photo

        view.create_rectangle(1, 1, width - 1, height - 1, outline="black", width=2)

        size = max(20, min(width, height) // 6)
        offset = size // 2
        center_x = width // 2
        center_y = height // 2
        points: Tuple[int, ...] = (
            center_x - offset // 2,
            center_y - offset,
            center_x - offset // 2,
            center_y + offset,
            center_x + offset,
            center_y,
        )
        triangle = view.create_polygon(points, fill="white", outline="black", width=2)
        view.tag_bind(triangle, "<Button-1>", close_window)

        def start_move(event) -> None:
            drag["x"] = event.x
            drag["y"] = event.y

        def move_window(event) -> None:
            x = event.x_root - drag["x"]
            y = event.y_root - drag["y"]
            root.geometry(f"+{x}+{y}")

        view.bind("<ButtonPress-1>", start_move)
        view.bind("<B1-Motion>", move_window)

        root.deiconify()
        root.mainloop()

    canvas.bind("<ButtonPress-1>", on_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)
    root.bind("<Escape>", close_window)

    root.mainloop()


def main() -> None:
    make_snip()


if __name__ == "__main__":
    main()
