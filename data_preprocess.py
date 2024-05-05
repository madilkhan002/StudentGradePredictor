import pandas as pd
class DataPreprocessing:
    def normalize_data(self):
        file_name = 'dataset.xlsx'
        output_file_path = './NormalizedData/normalized_data.xlsx'
        sheet_names = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"]

        # Create ExcelWriter object to write to a new Excel file
        writer = pd.ExcelWriter(output_file_path)

        # Iterate through each sheet and read it into a DataFrame
        for sheet_name in sheet_names:
            df = pd.read_excel(file_name, sheet_name=sheet_name)
            df.fillna(0, inplace=True)
            
            # For each column in the DataFrame of Assignments
            assignments = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As:7']
            quizzes = ['Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:5', 'Qz:6', 'Qz:7', 'Qz:8']
            
            # Normalize marks for assignments and quizzes
            for column in df.columns:
                if column in assignments:
                    for i in range(3, len(df[column])):
                        df.loc[i, column] = (df.loc[i, column] / df.loc[1, column]) * df.loc[0, column]
                if column in quizzes:
                    for i in range(3, len(df[column])):
                        df.loc[i, column] = (df.loc[i, column] / df.loc[1, column]) * df.loc[0, column]
            
            # Write the normalized DataFrame to the new Excel file
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        # Save the Excel file
        writer.close()

    def merge_all_sheets(self):
        output_file_path = "./MergedData/merged_data.xlsx"
        input_file_path = './NormalizedData/normalized_data.xlsx'
        sheet_names = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"]
        # Create an empty list to store DataFrames for each sheet
        dfs = []
        # Iterate through each sheet and read it into a DataFrame
        for sheet_name in sheet_names:
            df = pd.read_excel(input_file_path, sheet_name=sheet_name, skiprows=[1,2,3])
            dfs.append(df)

        # Merge all DataFrames in the list into a single DataFrame
        df = pd.concat(dfs, ignore_index=True)
        # Write the merged DataFrame to a new Excel file
        writer = pd.ExcelWriter(output_file_path)
        df.fillna(0, inplace=True)
        df.to_excel(writer, index=False)
        writer.close()

    def create_dataframe(self):
        file_path = './MergedData/merged_data.xlsx'
        df = pd.read_excel(file_path)
        return df