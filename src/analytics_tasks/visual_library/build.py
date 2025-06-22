from pathlib import Path


def lib_refs_vl(at_dir):
    """Assigns working libraries inside visual_library dir."""
    visual_library_dir = at_dir / "visual_library"

    Path(visual_library_dir).mkdir(parents=True, exist_ok=True)

    print("Assigned visual_library directories.")

    return visual_library_dir
