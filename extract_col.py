import pandas as pd

# Load the Excel file
file_path = 'Enhanced-Laws (5).xlsx'  # Replace with your file path
         # Replace with your sheet name if needed

# Read the Excel sheet
df = pd.read_excel(file_path)

# Specify the column you want to extract
column_name = 'Re-Write Version of Article'  # Replace with the actual column name

# Extract the column
extracted_column = df[column_name]

# Print the extracted column
print(extracted_column)

# Optional: Save to a new file
extracted_column.to_excel('extracted_column.xlsx', index=False)
