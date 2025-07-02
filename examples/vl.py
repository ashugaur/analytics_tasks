# %% VL

## Dependencies
from pathlib import Path
from analytics_tasks.utils.functions import open_file_folder
from analytics_tasks.visual_library.build import lib_refs_vl, copy_gallery_folder
from analytics_tasks.visual_library.visual_library_demo import create_site

## Project dir
at_dir = Path("C:/analytics_tasks")

## Visual library demo
visual_library_dir, visual_library_file = lib_refs_vl(at_dir)
result = copy_gallery_folder(at_dir)
print(f"Gallery copied to: {result}")
create_site(
    visual_library_dir,
    side_bar_width="200px",
    page_color="#D4BC96",
    toc_color="#8731bc",
    toc_bg_color="rgba(165, 165, 165, 0.1)",
    image_extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".jfif", '.xlsm'],
    exclude_folders=['____settings']
)

## Open visual library
open_file_folder(visual_library_file)
