import pandas as pd
import os

def merge_excel_files(directory):
    all_data = pd.DataFrame()
    for file in os.listdir(directory):
        if file.endswith('.xlsx'):
            file_path = os.path.join(directory, file)
            data = pd.read_excel(file_path)
            all_data = all_data.append(data, ignore_index=True)
    all_data.to_excel('merged_output.xlsx', index=False)

directory_path = "/path/to/excel/files"
merge_excel_files(directory_path)