# %% Testing automate office

## Dependencies
from pathlib import Path
import pandas as pd
from analytics_tasks.automate_office.build_batch import (
    lib_refs_ao_batch,
    calibration,
    python_override,
    scan_python_functions_from_file_s,
    apply_or_create_potm_colors,
    create_or_apply_potm,
    ppt_learn,
    macro_baseline,
    create_excel_charts_batch,
    export_to_powerpoint_batch,
    mask_ppt_errors,
    delete_all_chart_placeholders,
    ppt_theme,
    initialize_batch_globals,
    execute_pptx_pipeline,
    draw_charts,
)
from analytics_tasks.utils.functions import open_file_folder, round_columns


## Project folder
at_dir = Path("C:/analytics_tasks")


## Assign file/folder references [Shorter: initialize_batch_globals(at_dir)]
initialize_batch_globals(at_dir)
""" (
    _colors_file,
    _xlsm_path,
    _learn_dir,
    _output_pptm,
    _control_file,
    _control_file_worksheet,
    _template_path,
    _template_pathx,
    _visual_library_dir,
    _image_dir,
    _chart_data_dir,
    _slide_json_path,
    _slide_excel_path,
    _master_json_path,
    _master_excel_path,
    _excel_output_path,
    _learn_xl_output,
    _colors,
) = lib_refs_ao_batch(at_dir) """


## Browse or edit input parameters
"""
open_file_folder(_control_file)
open_file_folder(_colors_file)
"""


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


## Overrides
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
""" _control = python_override(
    _control,
    scan_python_functions_from_file_s,
    _visual_library_dir,
    _learn_dir,
    _chart_data_dir,
    _image_dir,
    _colors_file,
)

apply_or_create_potm_colors(
    _template_path,
    _template_pathx,
    _control[["master_name", "layout_name", "element_name"]]
    .drop_duplicates()
    .reset_index(drop=True),
    slide_master_text_elements,
)
_template_path = _template_pathx
create_or_apply_potm(_template_pathx, _output_pptm, _control) """


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
"""
_control_xlm = macro_baseline(
    _control, _xlsm_path, _visual_library_dir, universal_chart_elements
)

create_excel_charts_batch(_control, _colors, _xlsm_path, _chart_data_dir)

success, df_known_errors = export_to_powerpoint_batch(
    _control, _xlsm_path, _output_pptm, _image_dir
)

mask_ppt_errors(
    df_known_errors,
    _elements_combined,
    _master_json_path,
    _output_pptm,
    _slide_json_path,
    _slide_excel_path,
    _master_excel_path,
    _excel_output_path,
    _control,
    _learn_xl_output,
    round_columns,
    _control_file,
    _control_file_worksheet,
    _xlsm_path,
    _image_dir,
)

delete_all_chart_placeholders(_output_pptm)
"""


## Open processed file
open_file_folder(_output_pptm)
