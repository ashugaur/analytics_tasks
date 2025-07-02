# %% Tests

## Fixed paths
import os

os.chdir(r"C:\my_disk\edupunk\analytics\projects\analytics_tasks")

## Change as required

# fs_folder: Folder to keep all project files
fs_folder = r"C:\my_disk\____tmp\fs"

# scan_dirs: List of folders to scan for files and their text
scan_dirs = [r"C:\my_disk\edupunk\analytics\exploratory"]

# scan_ext: Dictionary of list of file types that we want to scan and index
scan_ext = {
    "txt": [".ps1", ".py", ".txt", ".R", ".sql", ".sas", ".rtf", ".md", ".yml", ".bas"],
    "docx": [".docx"],
    "pptx": [".pptx", ".pptm"],
    "ppt": [".ppt"],
    "msg": [".msg"],
    "eml": [".eml"],
    "epub": [".epub"],
    "pdf": [".pdf"],
    "excel": [".xls", ".xlsx", ".xlsm"],
}

# scan_size: Size limit in MB for 'scan_ext' dictionary
scan_size = {
    "txt": [3],
    "docx": [500],
    "pptx": [500],
    "msg": [100],
    "eml": [100],
    "epub": [300],
    "pdf": [300],
    "excel": [2],
}


## Build process
from file_search.build import lib_refs

# File/Folder references
fs_index_dir, logs_folder, time_machine, reports_folder = lib_refs(fs_folder)


## Log start
from file_search.build import log_start

log_start(logs_folder)


## scan_dir
from file_search.build import scan_dir_powershell

scan_dir_powershell(fs_index_dir, scan_dirs)

# Alternate

from file_search.build_alt import scan_directories_python

scan_directories_python(fs_index_dir, scan_dirs)


## Time machine
from file_search.build import scan_time_machine

scan_time_machine()


## Scan clean
from file_search.build import scan_clean

scan0 = scan_clean(fs_index_dir)


## Scan history
from file_search.build import scan_history

scan, scan_old, searchx_final_old = scan_history(scan0)


## Exceptions
from file_search.build import exceptions

paths_to_exclude = [
    r"C:/my_disk/edupunk/metadata",
    r"C:/my_disk/a/metadata",
    r"C:/my_disk/edupunk/all_docs/site",
    r"C:/my_disk/edupunk/all_docs/includes",
    r"C:/my_disk/edupunk/all_docs/docs/analytics",
    r"C:/my_disk/edupunk/all_docs/docs/assets",
    r"C:/my_disk/edupunk/all_docs/docs/revise",
    r"C:/my_disk/edupunk/analytics/application/____automated_function_scan",
]
scan, exception_file = exceptions(scan, paths_to_exclude)


## Apply filters
from file_search.build import apply_filters

scan = apply_filters(scan, scan_ext, scan_size)


## Scan drives
from file_search.build import (
    scan_drives,
    scan_folder_searchx,
    load_ifp,
    read_text,
    analyze_imoprt_load,
)

scan_drives(scan, scan_ext)


## Intermediate file pool

from file_search.build import ifp, scan_folder_searchx

searchx = ifp(scan0, searchx_final_old)


from file_search.build import export_indexes

export_indexes(fs_index_dir, scan0, searchx)


from file_search.build import log_end

log_end()
