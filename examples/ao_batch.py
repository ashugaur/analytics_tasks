# %% Automate office: batch

## Dependencies
from pathlib import Path
import pandas as pd
from analytics_tasks.automate_office.build_batch import (
    calibration,
    scan_python_functions_from_file_s,
    ppt_learn,
    ppt_theme,
    initialize_batch_globals,
    execute_pptx_pipeline,
    draw_charts,
    my_colors,
)
from analytics_tasks_utils.os_functions import open_file_folder
from analytics_tasks_utils.formatting import round_columns


## Project folder
at_dir = Path("C:/analytics_tasks")


## Assign file/folder references [Shorter: initialize_batch_globals(at_dir)]
initialize_batch_globals(at_dir)
# initialize_batch_globals(at_dir, _colors_file=_colors_file)


## Control file: Input parameters to create .xlsm and .pptm output
_control_file_worksheet = "calibration"
_control = calibration(_control_file)  # Calibration
# _control = pd.read_excel(_control_file, sheet_name=_control_file_worksheet)


## Theme
universal_chart_elements = {
    "chartFontFamily": "Calibri",
    "chartElementsColor": "RGB(0, 22, 94)",  # theme: RGB(0, 22, 94) | theme: RGB(184, 4, 4)
    "gridlineColor": "RGB(192, 192, 192)",
}
slide_master_text_elements = ppt_theme(_colors_file, universal_chart_elements)


## PPTM overrides
_control, _template_path = execute_pptx_pipeline(
    _control,
    scan_python_functions_from_file_s,
    _visual_library_dir,
    _learn_dir,
    _chart_data_dir,
    _image_dir,
    _colors_file,
    _template_path,
    _template_pathx,
    _output_pptm,
    slide_master_text_elements,
)


## Learn
_control, _elements_combined = ppt_learn(
    _master_json_path,
    _output_pptm,
    _slide_json_path,
    _slide_excel_path,
    _master_excel_path,
    _excel_output_path,
    _control,
    _learn_xl_output,
    round_columns,
)


## Draw charts
_control_xlm, success, df_known_errors = draw_charts(
    _control,
    _xlsm_path,
    _visual_library_dir,
    universal_chart_elements,
    _colors,
    _chart_data_dir,
    _output_pptm,
    _image_dir,
    _elements_combined,
    _master_json_path,
    _slide_json_path,
    _slide_excel_path,
    _master_excel_path,
    _excel_output_path,
    _learn_xl_output,
    round_columns,
    _control_file,
    _control_file_worksheet,
)


## Browse
"""
open_file_folder(_control_file)
open_file_folder(_learn_xl_output)
open_file_folder(_colors_file)
open_file_folder(_xlsm_path)
"""
open_file_folder(_output_pptm)


## Self
"""
exec(open('examples/ao_batch.py').read())
"""
