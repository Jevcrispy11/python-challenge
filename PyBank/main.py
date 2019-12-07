import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    total_months = len(data)
    total_value = 0
    greatest_change = ("", 0)
    last_value = 0
    greatest_decrease = ("", 0)
    difference = 0
    

    for row in data:
        monthly_value = int(row[1])
        total_value = total_value + int(monthly_value)
        if last_value != 0:
            change_profit = monthly_value - last_value
            if change_profit > greatest_change[1]:
                greatest_change = (row[0],change_profit)
                print(greatest_change)
            last_value = monthly_value
        if last_value != 0:
            neg_change = monthly_value - last_value
            if neg_change < greatest_decrease[1]:
                greatest_decrease = (row[0], neg_change)
            print(greatest_decrease)

    average=[]

    for i in range(len(data)-1):
        current=data[i][1]
        next=data[i+1][1]
        difference=int(next)-int(current)
        average.append(difference)
    average_change=sum(average)/len(average)
        

    
    total_months_text = "Total Months: {}" 
    total_value_text = "Total: ${}"
    average_change_text = "Average Change: ${}"
    greatest_increase_text = "Greatest Increase in Profits: {}"
    greatest_decrease_text = "Greatest Decrease in Profits: {}"


print("Financial Analysis")
print("------------------")
print(total_months_text.format(total_months))
print(total_value_text.format(total_value))
print(average_change_text.format(average_change))
print(greatest_increase_text.format(greatest_change))
print(greatest_decrease_text.format(greatest_decrease))

#couldnt get the above to change to a total variable like the other 
#output = os.path.join('../Pybank/Financial_analysis.txt')
#with open(output, 'w') as file:
    #txtwriter = file.write(Results)
    
