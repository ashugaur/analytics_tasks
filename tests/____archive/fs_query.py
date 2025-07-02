# %% fs query

## Fixed paths
from pathlib import Path
from analytics_tasks.file_search.build import lib_refs_fs
from analytics_tasks.file_search.functions import load_fs_polars, overview, query


# %% Project library

# Project folder
at_dir = Path("C:/my_disk/____tmp/analytics_tasks")

# Call build_process with the defined fs_folder
_fs_index_dir, _logs_dir, _time_machine, _reports_dir = lib_refs_fs(at_dir)


## Summary

# Load file search index
searchx = load_fs_polars(_fs_index_dir)

# File search index coverage
all = overview(searchx)
all.fs_coverage(_reports_dir, dark_mode=1)


# Search report: find 'substring' in files
substring = "happy"
report = query(searchx)

# Summary
report.fs_summary(substring)

# Summary details: all file types
report.fs_details(substring, _reports_dir, ext_filter=[], dark_mode=1)

# Summary details: particular file type
# report.fs_details(substring, _reports_dir, ext_filter=[".py"], dark_mode=1)
