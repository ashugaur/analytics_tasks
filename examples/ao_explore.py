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
from analytics_tasks.utils.functions import open_file_folder


## Project folder (at_dir: analytics_tasks directoary)
at_dir = Path("C:/analytics_tasks")


## Assign file/folder references
initialize_explore_globals(at_dir)


## Open macro workbook
load_macro_workbook(
    _explore_dir,
    _control_file,
    _control_file_worksheet,
    _visual_library_dir,
    _xlsm_path,
)

## Get data from clipboard
open_file_folder(_visual_library_dir / "change/xyv_multiline.csv") # Copy content of this file
df = pd.read_clipboard()
df.head()


## Assign x, y, z variables (refer visual library)
df = transform_data(df, x=["days_on_therapy"], y=["brand"], value=["value"])
df.head()


## Run
# open_file_folder(_colors_file)
transform_data_explore(df, _colors_file).to_clipboard(index=False) # Macro: `xyv_multiline`
