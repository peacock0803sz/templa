from pathlib import Path

import typer

app = typer.Typer()
_root = Path(__file__).parent.parent


@app.command()
def templa_(name: str):
    """
    Create a new template directory with the given name and copy all files from the _common directory into it.
    """
    dir = _root / "templates" / name
    if not dir.exists():
        print(f"Directory '{name}' does not exist, creating it.")
        dir.mkdir()

    common = _root / "common"
    for file in common.rglob("*"):
        if file.is_symlink():
            symlink_to = file.readlink()
            dest = dir / file.relative_to(common)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.symlink_to(symlink_to)
            print(f"Created symlink '{dest}' -> '{symlink_to}'")
        elif file.is_file():
            dest = dir / file.relative_to(common)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(file.read_bytes())
            print(f"Copied '{file}' to '{dest}'")
        else:
            print(f"'{file}' is not a file, skipping.")


if __name__ == "__main__":
    app()
