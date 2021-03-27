import os
import csv

budget_csv = os.path.join("resources","budget_data.csv")
output_path = os.path.join("resources", "budget_data_output.csv")

months = 0
profit_loss_total = 0
change = 0
revenue = 0
date = []
profitsandlosses =[]

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    firstrow = next(csv_reader)
    months +=1
    profit_loss_total += int(firstrow[1])
    revenue = int(firstrow[1])

    for row in csv_reader:
        date.append(row[0])

        change = int(row[1]) - revenue
        profitsandlosses.append(change)
        value = int(row[1])

        months +=1 

        profit_loss_total = profit_loss_total + int(row[1])

biggest_increase = max(profitsandlosses)
increase_index = profitsandlosses.index(biggest_increase)
increase_date = date[increase_index]

biggest_decrease = min(profitsandlosses)
decrease_index = profitsandlosses.index(biggest_decrease)
decrease_date = date[decrease_index]

year_change_average = sum(profitsandlosses)/len(profitsandlosses)

print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {months}")
print(f"Total: {profit_loss_total}")
print(f"average Change: {round(year_change_average)}")
print(f"Greatest Increase in Profits: {increase_date} ({biggest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} ({biggest_decrease})")

with open (output_path, 'w',) as output_file:
    output_file.write("Financial Analysis")
    output_file.write("\n")
    output_file.write("-----------------------------------------------------")
    output_file.write("\n")
    output_file.write("Total Months: " + "$ " + str(months))
    output_file.write("\n")
    output_file.write("Total: " + str(profit_loss_total))
    output_file.write("\n")
    output_file.write("Average Change: " + str(round(year_change_average)))
    output_file.write("\n")
    output_file.write("Greatest Increase: " + str(increase_date) + "($" + str(biggest_increase) + ")")
    output_file.write("\n")
    output_file.write("Greatest Decrease: " + str(decrease_date) + "($" + str(biggest_decrease) + ")")