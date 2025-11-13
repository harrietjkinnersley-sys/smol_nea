#report calculations 
#costs

transport = input(float("Enter Transport cost"))
storage = input(float("Enter storage cost"))
wages = input(float("Enter wages cost"))
manufacturing = input(float("Enter manufacturing cost"))
refunds = input(float("Enter cost refunded"))
subscription = input(float("Enter subscription cost"))
sales = input(float("Enter sales total"))

spends = transport + storage + wages + manufacturing + refunds
imports = subscription + sales

#product categories
liquid = input(int("Sales made from liquid based products"))
powder = input(int("Sales made from powder based products"))
utensils = input(int("Sales of utensils sold"))
 
 
# report

print ("-"*20)
print ("\x1B[4m" + "Summary report" + "\x1B[0m") # underlined title
print ("Profit =", imports - spends)

if liquid > powder and liquid > utensils:
    print ("Best selling category of products at this time is Liquid Based")

elif powder > liquid and powder > utensils:
    print ("Best selling category of products at this time is Powder Based")

else:
    print ("Best selling category of products at this time is utensils")
