# %% fs

## Dependencies
from pathlib import Path
from analytics_tasks.file_search.build import (
    log_start,
    lib_refs_fs,
    scan_directories_python,
    scan_dir_powershell,
    scan_time_machine,
    scan_clean,
    scan_history,
    exceptions,
    apply_filters,
    scan_drives,
    ifp,
    export_index_files,
    log_end,
)


## Project folder
at_dir = Path("C:/analytics_tasks")


## List folders to scan and index
scan_dirs = [Path("C:/my_disk/settings")]


## Dictionary of list of file type to scan and index
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

## Size limit in MB for 'scan_ext' dictionary
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


## Assign file/folder references
_fs_index_dir, _logs_dir, _time_machine, _reports_dir = lib_refs_fs(at_dir)

# Logging
log_start(_logs_dir)

# Scan directories (small and fast hard disk)
scan_directories_python(_fs_index_dir, scan_dirs)

# Recommended for windows (large and slow hard disk)
# scan_dir_powershell(fs_index_dir, scan_dirs)

# Time machine
scan_time_machine()

# Scan clean
scan0 = scan_clean(_fs_index_dir)

# Scan history
scan, scan_old, searchx_final_old = scan_history(scan0)


# Exceptions
paths_to_exclude = [Path("C:/my_disk/settings/python"), Path("C:/my_disk/settings/r")]
scan, exception_file = exceptions(scan, paths_to_exclude)

# Apply filters
scan = apply_filters(scan, scan_ext, scan_size)

# Scan disk
scan_drives(scan, scan_ext)

# Index files creating an 'intermediate file pool'
searchx = ifp(scan0, searchx_final_old)

# Export search index
export_index_files(_fs_index_dir, scan0, searchx)

# Close logging
log_end()
