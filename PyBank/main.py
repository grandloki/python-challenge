import os
import csv

bankcsv = os.path.join('Resources', 'budget_data.csv')

months = []
profitlosses = []
averagechanges = []

monthTotal = 0
sumTotal = 0
averages = 0
greatestinc = 0
greatestdec = 0

with open(bankcsv) as bankdata:
    bankreader = csv.reader(bankdata, delimiter=',')
    #print(bankreader)
    
    csv_header = next(bankdata)
    #print(f"Header: {csv_header}")
    firstRow = next(bankreader)
    #previousVal = int(firstRow[1])
    #totalChange = 0
    #totalRowsForAverage = 0 
    for row in bankreader:
        #print(row[0])
        months.append(row[0])
        
        
        profitlosses.append(int(row[1]))
        #sum of profit/losses - 
        
        #print(sumTotal)

        #average of changes in profit/losses - sum(column) / len(column)
        #totalChange = totalChange + int(row[1]) - previousVal
        #totalRowsForAverage = totalRowsForAverage + 1
        #previousVal = int(row[1])
        #averages = next(bankreader, int(row[1])) - int(row[1])
        #averagechanges.append(averages)
        if int(row[1]) > 0:
            greatestinc = int(row[1])
        if int(row[1]) < 0:
            greatestdec = int(row[1])
    monthTotal = len(months)
    sumTotal = sum(profitlosses)


        


print(monthTotal)
print(sumTotal)
#print(totalchange / totalRowsForAverage)
print(greatestinc)
print(greatestdec)


print(f"This is all I was able to get so far: Total Months: {monthTotal} Total: {sumTotal} Greatest increase: {greatestinc} Greatest Decrease: {greatestdec}", file = open(r"analysis/results.txt","w+"))