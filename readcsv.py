import pandas as pd

def get_csv_info(file_path):

    try:
        df = pd.read_csv(file_path, nrows=0)  # 只读取表头
    except Exception as e:
        return f"Error reading file: {e}"

    num_columns = len(df.columns)
    column_names = df.columns.tolist()

    try:
        num_rows = sum(1 for row in open(file_path)) - 1
    except Exception as e:
        return f"Error counting rows: {e}"

    return {
        "Number of Rows": num_rows,
        "Number of Columns": num_columns,
        "Column Names": column_names
    }


file_path = '/home/jiacheng/Downloads/final_results.csv'


info = get_csv_info(file_path)
print(info)
