import pandas as pd
from pathlib import Path

# Get a list of the workbooks to loop through
directory = "/enter/your/directory/here/to/loop/through"
workbooks = [f for f in Path(directory).glob("*.xlsx")]

final = []

# Loop through the workbooks
for workbook in workbooks:
    full_path = workbook.resolve()
    print(full_path)
    xls = pd.ExcelFile(full_path)
    sheets = xls.sheet_names[4:-1]
    print(sheets)

    # Loop through the specific sheets in each workbook
    for sheet in sheets:
        df = pd.read_excel(full_path, sheet_name=sheet, usecols="A:J", skiprows=9)
        last_row = df[df["Unnamed: 0"] == "xxxxxx1"].index[0] - 4

        df1 = pd.read_excel(
            full_path, sheet_name=sheet, usecols="A:J", skiprows=9, nrows=last_row
        )
        #Rename your columns below
        df1.rename(
            columns={
                "Unnamed: 0": "xxxxxx1",
                "Unnamed: 1": "xxxxxx2",
                "Unnamed: 2": "xxxxxx3",
                "Unnamed: 3": "xxxxxx4",
                "Unnamed: 4": "xxxxxx5",
                "Unnamed: 5": "xxxxxx6",
                "Unnamed: 6": "xxxxxx7",
                "Unnamed: 7": "xxxxxx8",
                "Unnamed: 8": "xxxxxx9",
                "Unnamed: 9": "xxxxxx10",
            },
            inplace=True,
        )
        df1.dropna(subset=["xxxxxx1"], inplace=True)
        df1.dropna(subset=["xxxxxx2"], inplace=True)
        #Create additional columns not within the workbooks below
        df1["Source"] = sheet
        df1["Workbook"] = workbook.stem

        df2 = df1[(df1["xxxxxx1"] != 0) & (df1["xxxxxx2"] != 0)]
        final.append(df2)

# combine all data and write to Excel
df3 = pd.concat(final)
df3.to_excel("/enter/your/excel/path/to/export/to/here.xslx", index=False)
