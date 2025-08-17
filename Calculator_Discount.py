def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

original_price = float(input ("Enter original_price:"))
discount_percentage = float(input("Enter discount percentage:"))

final_price = calculate_discount(original_price, discount_percentage)
if final_price < original_price:
    print(f"Final price after discount:{final_price:}")
else:
    print(f"No discount applied.")
    print(f"Final price remains: {original_price}")

# End of Calculator_Discount.py