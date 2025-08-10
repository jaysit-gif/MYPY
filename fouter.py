from test import findmean, findmode
import csv

def read_column(filename, col_index):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        data = []
        for row in reader:
            try:
                value = int(row[col_index])
                data.append(value)
            except ValueError:
                continue
    return data

price = read_column("Netflix_stock_data.csv", 5)
print("Mean price:", findmean(price))
print("Mode price:", findmode(price))
 






    

        


        

