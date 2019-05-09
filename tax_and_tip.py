# Created by: Andrew Coxall
HST_AMOUNT = 0.13
#print(type(HST_AMOUNT))
money_for_tip = 0.00

print ("Welcome to the mars circus\n")
person_name = input ('Plese say your name: ' )
print("Hello: " + person_name) 
#print ("Hello")

#Math starts 
#print ("How much would you like to pay? ")
cost_of_food = float(input("Say how much you would like to pay: ")) 
money_for_tax = HST_AMOUNT * (cost_of_food) 

subtotal = money_for_tax + (cost_of_food)
#print (final_part)

# Money for tip 
print ("Would you like to tip?")
tip_yes_or_no = input("yes? no?: ")
if tip_yes_or_no == "yes":
    tip_cost = input("Say how much you would like to tip: ")
    money_for_tip = float(tip_cost) * float(cost_of_food)
    print ("Your tip costs: ${:.2f}" .format(money_for_tip))

    #All added up
    #all_added_up = money_for_tip + money_for_tax + float(cost_of_food)
    #print ("Your total costs: ${:.2f}" .format(all_added_up))
    #print ("have a nice day")

#else:
#    all_added_up_no_tip = money_for_tax + float(cost_of_food)
#    print ("You know I make less than minimum wage right")
#    print ("Your bill comes to $")
#    print (all_added_up_no_tip)

    
print ("Your tax costs: ${:.2f}" .format(money_for_tax))
all_added_up = money_for_tip + money_for_tax + float(cost_of_food)
print("")
print("You payed: ${:.2f}" .format(cost_of_food))
print("Your total costs: ${:.2f}" .format(all_added_up))
print ("Have a nice day")

print("")
print("Done")
