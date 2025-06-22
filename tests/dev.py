# %% Dev

## Dependencies
"""
Install in editable mode
uv pip install -e .
uv pip install --system -e .
"""

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
from analytics_tasks.file_search.functions import (
    load_fs_polars,
    overview,
    query,
    extract_xl,
)





# %% Build








