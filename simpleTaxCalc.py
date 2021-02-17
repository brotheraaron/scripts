# Rates are for married filing jointly.
# I made this for me so it's a lot of hardcoded values.
# This code meets two goals:
# 1. Let's me play with python a little bit.
# 2. Tells me what effective tax rates are based on income entered if no deductions taken.

# Why would I want to know this? 
# I'm a nerd and I think of random stuff all time, thank you for visiting.


# amount = 123456.78
# currency = "${:,.2f}".format(amount)

# 10% $0 to $19,900

# 12% $19,901 to $81,050

# 22% $81,051 to $172,750

# 24% $172,751 to $329,850

# 32% $329,851 to $418,850

# 35%	$418,851 to $628,300

# 37% $628,301 or more

wages = float(input("Enter wages: $ "))
wagesFull = wages

print("Wages entered:", "${:,.2f}".format(wagesFull), "\n")

if (wages <= 19900):
    taxes = wages * .1
    print("[10%] $0 to $19,900 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" , "\n")
    quit()
else:
    taxes = 19900 * .1
    wages = wages - 19900
    print("[10%] $0 to $19,900 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
if (wages <= 81050):
    taxes = taxes + (wages * .12)
    print("[12%] $19,901 to $81,050 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
    quit()
else:
    taxes = taxes + (81050 * .12) 
    wages = wages - 81050
    print("[12%] $19,901 to $81,050 \n Total Taxes Due ", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
if (wages <= 172750):
    taxes = taxes + (wages * .22)
    print("[22%] $81,051 to $172,750 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
    quit()
else:
    taxes = taxes + (172750 * .22)
    wages = wages - 172750
    print("[22%] $81,051 to $172,750 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
if (wages <= 329850):
    taxes = taxes + (wages * .24)
    print("[24%] $172,751 to $329,850 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
    quit()
else:
    taxes = taxes + (329850 * .24)
    wages = wages - 329850
    print("[24%] $172,751 to $329,850 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
if (wages <= 418850):
    taxes = taxes + (wages * .32)
    print("[32%] $329,851 to $418,850 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
    quit()
else:
    taxes = taxes + (418850 * .32)
    wages = wages - 418850
    print("[32%] $329,851 to $418,850 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
if (wages <= 628300):
    taxes = taxes + (wages * .35)
    print("[35%] $418,851 to $628,300 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
    quit()
else:
    taxes = taxes + (628300 * .35)
    wages = wages - 628300
    print("[35%] $418,851 to $628,300 \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")
if (wages >= 628,301):
    taxes = taxes + ((wages - 628301) * .37)
    wages = wages - 628300
    print("[37%] $628,301 or more \n Total Taxes Due $", "{:,.2f}".format(taxes),  "Effective Tax Rate:", round(((taxes/wagesFull) * 100),2), "%" ,"\n")


# print("Total Taxes Due $", "{:,.2f}".format(taxes), " Wages Taxed $ ", wages)
