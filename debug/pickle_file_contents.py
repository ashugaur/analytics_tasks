import os
import pandas as pd
import shutil

def check_single_value_pickle(file_path):
    # Read the pickle file directly into a Pandas DataFrame
    df = pd.read_pickle(file_path)

    # Check if the DataFrame has only a single unique value in any column
    unique_values = df.nunique()
    single_value = None

    for col in unique_values.index:
        if unique_values[col] == 1:
            single_value = df[col].iloc[0]
            break

    # Release the DataFrame from memory
    del df

    return single_value

def process_pickle_files(folder_path, move_file_to):
    # Create the move_file_to directory if it doesn't exist
    os.makedirs(move_file_to, exist_ok=True)

    # Get the list of pickle files in the folder and sort them
    pickle_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pickle')])
    total_files = len(pickle_files)

    # Iterate over each file in the folder
    for i, filename in enumerate(pickle_files, start=1):
        file_path = os.path.join(folder_path, filename)
        print(f"Reading {i} of {total_files} files: {filename}")

        try:
            single_value = check_single_value_pickle(file_path)

            if single_value is not None:
                print(f"File: {filename}, Unique Value: {single_value}")
        except Exception as e:
            print(f"Error processing file {filename}: {str(e)}")
            # Move the problematic file to the specified folder
            shutil.move(file_path, os.path.join(move_file_to, filename))
            print(f"Moved {filename} to {move_file_to}")

if __name__ == "__main__":
    folder_path = time_machine  # Replace with the path to your folder
    error_folder = reports_folder+r"/pickle_file_contents_error"  # Replace with the path where you want to move error files
    process_pickle_files(folder_path, error_folder)

