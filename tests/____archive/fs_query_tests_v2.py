# %% File search query Testing

## Fixed paths
import os
from pathlib import Path
os.chdir(Path("C:/my_disk/projects/analytics_tasks"))
from file_search.build import lib_refs
from file_search.functions import load_fs_polars, overview, query



# %% Project library

# Project folder
at_dir = Path("C:/my_disk/____tmp/analytics_tasks")

# Call build_process with the defined fs_folder
fs_index_dir, logs_folder, time_machine, reports_folder = lib_refs(at_dir)


## Summary

# Load file search index
searchx = load_fs_polars(fs_index_dir)

# File search index coverage
all = overview(searchx)
all.fs_coverage(reports_folder, dark_mode=1)


# Search report: find 'substring' in files
substring = "happy"
report = query(searchx)

# Summary
report.fs_summary(substring)

# Summary details: all file types
report.fs_details(substring, reports_folder, ext_filter=[], dark_mode=1)

# Summary details: particular file type
# report.fs_details(substring, reports_folder, ext_filter=[".py"], dark_mode=1)
