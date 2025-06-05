# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent /= 100
        price = price - (price*discount_percent)
        print(f"DISCOUNT APPLIED")
        return price
    else:
        print(f"DISCOUNT NOT APPLIED")
        return price
    
amount = float(input("Enter price: "))
discount = float(input("Enter discount in whole number e.g '20%' should be 20: "))

final_price = calculate_discount(amount, discount)

print(f"The final price is: Ksh {final_price:.2f}")