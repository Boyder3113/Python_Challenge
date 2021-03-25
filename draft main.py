import os
import csv

budget_csv = os.path.join("..", "resources","budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        for months in row[0]:
            length = (len(row[0]))
        print(f"{length}")


        for PL in row[1]:
            total += int(PL)
        print(f"{total}")

        for max in row[1]:
            mostprofit = max(row[1])
        print(f"{mostprofit}")
        
        


