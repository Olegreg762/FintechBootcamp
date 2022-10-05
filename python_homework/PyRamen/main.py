#Import library to read csv file
import csv

#Define variables
menu = []
sales = []
report = {}

#Open csv file menu_data.csv
with open('./Resources/menu_data.csv') as menu_data:
    #Create variable menu_data from csvreader
    menu_data = csv.reader(menu_data, delimiter=',')
    #Skip header labels
    header = next(menu_data)
    #Print header
    for row in menu_data:
        menu.append(row)

#Open csv file sales_data.csv
with open('./Resources/sales_data.csv') as sales_data:
    #Create variable sales_data from csvreader
    sales_data = csv.reader(sales_data, delimiter=',')
    #Skip header labels
    header = next(sales_data)
    #Print header
    for row in sales_data:
        sales.append(row)

#Create dict for each item in menu
for sale_row in sales:
    sale_item = sale_row[4]
    quantity = sale_row[3]
    #Extras from sales, report
    if sale_item not in report:
        report[sale_item] = {'01-count': 0, '02-revenue': 0, '03-cogs': 0, '04-profit': 0}
        print(f'{sale_item} does not match {menu_item}! NO MATCH!')
     #Extras price & cost calculate revenue and cogs
    if sale_item in report:
        report[sale_item]['01-count'] += int(quantity)
    #Read into menu
    for menu_row in menu:
        menu_item = menu_row[0]
        menu_price = menu_row[3]
        menu_cost = menu_row[4]     
    #Calculate price & cost    
        if sale_item == menu_item:
            report[menu_item]['02-revenue'] += (int(menu_price) * int(quantity))
            report[menu_item]['03-cogs'] += (int(menu_cost) * int(quantity))
            

#Use revenue and cogs to calculate profit
for item, value, in report.items():
    for key in value:
        cogs = report[item]['03-cogs']
        revenue = report[item]['02-revenue']
        if key == '04-profit':
            report[item][key] = revenue - cogs

#Write file pyramen_analysis.txt
with open('pyramen_analysis.txt' , 'w') as pyramen_analysis:
    pyramen_analysis.write('Financial Report for PyRamen.\n')
    for key in report:
        pyramen_analysis.write(f'{key} {report[key]}\n')