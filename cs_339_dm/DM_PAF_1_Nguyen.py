# 3 Monthly Sales Tax
COUNTRY_TAX_PERCENTAGE=0.05
STATE_TAX_PERCENTAGE=0.025

def main():

    countrySales=input("What is the amount of country sales?: ")
    stateSales=input("What is the amount of state sales?: ")

    calTotalSalesTax(countrySales, stateSales)


def calTotalSalesTax(totalCountrySales, totalStateSales):
    totalCountrySalesTax=float(totalCountrySales) * COUNTRY_TAX_PERCENTAGE
    totalStateSalesTax=float(totalStateSales) * STATE_TAX_PERCENTAGE

    totalSalesTax = totalCountrySalesTax + totalStateSalesTax

    print(totalSalesTax)


main()
