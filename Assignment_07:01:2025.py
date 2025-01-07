#1.Calculation of cost of trip
'''def Total_trip_cost(kilometers, liters_per_km, price_per_liter):
    total_liters = kilometers * liters_per_km
    total_cost = total_liters * price_per_liter
    return total_cost


kilometers = float(input("Enter kilometers to drive: "))
liters_per_km = float(input("Enter liters per kilometer usage of the car: "))
price_per_liter = float(input("Enter price per liter of fuel: "))


cost = Total_trip_cost(kilometers, liters_per_km, price_per_liter)
print("The total cost of the trip is: "+ "Rs."+str(cost))'''


#2.Calculation of all expenses 
def Final_cost(quantity, price_per_item):
    if quantity > 10:
        discount=0.10
    else:
        discount=0.0
    total_cost = quantity * price_per_item
    final_cost = total_cost - (total_cost * discount)
    return final_cost

quantity = int(input("Enter the quantity of items purchased: "))
price_per_item = float(input("Enter the price per item: "))

final_cost = Final_cost(quantity, price_per_item)
print("Final cost of items is: ","Rs.",str(final_cost))

