#LoveSeat Varibles
lovely_loveseat_description = "Lovely Loveseat. Tufted pilyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white"

lovely_loveseat_price = 254.00

#Settee Varibles
stylish_settee_description = "Stlyish Settee. Faux leather on birch. 29.50 inches high z 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

#Lamp Varibles 
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

#Tax Varible 
sales_tax = .088

#Customer_one total varibles
customer_one_total = 0 
customer_one_itemization = ""

#Cutomer_one Purchases 
#buying loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#buying lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += " " + luxurious_lamp_description

#Updating customer_one price with Tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Printing Customer_one Receipt
print("Customer One Items: " + customer_one_itemization + "Customer One Total: " + str(customer_one_total))