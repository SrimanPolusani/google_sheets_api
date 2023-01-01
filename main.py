import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("./keys.json", scopes=scope)

file = gspread.authorize(creds)
workbook = file.open("workoutAI")
sheet = workbook.sheet1


# <---------- Reading the data from Google spreadsheets ---------->

for cell in sheet.range("A1:A2"):  # it prints values of A1 and A2
    print(cell.value)


print(sheet.row_values(2))  # it prints the whole 2nd row (Horizontal iteration in sheets)
print(sheet.col_values(2))  # it prints the whole 2nd column (Vertical iteration)
print(sheet.acell('A3').value)  # it prints a single cell (A3)
print(sheet.cell(1, 4).value)  # it prints value at point (1, 4). "four in sheets is D"


# <---------- Writing the data in Google spreadsheets ---------->
sheet.update(
    "A2:E2",
    [
        [
            "15/07/2044",
            "16:00:00",
            "Skipping",
            "40",
            "700"
        ]
    ]

)  # Replaces the cell values from A2 to E2 with given values in the list

sheet.update_cell(2, 4, 50)  # Format: (X, Y [Convert letters into numbers Ex: A as 1 or D as 4], Replacing value)
sheet.update_acell("B2", "01:00:00")
sheet.append_row(['12/04/2343', '01:00:25', 'Running', '20', '200'])  # Adds a row at the last
