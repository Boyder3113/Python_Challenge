import os
import csv


budget_csv = os.path.join("resources","budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    months = 0
    total = 0
    for row in csv_reader:
        months += 1
        total += float(row[1])



print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {months}")
print(f"Total: {total}")


#for row in csv_reader:
    #total = row[1].sum()

#print(f"Total: {total}")

#length = len(list(csv_reader))