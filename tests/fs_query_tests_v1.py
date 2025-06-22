# %% Summary

## Fixed paths
import os

os.chdir(r"C:\my_disk\edupunk\analytics\projects\analytics_tasks")

fs_folder = r"C:\my_disk\____tmp\fs"
fs_index_dir = fs_folder + r"\input"


## Build process
from file_search.build import build_process

# Call build_process with the defined fs_folder
logs_folder, time_machine, reports_folder = build_process(fs_folder)


## Summary
from file_search.functions import load_search_polars, overview, summary

# Load search index
searchx = load_search_polars(fs_index_dir)

# Check coverage
all = overview(searchx)
all.fs_coverage(reports_folder, dark_mode=1)


## Search report
substring = "the"
report = summary(searchx)

# Summary
report.fs_summary(substring)

# Details
report.fs_details(substring, reports_folder, ext_filter=[".py"], dark_mode=1)
