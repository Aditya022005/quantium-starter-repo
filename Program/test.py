import csv

# Open and filter CSV manually
for i in range(3):
    with open(f"./data/daily_sales_data_{i}.csv", "r") as file:
        reader = csv.DictReader(file)
        filtered_rows = [row for row in reader if row["product"] == "pink morsel"]

    # Print filtered records
    for row in filtered_rows:
        print(row)

    with open('../Output Data/filtered_data.csv', mode='w', newline="") as csv_file:
        fieldnames = ["Sales", "Date", "Region"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered_rows:
            data = {
                "Sales": "$"+str(float(row["price"][1:])*float(row["quantity"])),
                "Date": row["date"],
                "Region": row["region"],
            }
            writer.writerow(data)



