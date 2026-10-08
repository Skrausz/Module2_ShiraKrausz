'''
Shira Krausz's Campus Cafe
This function will present menu choices, take in input, calculate totals including tip and tax, and generate an output of a receipt
'''

'''Creating main function '''
def main():

#print menu
    print("Coffee - $2.25")
    print("Muffin - $2.75")

# set variables for unit prices
    unit_price_c = 2.25
    unit_price_m = 2.75

#takes input of amount of coffees, muffins, and tip percent.Coverts into integers
    coffees = int(input("How many coffees? "))
    muffins = int(input("How many muffins? "))
    tip_percent = int(input("Enter tip percent "))

#calculates total price of coffees and muffins
    total_coffees = unit_price_c * coffees
    total_muffins = unit_price_m * muffins

#calculates subtotal
    subtotal = total_coffees + total_muffins

# Find tax and tip based off of subtotal
    tax = subtotal * 0.08875
    tip = subtotal * tip_percent/100

 # Calculates total
    total = subtotal + tax + tip

 #prints receipt converting floats to have to decimal places with .2f
    receipt = ["----","Receipt:",f"{coffees} x Coffee @ $2.25 = ${total_coffees:.2f}",f"{muffins} x Coffee @ $2.25 = ${total_muffins:.2f}",f"Subtotal:${subtotal:.2f}",f"Tax:${tax:.2f}",f"Tip:${tip:.2f}",f"Total:${total:.2f}"]
    for item in receipt:
        print (item)

#running function
main()