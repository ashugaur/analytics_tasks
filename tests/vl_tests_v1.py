# %% Testing visual library

## Dependencies
from pathlib import Path
from analytics_tasks.visual_library.build import lib_refs_vl
from analytics_tasks.visual_library.visual_library_demo import create_site
from analytics_tasks.visual_library.copy_gallery_folder import copy_gallery_folder

## Project folder (at_dir: analytics_tasks directoary)
at_dir = Path("C:/my_disk/____tmp/analytics_tasks")

## Assign file/folder references
visual_library_dir = lib_refs_vl(at_dir)

## Copy gallery folder
result = copy_gallery_folder(at_dir)
print(f"Gallery copied to: {result}")

## Create visual library using sample code
create_site(
    visual_library_dir,
    page_color="#1E2129",
    toc_color="#8856a7",
    toc_bg_color="rgba(0, 0, 0, 0.2)",
    output_file="visual_library.html",
)

## Create visual library in other places
"""

create_site(
    r"C:\my_disk\edupunk\analytics\application\visual_library",
    page_color="#1E2129",
    toc_color="#8856a7",
    toc_bg_color="rgba(0, 0, 0, 0.2)",
    output_file="visual_library.html",
)


create_site(
    r"C:\my_disk\edupunk\analytics\application\visual_library\flashcards",
    page_color="#1E2129",
    toc_color="#8856a7",
    toc_bg_color="rgba(0, 0, 0, 0.2)",
    output_file="flashcards.html",
)

"""
