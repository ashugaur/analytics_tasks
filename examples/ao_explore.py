# %% Automate office: explore

## Dependencies
from pathlib import Path
import pandas as pd
from analytics_tasks.automate_office.build_explore import (
    initialize_explore_globals,
    load_macro_workbook,
    transform_data_explore,
)
from analytics_tasks.automate_office.build_batch import (
    transform_data,
)
from analytics_tasks_utils.os_functions import open_file_folder

""" off
from pathlib import Path
_startup = Path("C:/my_disk/edupunk/src/functions/startup.py")
exec(open(_startup).read())
"""


## Project folder (at_dir: analytics_tasks directoary)
at_dir = Path("C:/analytics_tasks")


## Assign file/folder references
initialize_explore_globals(at_dir)


## Load macro workbook, open_file_folder(_explore_dir)
load_macro_workbook(
    _explore_dir,
    _control_file,
    _control_file_worksheet,
    _visual_library_dir,
    _xlsm_path,
)

## Get data from clipboard, open_file_folder(_visual_library_dir / "change/xyv_multiline.csv")
"""
bar_stacked_xstr_ypct = pd.read_csv(_vl / "compare/bar_stacked_xstr_ypct.csv")
df = bar_stacked_xstr_ypct[bar_stacked_xstr_ypct['drug']=='Drug A']
"""
df = pd.read_clipboard()
df.head()


## Assign x, y, z variables (refer visual library)
"""
dft = transform_data(df, x=["days_on_therapy"], y=["brand"], value=["value"], y_override={'Drug A': 'Drug A ®', 'Drug B': 'Drug B ®'}) #Check override
dft = transform_data(df, x=["cat"], y=["source"], value='nbr_of_patients')
"""
dft = transform_data(df, x=["days_on_therapy"], y=["brand"], value=["value"])
dft.head()

## Override default
_colors_file = _vl / "____settings/colors.xlsm"


## Run
# open_file_folder(_colors_file)
transform_data_explore(dft, _colors_file, y_override_color={'New': '#c23899'}).to_clipboard(index=False)
