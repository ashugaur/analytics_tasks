# %% Testing automate office

## Dependencies
from pathlib import Path
import pandas as pd
from analytics_tasks.automate_office.build_explore import (
    lib_refs_ao_explore,
    load_macro_workbook,
    transform_data,
    transform_data_explore,
)

## Project folder (at_dir: analytics_tasks directoary)
at_dir = Path("C:/my_disk/____tmp/analytics_tasks")

## Assign file/folder references
(
    _colors_file,
    _xlsm_path,
    logs_folder,
    input_folder,
    learn_folder,
    _output_pptm,
    _control_file,
    _control_file_worksheet,
    explore_folder,
    _template_path,
    input_img_folder,
    input_data_folder,
    visual_library_dir,
    automate_office_dir,
    input_template_folder,
) = lib_refs_ao_explore(at_dir)


## Load macro workbook
load_macro_workbook(
    explore_folder,
    _control_file,
    _control_file_worksheet,
    visual_library_dir,
    _xlsm_path,
)


## Get data from clipboard
df = pd.read_clipboard()
df.head()

## Assign x, y, z variables (refer visual library)
df = transform_data(df, x=["days_on_therapy"], y=["brand"], value=["value"])
df.head()

## Run and paste to excel
# open_file_folder(_colors_file)
transform_data_explore(df, _colors_file).to_clipboard(index=False)
