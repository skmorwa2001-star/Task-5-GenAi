# Import the shop_package

import task3_shop_package.discount as disc
from task3_shop_package.billing import calculate_total
from task3_shop_package.billing import apply_tax


# Example
## 1000 price par 10% discount apply hoga
print("Discounted Price:",disc.apply_discount(1000, 10))

# List of product
prices= [100, 200, 300]

# Using calculate.total() from billing.py
## ye list ke saare prices ka total nikalega

total=calculate_total(prices)
print("Total Bill:", total)

# Using apply_tax() from billing.py
## Total amount par 5% tax add hoga

print("Total with tax:", apply_tax(total))