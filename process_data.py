import csv
import os

# Folder where CSV files exist
data_folder = "data"

# Output file
output_file = "formatted_data.csv"

# Store processed rows
output_data = []

# Loop through all CSV files
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)

        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Step 1: Filter only Pink Morsels
                if row["product"].lower() == "pink morsel":
                    # Step 2: Calculate sales
                    price = float(row["price"].replace("$","").strip())
                    sales = int(row["quantity"]) * price

                    # Step 3: Store required fields
                    output_data.append({
                        "Sales": sales,
                        "Date": row["date"],
                        "Region": row["region"]
                    })

# Step 4: Write output CSV
with open(output_file, mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Sales", "Date", "Region"])
    writer.writeheader()
    writer.writerows(output_data)

print("Processing complete! File saved as formatted_data.csv")