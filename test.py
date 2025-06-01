import json
import openpyxl

# Load Excel workbook
workbook = openpyxl.load_workbook("generated_data.xlsx")
sheet = workbook.active

# Extract headers
headers = [cell.value if cell.value is not None else "" for cell in sheet[1]]

# Build final JSON
json_output = []

for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
    characteristics = []
    for key, value in zip(headers, row):
        characteristics.append({
            "name": key,
            "valueType": "string",
            "value": value if value is not None else ""
        })

    entry = {
        "entityType": "OTTCategory",
        "characteristics": characteristics
    }

    json_output.append(entry)

# Save to file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=4, ensure_ascii=False)

print("Conversion complete. JSON saved as output.json")
