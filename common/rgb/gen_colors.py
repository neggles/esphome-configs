#!/usr/bin/env python3
# This file is used to generate color definitions for RGB lights in ESPHome.
from pathlib import Path
from shutil import rmtree

script_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
out_dir = script_dir.joinpath("colors")


class Color:
    def __init__(self, id: str, rgb: str):
        """Initialize a Color with an ID and an RGB hex string."""
        self.id = id
        self.rgb = rgb.lstrip("#")

    @property
    def red(self) -> int:
        """Return the red component as a percentage (0-100)."""
        return max(0, min(100, int(self.rgb[0:2], 16) * 100 // 255))

    @property
    def green(self) -> int:
        """Return the green component as a percentage (0-100)."""
        return max(0, min(100, int(self.rgb[2:4], 16) * 100 // 255))

    @property
    def blue(self) -> int:
        """Return the blue component as a percentage (0-100)."""
        return max(0, min(100, int(self.rgb[4:6], 16) * 100 // 255))

    def as_yaml(self) -> tuple[str, str]:
        """Return the color name, and its YAML representation for ESPHome yaml insertion."""
        return self.id, "\n".join(
            [
                f"# {self.id} #{self.rgb}",
                f"red: {self.red}%",
                f"green: {self.green}%",
                f"blue: {self.blue}%",
            ]
        )


COLORS = {
    Color("red", "#FF0000"),
    Color("vermillion", "#FF4000"),
    Color("orange", "#FF8000"),
    Color("amber", "#FFC000"),
    Color("yellow", "#FFFF00"),
    Color("lime", "#C0FF00"),
    Color("chartreuse", "#80FF00"),
    Color("harlequin", "#40FF00"),
    Color("green", "#00FF00"),
    Color("erin", "#00FF40"),
    Color("spring_green", "#00FF80"),
    Color("aquamarine", "#00FFC0"),
    Color("cyan", "#00FFFF"),
    Color("sky_blue", "#00C0FF"),
    Color("azure", "#0080FF"),
    Color("cerulean", "#0040FF"),
    Color("blue", "#0000FF"),
    Color("indigo", "#4000FF"),
    Color("violet", "#8000FF"),
    Color("purple", "#C000FF"),
    Color("magenta", "#FF00FF"),
    Color("cerise", "#FF00C0"),
    Color("rose", "#FF007F"),
    Color("crimson", "#FF0040"),
}


def main():
    # Clean up output directory
    if out_dir.exists():
        print("Cleaning up old output directory...")
        rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if len(list(out_dir.iterdir())) > 0:
        raise RuntimeError(f"Output directory {out_dir} is not empty after cleanup!")

    print(f"Generating {len(COLORS)} color files in {out_dir.relative_to(script_dir)}:")
    for color in COLORS:
        color_id, color_yaml = color.as_yaml()
        print(f"- {color_id}")
        color_file = out_dir.joinpath(f"{color_id}.yaml")
        color_file.write_text(color_yaml)

    print("Done.")


if __name__ == "__main__":
    main()
